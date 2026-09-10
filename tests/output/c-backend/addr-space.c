#line 3 "/home/siddhartha/work/git/cif/tests/input/c-backend/addr-space.c"
int counter;
#line 5 "/home/siddhartha/work/git/cif/tests/input/c-backend/addr-space.c"
extern int __seg_gs pcpu;
#line 7 "/home/siddhartha/work/git/cif/tests/input/c-backend/addr-space.c"
int main(void)
{
  {
#line 9 "/home/siddhartha/work/git/cif/tests/input/c-backend/addr-space.c"
    int __seg_gs *p = ( int __seg_gs *) & counter;
#line 11 "/home/siddhartha/work/git/cif/tests/input/c-backend/addr-space.c"
    return ( int ) * p + ( int ) pcpu;
  }
#line 0 "<built-in>"
  return 0;
}
