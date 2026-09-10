#include <stdio.h>
#include <stdlib.h>

struct stack {
    int *items;
    int size;
    int top;
};

struct stack *stack_new(int size)
{
    struct stack *s = malloc(sizeof(*s));

    s->items = malloc(size * sizeof(int));
    s->size = size;
    s->top = 0;

    return s;
}

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
