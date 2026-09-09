typedef int my_int;
#line 3 "/home/siddhartha/work/git/cif/tests/input/aspect_patterns.c"
int global_arr[10U];
#line 5 "/home/siddhartha/work/git/cif/tests/input/aspect_patterns.c"
my_int global_var = 7;
#line 7 "/home/siddhartha/work/git/cif/tests/input/aspect_patterns.c"
static int helper(int *, my_int);
#line 9 "/home/siddhartha/work/git/cif/tests/input/aspect_patterns.c"
static int cif_helper(int *ptr, my_int num)
{
  return ( int ) ( ( my_int ) * ptr + num );
}
static int cif_helper(int *, my_int);
#line 9 "/home/siddhartha/work/git/cif/tests/input/aspect_patterns.c"
static int helper(int *ptr, my_int num);
#line 14 "/home/siddhartha/work/git/cif/tests/input/aspect_patterns.c"
int caller(void)
{
  global_var = 3;
#line 18 "/home/siddhartha/work/git/cif/tests/input/aspect_patterns.c"
  return helper ( ( int *) & global_arr , global_var );
}
#line 3 "/home/siddhartha/work/git/cif/tests/work/res_ret_type.c.aux"
static int helper(int *ptr, my_int num)
{
  typedef int ldv_func_ret_type;
#line 7 "/home/siddhartha/work/git/cif/tests/work/res_ret_type.c.aux"
  ldv_func_ret_type ldv_func_res = cif_helper ( ptr , num );
#line 9 "/home/siddhartha/work/git/cif/tests/work/res_ret_type.c.aux"
  ldv_func_ret_type ldv_saved_res = ldv_func_res;
  ( void ) ldv_saved_res;
#line 12 "/home/siddhartha/work/git/cif/tests/work/res_ret_type.c.aux"
  return ( int ) ldv_func_res;
}
