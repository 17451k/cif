int global_var;

int assign_global(int arg)
{
    global_var = arg;

    return global_var;
}

int assign_local(int arg)
{
    int local_var = 0;

    local_var = arg;

    return local_var;
}
