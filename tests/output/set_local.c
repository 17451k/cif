int global_var;
#line 3 "/home/siddhartha/work/git/cif/tests/input/var_pointcuts.c"
int assign_global(int arg)
{
  global_var = arg;
#line 7 "/home/siddhartha/work/git/cif/tests/input/var_pointcuts.c"
  return global_var;
}
#line 11 "/home/siddhartha/work/git/cif/tests/input/var_pointcuts.c"
int cif_set_local_var(int);
#line 10 "/home/siddhartha/work/git/cif/tests/input/var_pointcuts.c"
int assign_local(int arg)
{
  int local_var = 0;
#line 14 "/home/siddhartha/work/git/cif/tests/input/var_pointcuts.c"
  local_var = cif_set_local_var
#line 11 "/home/siddhartha/work/git/cif/tests/input/var_pointcuts.c"
  ( arg );
#line 16 "/home/siddhartha/work/git/cif/tests/input/var_pointcuts.c"
  return local_var;
}
#line 1 "/home/siddhartha/work/git/cif/tests/work/set_local.c.aux"
int cif_set_local_var(int ldv_var_arg)
{
#line 4 "/home/siddhartha/work/git/cif/tests/work/set_local.c.aux"
  ldv_var_arg++;
#line 6 "/home/siddhartha/work/git/cif/tests/work/set_local.c.aux"
  return ldv_var_arg;
}
