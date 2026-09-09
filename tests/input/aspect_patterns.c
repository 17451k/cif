typedef int my_int;

int global_arr[10];

my_int global_var = 7;

static int helper(int *ptr, my_int num);

static int helper(int *ptr, my_int num)
{
    return ptr[0] + num;
}

int caller(void)
{
    global_var = 3;

    return helper(global_arr, global_var);
}
