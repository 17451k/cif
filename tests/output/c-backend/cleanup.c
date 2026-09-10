#line 4 "/home/siddhartha/work/git/cif/tests/input/c-backend/cleanup.c"
static void unlock(int *lock)
{
  * lock = 0;
}
#line 9 "/home/siddhartha/work/git/cif/tests/input/c-backend/cleanup.c"
int main(void)
{
  {
#line 11 "/home/siddhartha/work/git/cif/tests/input/c-backend/cleanup.c"
    int __attribute__((cleanup(unlock))) held = 1;
    {
#line 12 "/home/siddhartha/work/git/cif/tests/input/c-backend/cleanup.c"
      int other = 2;
#line 14 "/home/siddhartha/work/git/cif/tests/input/c-backend/cleanup.c"
      return held + other;
    }
  }
#line 0 "<built-in>"
  return 0;
}
