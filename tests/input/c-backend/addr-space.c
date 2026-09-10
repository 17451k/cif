/* Named address space qualifier on declarations. The Linux kernel uses
   __seg_gs for x86 per-cpu variables (arch/x86/include/asm/percpu.h). */
int counter;

extern int __seg_gs pcpu;

int main(void)
{
	typeof(counter) __seg_gs *p = (typeof(counter) __seg_gs *)&counter;

	return *p + pcpu;
}
