# CIF

CIF (C Instrumentation Framework) is a tool that implements
[aspect-oriented programming](http://en.wikipedia.org/wiki/Aspect-oriented_programming) for the C programming
language.

## Why aspects?

Some things a program has to do cannot live in one function or one file: check API contracts, trace calls, count
resources, inject faults, collect facts about the code for other tools.
Written by hand, such code ends up scattered over every place where it applies and stays there forever.
An *aspect* describes such a concern once, in terms of *join points* of the program (calls, definitions, macro
expansions, variable accesses), and CIF *weaves* it in at build time.
The program itself stays as it is, and the aspect can be dropped, replaced or stacked with others.

Take a stack that trusts its callers.
Pushing to a full stack silently corrupts memory; nothing tells you that until something else breaks:

```c
struct stack {
    int *items;
    int size;
    int top;
};

void stack_push(struct stack *s, int value)
{
    s->items[s->top++] = value;
}

int stack_pop(struct stack *s)
{
    return s->items[--s->top];
}

int main(void)
{
    struct stack *s = stack_new(2);

    stack_push(s, 1);
    stack_push(s, 2);
    stack_push(s, 3);

    printf("%d\n", stack_pop(s));

    return 0;
}
```

```console
$ gcc stack.c -o stack && ./stack
3
```

Here is an aspect that enforces the preconditions of the stack API at every call site.
An advice consists of a *pointcut* (`call(...)`, which matches calls of a function with the given signature) and a
body in plain C that can use the arguments of the matched call by name:

```c
before: call(void stack_push(struct stack *s, int value))
{
    if (s->top == s->size) {
        fprintf(stderr, "stack_push(): pushing %d to a full stack of size %d\n", value, s->size);
        abort();
    }
}

before: call(int stack_pop(struct stack *s))
{
    if (s->top == 0) {
        fprintf(stderr, "stack_pop(): popping from an empty stack\n");
        abort();
    }
}
```

CIF takes the program and the aspect and produces a binary, or, with `--back-end src`, a woven C source file:

```console
$ cif --in stack.c --aspect stack.aspect --out stack --back-end bin && ./stack
stack_push(): pushing 3 to a full stack of size 2
Aborted (core dumped)
```

Under the hood every matched call is redirected to an auxiliary function that runs the advice body and then the
original call, so the woven source is ordinary C that any compiler accepts (line directives and explicit casts that
CIF adds are omitted here):

```c
    cif_stack_push ( s , 1 );
    cif_stack_push ( s , 2 );
    cif_stack_push ( s , 3 );
...
static void cif_stack_push(struct stack *s, int value)
{
  if (( * s ) . top == ( * s ) . size)
  {
    fprintf ( stderr , "stack_push(): pushing %d to a full stack of size %d\n" , value , ( * s ) . size );
    abort ( );
  }
  stack_push ( s , value );
}
```

The same mechanism works for `around` advices that replace a call and decide whether to `$proceed` with it, for
`after` advices that see the result, and for join points other than calls: function definitions, macro expansions,
assignments to variables, definitions of structures.
Aspects can also *query* the program instead of changing it, for example to list every call of every function together
with the caller and the line, which is how [Klever](https://github.com/ldv-klever/klever) and
[Clade](https://github.com/17451k/clade) use CIF to extract facts from the Linux kernel.

The example above is available in `docs/samples` (`stack.c` and `stack.aspect`), and the [tutorial](docs/tutorial.md)
walks through the other kinds of join points.

## Contents

* [Deployment](docs/deploy.md)
* [Tutorial](docs/tutorial.md)
* [Aspect-Oriented C](docs/aoc.md)
* [Development](docs/development.md)

## Acknowledgments

CIF and Aspectator are created by Evgeny Novikov.
