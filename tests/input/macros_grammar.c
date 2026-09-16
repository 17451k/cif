#define OBJ 1
#define EMPTY()
#define ONE(a) (a)
#define TWO(a, b) ((a)+(b))
#define THREE(a, b, c) ((a)+(b)+(c))
#define VAR(...) 0
#define NVAR(args...) 0
#define PRE(a, ...) (a)
#define NPRE(a, rest...) (a)

int main() {
    EMPTY();
    return OBJ + ONE(1) + TWO(1, 2) + THREE(1, 2, 3) + VAR(1, 2) + NVAR(1, 2) + PRE(1, 2) + NPRE(1, 2);
}
