int gi;
static int si;
extern int ei;
const int ci = 1;
volatile int vi;
unsigned long ul;
long long ll;
char *cp;
const char *ccp;
char *const cpc = 0;
int arr3[3];
int arr5[5];
int arr2d[2][3];
int (*fp)(int);
void (*fpv)(void);
struct S { int a; } gs;
union U { int b; } gu;
enum E { E0 } ge;
typedef int myint;
myint mi;
double d;
float f;
_Bool bo;

void fv(void) {}
int fi(int a) { return a; }
static int sfi(int a) { return a; }
unsigned long ful(unsigned long a) { return a; }
int fva(const char *fmt, ...) { return 0; }
int ftwo(int a, char *b) { return a; }
int farr(int a[3]) { return a[0]; }
int ffp(int (*cb)(int)) { return cb(1); }
char *fcp(void) { return 0; }
struct S fs(struct S s) { return s; }
int fnp() { return 0; }
myint fmy(myint a) { return a; }
static inline int sinlf(int a) { return a; }

int main(void) {
    int r = gi;
    r += si;
    r += ci;
    r += arr3[0];
    r += arr5[0];
    r += arr2d[0][0];
    r += vi;
    r += ul;
    r += ll;
    r += mi;
    r += d;
    r += f;
    r += bo;
    ei = r;
    r += *cp;
    r += *ccp;
    r += *cpc;
    r += fp ? 1 : 0;
    r += fpv ? 1 : 0;
    r += gs.a;
    r += gu.b;
    r += ge;

    fv();
    r += fi(r);
    r += sfi(r);
    r += ful(r);
    r += fva("x");
    r += ftwo(r, cp);
    r += farr(arr3);
    r += ffp(fp);
    r += *fcp();
    struct S sv = fs(gs);
    r += sv.a;
    r += fnp();
    r += fmy(mi);
    r += sinlf(r);

    return r;
}
