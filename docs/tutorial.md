<a id="tutorial"></a>

# Tutorial

This section describes several typical cases of using CIF as well as current most vital limitations.
CIF has a bunch of command-line options that you can investigate by running it with *-h* or *--help*.
In the given tutorial we will consider only the following ones:

* *--in* -- a path to a C source file to be processed.
* *--aspect* -- a path to an aspect file.
  Below there will be several examples of aspect files.
* *--out* -- a path where a result will be placed.
* *--back-end* -- a kind of a back-end to be used, e.g. 'src' or 'bin'.

If you are going to try provided examples, we recommend to change your current directory to `docs/samples` within
the source tree root.
Hereinafter all file paths and commands will be relative to that directory.

For all use cases below we will consider as an input the C source file presented in [Listing 1](#input-c-source-file).
You can find it here: `calculate-max-rectangle-square.c`.

<a id="input-c-source-file"></a>

**Listing 1. Input C source file**

```c
/* This is a very simple program that finds out a rectangle with a maximum square from a provided list of rectangle
   heights and widths. It is intended only for demonstration of CIF capabilities. Please, do not use it anywhere since
   it contains several issues.
   The program expects the following input:
       height1 width1 height2 width2 ... heightN widthN
   where heighti and widthi should be integers representing respectively height and width of ith rectangle. */
#include <stdio.h>
#include <stdlib.h>

#define MAX(a, b) (a > b ? a : b)

struct rectangle
{
    unsigned int height;
    unsigned int width;
    unsigned int square;
};

unsigned int calculate_rectangle_square(struct rectangle *r)
{
    r->square = r->height * r->width;
    return r->square;
}

int main(int argc, const char *argv[])
{
    unsigned int rectangles_num;
    struct rectangle *rectangles;
    unsigned int cur_max_rectangle_square = 0;

    rectangles_num = (unsigned int)(argc / 2);
    rectangles = calloc(rectangles_num, sizeof(*rectangles));

    for (int i = 0; i < rectangles_num; i++) {
        struct rectangle *cur_rectangle = rectangles + i;
        cur_rectangle->height = atoi(argv[2 * i + 1]);
        cur_rectangle->width = atoi(argv[2 * i + 2]);
        calculate_rectangle_square(cur_rectangle);
        cur_max_rectangle_square = MAX(cur_max_rectangle_square, cur_rectangle->square);
    }

    printf("Maximum rectangle square is %u\n", cur_max_rectangle_square);

    return 0;
}
```

Normal compilation and running of this program will result in the following output:

```console
$ gcc calculate-max-rectangle-square.c -o calculate-max-rectangle-square
$ ./calculate-max-rectangle-square 2 5 7 3 4 4
Maximum rectangle square is 21
```

## Weaving function calls

This is the most typical use case.
[Listing 2](#weave-func-calculate-rectangle-square-aspect) provides an example of an appropriate aspect file located in
`weave-func-calculate-rectangle-square.aspect`.

<a id="weave-func-calculate-rectangle-square-aspect"></a>

**Listing 2. Aspect file intended for weaving calls of function **calculate_rectangle_square()****

```c
/* Introduce extra checking and debugging for calls of function calculate_rectangle_square(). */
around: call(unsigned int calculate_rectangle_square(struct rectangle *r))
{
    unsigned int tmp, res;

    // Check for possible overflow.
    tmp  = r->height * r->width;
    if (r->height != 0 && tmp / r->height != r->width)
        printf("After multiplication of %u and %u there will be overflow, so you can get invalid result\n", r->height, r->width);

    // Invoke woven in function itself. 
    res = $proceed;

    // Debug its result.
    printf("Calculated rectangle square is %u (%u * %u)\n", res, r->height, r->width);

    return res;
}
```

To weave in the target C source file with the given aspect you can run the following command:

```console
$ ../../inst/bin/cif --in calculate-max-rectangle-square.c --aspect weave-func-calculate-rectangle-square.aspect --out calculate-max-rectangle-square --back-end bin
```

Then you will get the following output when running the generated program binary:

```console
$ ./calculate-max-rectangle-square 2 5 7 3 4 4
Calculated rectangle square is 10 (2 * 5)
Calculated rectangle square is 21 (7 * 3)
Calculated rectangle square is 16 (4 * 4)
Maximum rectangle square is 21
```

This demonstrates debugging and logging facilities of CIF.
Probably by some reason you would not like to add an appropriate code directly to program's source files.
So you can use aspect files instead in a similar way.

The same aspect also enables extra checking.
Therefore, you can get the following warning if you will intentionally violate implicit assumptions regarding possible
multiplication overflows:

```console
$ ./calculate-max-rectangle-square 4317358 6927345
After multiplication of 4317358 and 6927345 there will be overflow, so you can get invalid result
Calculated rectangle square is 1971072462 (4317358 * 6927345)
Maximum rectangle square is 1971072462
```

(the valid result should be 29907828354510).

## Weaving macros

Sometimes it may be necessary to change macros.
CIF is capable to do that.
`weave-macro-max.aspect` in [Listing 3](#weave-macro-max-aspect) contains an example that add extra debugging for
macro *MAX*.

<a id="weave-macro-max-aspect"></a>

**Listing 3. Aspect file intended for weaving macro **MAX****

```c
/* Notify when current maximum value is changed. It is assumed that "a" holds that value. */
around: define(MAX(a, b))
{
({unsigned int __max; if (a > b) {__max = a;} else {printf("Update maximum value from %u to %u\n", a, b); __max = b;} __max;})
}
```

On executing following commands you will get the output as follows:

```console
$ ../../inst/bin/cif --in calculate-max-rectangle-square.c --aspect weave-macro-max.aspect --out calculate-max-rectangle-square --back-end bin
$ ./calculate-max-rectangle-square 2 5 7 3 4 4
Update maximum value from 0 to 10
Update maximum value from 10 to 21
Maximum rectangle square is 21
```

## Weaving variables

[Listing 4](#weave-var-rectangles-num-aspect) shows how to weave in variable assignments.
The corresponding aspect file is `weave-var-rectangles-num.aspect`.

<a id="weave-var-rectangles-num-aspect"></a>

**Listing 4. Aspect file intended for weaving assignments of variable **rectangles_num****

```c
/* Do not consider last rectangle. */
after: set(unsigned int rectangles_num)
{
    $res--;
}
```

This aspect makes pretty artificial change (it excludes the last rectangle from calculations), but you can have some
more important things to do, e.g. you can dump all values assigned to a given variable.

To test this aspect you can run the following commands:

```console
$ ../../inst/bin/cif --in calculate-max-rectangle-square.c --aspect weave-var-rectangles-num.aspect --out calculate-max-rectangle-square --back-end bin
$ ./calculate-max-rectangle-square 2 5 7 3 4 4 8 9
Maximum rectangle square is 21
```

## Weaving compound types

CIF suggests means to modify compound types such as structures, unions and enumerations.
For instance, you can find an example of an appropriate aspect in [Listing 5](#weave-struct-rectangle-aspect)
(`weave-struct-rectangle.aspect` in `docs/samples`).

<a id="weave-struct-rectangle-aspect"></a>

**Listing 5. Aspect file intended for weaving structure **rectangle****

```c
/* It does not work at the moment. */
before: introduce(struct rectangle)
{
    unsigned int perimeter;
}

before: call(unsigned int calculate_rectangle_square(struct rectangle *r))
{
    /* Calculate, store and print rectangle perimeter in addition to square. */
    r->perimeter = r->height + r->width;
    printf("Calculated rectangle perimeter is %u (%u * %u)\n", r->perimeter, r->height, r->width);
}
```

This aspect adds extra field *perimeter* to the definition of structure *rectangle*.
Besides, through weaving of function *calculate_rectangle_square()* it calculates, stores and prints out perimeters for
all rectangles.

To test this aspect you can run the following commands:

```console
$ ../../inst/bin/cif --in calculate-max-rectangle-square.c --aspect weave-struct-rectangle.aspect --out calculate-max-rectangle-square --back-end bin
$ ./calculate-max-rectangle-square 2 5 7 3 4 4 8 9
Calculated rectangle perimeter is 7 (2 * 5)
Calculated rectangle perimeter is 10 (7 * 3)
Calculated rectangle perimeter is 8 (4 * 4)
Calculated rectangle perimeter is 17 (8 * 9)
Maximum rectangle square is 72
```

## Querying source code

CIF can execute different queries to target source files.
For instance, you can use aspect `query-func-calls.aspect` shown in [Listing 6](#query-func-calls-aspect) to find out
all function calls.

<a id="query-func-calls-aspect"></a>

**Listing 6. Aspect file demonstrating source code queries**

```c
/* Query all function calls and print some information on them. */
query: call($ $(..))
{
    $fprintf<"func-calls.txt", "Function %s() is called at line %d\n", $func_name, $call_line>
}
```

This aspect file will not affect your program.
You will only get an extra file at the weaving stage.
For instance:

```console
$ ../../inst/bin/cif --in calculate-max-rectangle-square.c --aspect query-func-calls.aspect --out calculate-max-rectangle-square --stage instrumentation
$ cat func-calls.txt
Function calloc() is called at line 32
Function atoi() is called at line 36
Function atoi() is called at line 37
Function calculate_rectangle_square() is called at line 38
Function printf() is called at line 42
```

(we asked CIF to stop after stage *instrumentation* since we would not like to get the program binary in this case).

## Invalid aspects

You can wonder how to track various issues with aspects.
First of all, CIF will fail and report appropriate errors if you will provide syntactically invalid aspects.
Sometimes, aspects can have valid syntax, but they might not work as expected.
[Listing 7](#weave-invalid-func-decl-aspect) presents the content of `weave-invalid-func-decl.aspect`.
Therein we deliberately specified invalid declaration for function *calculate_rectangle_square()*.

<a id="weave-invalid-func-decl-aspect"></a>

**Listing 7. Aspect file using invalid target function declaration**

```c
/* Declaration of function calculate_rectangle_square() is not valid intentionally. */
around: call(struct rectangle *calculate_rectangle_square(unsigned int, unsigned int))
{
}
```

You will not get any warnings if you will run CIF as usual:

```console
$ ../../inst/bin/cif --in calculate-max-rectangle-square.c --aspect weave-invalid-func-decl.aspect --out calculate-max-rectangle-square --back-end bin
```

But if you will set environment variable `LDV_PRINT_SIGNATURE_OF_MATCHED_BY_NAME` the situation will change:

```console
$ export LDV_PRINT_SIGNATURE_OF_MATCHED_BY_NAME=1
$ ../../inst/bin/cif --in calculate-max-rectangle-square.c --aspect weave-invalid-func-decl.aspect --out calculate-max-rectangle-square --back-end bin

These functions were matched by name but have different signatures:
  source function declaration: unsigned int calculate_rectangle_square (struct rectangle *r)
  aspect function declaration: struct rectangle *calculate_rectangle_square (unsigned int, unsigned int)
```

## Getting woven source files

It may be useful for debugging and necessary for some applications to get woven source files rather than binaries as an
output.
For instance, you can slightly change the command for the first use case (note the change of *bin* to *src* for
command-line option *--back-end*):

```console
$ ../../inst/bin/cif --in calculate-max-rectangle-square.c --aspect weave-func-calculate-rectangle-square.aspect --out calculate-max-rectangle-square --back-end src
```

and investigate outputted file `calculate-max-rectangle-square` that will be a C source file.

## Further study

CIF has much more capabilities in addition to the ones that we presented in this tutorial.
You can read [Aspect-Oriented C](aoc.md#aoc) that describes the aspect-oriented extension of the C programming language to study all possible
ways of using CIF.
Besides, you can find a lot of examples of aspects in projects [Klever](https://forge.ispras.ru/projects/klever) (in
particular, [here](https://klever.readthedocs.io/en/latest/dev_common_api_models.html) and
[here](https://klever.readthedocs.io/en/latest/dev_req_specs.html)) and [Clade](https://github.com/17451k/clade)
([here](https://github.com/17451k/clade/blob/master/clade/extensions/info/info.aspect)).

## Known issues

CIF is not used very widely, so there is a lot of different issues with it.
You can find the known issues in the [official issue tracker](https://forge.ispras.ru/projects/cif/issues).
The most vital ones are as follows:

* CIF does not have a command-line interface that is compatible with a compiler
  ([#6829](https://forge.ispras.ru/issues/6829)).
  Thus, you can not easily incorporate it into your program's build process.
* CIF does not support multiple advices for the same join point ([#358](https://forge.ispras.ru/issues/358)).
* CIF does not support well the entire C programming language with all [GCC](https://gcc.gnu.org/) compiler
  extensions.
  Other compiler extensions are supported to the extent that it is done by GCC itself (you can find some related
  command-line options [here](https://gcc.gnu.org/onlinedocs/gcc/C-Dialect-Options.html)).
* CIF is not particularly optimized.
  It is noticeable if it is called to handle hundreds or thousands of files.
