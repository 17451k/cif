/* __attribute__((cleanup)) as expanded from guard()/__free() in the Linux
   kernel (include/linux/cleanup.h). The C front end wraps the rest of the
   block into TRY_FINALLY_EXPR. */
static void unlock(int *lock)
{
	*lock = 0;
}

int main(void)
{
	int held __attribute__((cleanup(unlock))) = 1;
	int other = 2;

	return held + other;
}
