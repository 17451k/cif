#define ARRAY_SIZE (1L << 20)
int *array[ARRAY_SIZE] = {
    [0 ... ARRAY_SIZE - 1] = (void *)0
};

struct large_struct {
    int array[ARRAY_SIZE];
    int size;
} large_struct = {
    .array = { [0 ... ARRAY_SIZE - 1] = 0 },
    .size = ARRAY_SIZE
};
