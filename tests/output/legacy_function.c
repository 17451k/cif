#define LDV_MIN(X,Y) ((X) < (Y) ? (X) : (Y))
#define LDV_MAX(X,Y) ((X) > (Y) ? (X) : (Y))
#define LDV_ABS(X) ((X) < 0 ? -(X) : (X))
#define LDV_LROTATE(X,Y) (((X) << (Y)) | ((X) >> (__CHAR_BIT__ * sizeof (X) - Y)))
#define LDV_RROTATE(X,Y) (((X) >> (Y)) | ((X) << (__CHAR_BIT__ * sizeof (X) - Y)))
typedef struct __va_list_tag __va_list_tag;
#line 1 "input/legacy_function.c"
void ldv_a011(int arg)
{
}
#line 5 "input/legacy_function.c"
void ldv_a011(int);
#line 1 "input/legacy_function.c"
void a011(int arg);
#line 8 "input/legacy_function.c"
void ldv_a012(int arg)
{
}
#line 12 "input/legacy_function.c"
void ldv_a012(int);
#line 8 "input/legacy_function.c"
void a012(int arg);
#line 15 "input/legacy_function.c"
void ldv_a013(long long unsigned int const arg)
{
}
#line 19 "input/legacy_function.c"
void ldv_a013(long long unsigned int const);
#line 15 "input/legacy_function.c"
void a013(long long unsigned int const arg);
#line 22 "input/legacy_function.c"
void ldv_a014(long double arg)
{
}
#line 27 "input/legacy_function.c"
void ldv_a014(long double);
#line 22 "input/legacy_function.c"
void a014(long double arg);
#line 30 "input/legacy_function.c"
void *ldv_a020(int *arg)
{
  return ( ( void *) 0 );
}
#line 35 "input/legacy_function.c"
void *ldv_a020(int *);
#line 30 "input/legacy_function.c"
void *a020(int *arg);
#line 38 "input/legacy_function.c"
void ldv_a021(int *arg)
{
}
#line 42 "input/legacy_function.c"
void ldv_a021(int *);
#line 38 "input/legacy_function.c"
void a021(int *arg);
#line 45 "input/legacy_function.c"
void ldv_a022(int *arg)
{
}
#line 49 "input/legacy_function.c"
void ldv_a022(int *);
#line 45 "input/legacy_function.c"
void a022(int *arg);
#line 52 "input/legacy_function.c"
void ldv_a023(int *const *volatile arg)
{
}
#line 56 "input/legacy_function.c"
void ldv_a023(int *const *volatile);
#line 52 "input/legacy_function.c"
void a023(int *const *volatile arg);
#line 59 "input/legacy_function.c"
void ldv_a024(int *const *volatile arg)
{
}
#line 64 "input/legacy_function.c"
void ldv_a024(int *const *volatile);
#line 59 "input/legacy_function.c"
void a024(int *const *volatile arg);
#line 67 "input/legacy_function.c"
void ldv_a031(int *arg)
{
}
#line 71 "input/legacy_function.c"
void ldv_a031(int *);
#line 67 "input/legacy_function.c"
void a031(int *arg);
#line 74 "input/legacy_function.c"
void ldv_a032(int *arg)
{
}
#line 78 "input/legacy_function.c"
void ldv_a032(int *);
#line 74 "input/legacy_function.c"
void a032(int *arg);
#line 81 "input/legacy_function.c"
void ldv_a033(int (*arg)[20U][30U])
{
}
#line 85 "input/legacy_function.c"
void ldv_a033(int (*)[20U][30U]);
#line 81 "input/legacy_function.c"
void a033(int (*arg)[20U][30U]);
#line 88 "input/legacy_function.c"
void ldv_a034(int (*arg)[20U][30U])
{
}
#line 93 "input/legacy_function.c"
void ldv_a034(int (*)[20U][30U]);
#line 88 "input/legacy_function.c"
void a034(int (*arg)[20U][30U]);
#line 96 "input/legacy_function.c"
void ldv_a041(int **arg)
{
}
#line 100 "input/legacy_function.c"
void ldv_a041(int **);
#line 96 "input/legacy_function.c"
void a041(int **arg);
#line 103 "input/legacy_function.c"
void ldv_a042(int **arg)
{
}
#line 107 "input/legacy_function.c"
void ldv_a042(int **);
#line 103 "input/legacy_function.c"
void a042(int **arg);
#line 110 "input/legacy_function.c"
void ldv_a043(int *const *volatile (*arg)[20U][30U])
{
}
#line 114 "input/legacy_function.c"
void ldv_a043(int *const *volatile (*)[20U][30U]);
#line 110 "input/legacy_function.c"
void a043(int *const *volatile (*arg)[20U][30U]);
#line 117 "input/legacy_function.c"
void ldv_a044(int *const *volatile (*arg)[20U][30U])
{
}
#line 122 "input/legacy_function.c"
void ldv_a044(int *const *volatile (*)[20U][30U]);
#line 117 "input/legacy_function.c"
void a044(int *const *volatile (*arg)[20U][30U]);
#line 125 "input/legacy_function.c"
void ldv_a051(int (*arg)[10U])
{
}
#line 129 "input/legacy_function.c"
void ldv_a051(int (*)[10U]);
#line 125 "input/legacy_function.c"
void a051(int (*arg)[10U]);
#line 132 "input/legacy_function.c"
void ldv_a052(int (*arg)[10U])
{
}
#line 136 "input/legacy_function.c"
void ldv_a052(int (*)[10U]);
#line 132 "input/legacy_function.c"
void a052(int (*arg)[10U]);
#line 139 "input/legacy_function.c"
void ldv_a053(int (*const *volatile arg)[10U][20U][30U])
{
}
#line 143 "input/legacy_function.c"
void ldv_a053(int (*const *volatile)[10U][20U][30U]);
#line 139 "input/legacy_function.c"
void a053(int (*const *volatile arg)[10U][20U][30U]);
#line 146 "input/legacy_function.c"
void ldv_a054(int (*const *volatile arg)[10U][20U][30U])
{
}
#line 151 "input/legacy_function.c"
void ldv_a054(int (*const *volatile)[10U][20U][30U]);
#line 146 "input/legacy_function.c"
void a054(int (*const *volatile arg)[10U][20U][30U]);
#line 154 "input/legacy_function.c"
void ldv_a061(int **(*arg)[10U])
{
}
#line 158 "input/legacy_function.c"
void ldv_a061(int **(*)[10U]);
#line 154 "input/legacy_function.c"
void a061(int **(*arg)[10U]);
#line 161 "input/legacy_function.c"
void ldv_a062(int **(*arg)[10U])
{
}
#line 165 "input/legacy_function.c"
void ldv_a062(int **(*)[10U]);
#line 161 "input/legacy_function.c"
void a062(int **(*arg)[10U]);
#line 168 "input/legacy_function.c"
void ldv_a063(int *const *volatile (*const *volatile arg)[10U][20U][30U])
{
}
#line 172 "input/legacy_function.c"
void ldv_a063(int *const *volatile (*const *volatile)[10U][20U][30U]);
#line 168 "input/legacy_function.c"
void a063(int *const *volatile (*const *volatile arg)[10U][20U][30U]);
#line 175 "input/legacy_function.c"
void ldv_a064(int *const *volatile (*const *volatile arg)[10U][20U][30U])
{
}
#line 180 "input/legacy_function.c"
void ldv_a064(int *const *volatile (*const *volatile)[10U][20U][30U]);
#line 175 "input/legacy_function.c"
void a064(int *const *volatile (*const *volatile arg)[10U][20U][30U]);
#line 183 "input/legacy_function.c"
void ldv_a071(int (*arg)(void))
{
}
#line 187 "input/legacy_function.c"
void ldv_a071(int (*)(void));
#line 183 "input/legacy_function.c"
void a071(int (*arg)(void));
#line 190 "input/legacy_function.c"
void ldv_a072(int (*arg)(void))
{
}
#line 194 "input/legacy_function.c"
void ldv_a072(int (*)(void));
#line 190 "input/legacy_function.c"
void a072(int (*arg)(void));
#line 197 "input/legacy_function.c"
void ldv_a073(int (*const arg)(void))
{
}
#line 201 "input/legacy_function.c"
void ldv_a073(int (*const)(void));
#line 197 "input/legacy_function.c"
void a073(int (*const arg)(void));
#line 204 "input/legacy_function.c"
void ldv_a074(int (*const arg)(void))
{
}
#line 209 "input/legacy_function.c"
void ldv_a074(int (*const)(void));
#line 204 "input/legacy_function.c"
void a074(int (*const arg)(void));
#line 212 "input/legacy_function.c"
void ldv_a081(int **(*arg)(void))
{
}
#line 216 "input/legacy_function.c"
void ldv_a081(int **(*)(void));
#line 212 "input/legacy_function.c"
void a081(int **(*arg)(void));
#line 219 "input/legacy_function.c"
void ldv_a082(int **(*arg)(void))
{
}
#line 223 "input/legacy_function.c"
void ldv_a082(int **(*)(void));
#line 219 "input/legacy_function.c"
void a082(int **(*arg)(void));
#line 226 "input/legacy_function.c"
void ldv_a083(int *const *volatile *(*const arg)(void))
{
}
#line 230 "input/legacy_function.c"
void ldv_a083(int *const *volatile *(*const)(void));
#line 226 "input/legacy_function.c"
void a083(int *const *volatile *(*const arg)(void));
#line 233 "input/legacy_function.c"
void ldv_a084(int *const *volatile *(*const arg)(void))
{
}
#line 238 "input/legacy_function.c"
void ldv_a084(int *const *volatile *(*const)(void));
#line 233 "input/legacy_function.c"
void a084(int *const *volatile *(*const arg)(void));
#line 241 "input/legacy_function.c"
void ldv_a091(int (**arg)(void))
{
}
#line 245 "input/legacy_function.c"
void ldv_a091(int (**)(void));
#line 241 "input/legacy_function.c"
void a091(int (**arg)(void));
#line 248 "input/legacy_function.c"
void ldv_a092(int (**arg)(void))
{
}
#line 252 "input/legacy_function.c"
void ldv_a092(int (**)(void));
#line 248 "input/legacy_function.c"
void a092(int (**arg)(void));
#line 255 "input/legacy_function.c"
void ldv_a093(int (*const (*arg)[20U][30U])(void))
{
}
#line 259 "input/legacy_function.c"
void ldv_a093(int (*const (*)[20U][30U])(void));
#line 255 "input/legacy_function.c"
void a093(int (*const (*arg)[20U][30U])(void));
#line 262 "input/legacy_function.c"
void ldv_a094(int (*const (*arg)[20U][30U])(void))
{
}
#line 267 "input/legacy_function.c"
void ldv_a094(int (*const (*)[20U][30U])(void));
#line 262 "input/legacy_function.c"
void a094(int (*const (*arg)[20U][30U])(void));
#line 270 "input/legacy_function.c"
void ldv_a101(int **(**arg)(void))
{
}
#line 274 "input/legacy_function.c"
void ldv_a101(int **(**)(void));
#line 270 "input/legacy_function.c"
void a101(int **(**arg)(void));
#line 277 "input/legacy_function.c"
void ldv_a102(int **(**arg)(void))
{
}
#line 281 "input/legacy_function.c"
void ldv_a102(int **(**)(void));
#line 277 "input/legacy_function.c"
void a102(int **(**arg)(void));
#line 284 "input/legacy_function.c"
void ldv_a103(int *const *volatile *(*const *const volatile *(*arg)[20U][30U])(void))
{
}
#line 288 "input/legacy_function.c"
void ldv_a103(int *const *volatile *(*const *const volatile *(*)[20U][30U])(void));
#line 284 "input/legacy_function.c"
void a103(int *const *volatile *(*const *const volatile *(*arg)[20U][30U])(void));
#line 291 "input/legacy_function.c"
void ldv_a104(int *const *volatile *(*const *const volatile *(*arg)[20U][30U])(void))
{
}
#line 296 "input/legacy_function.c"
void ldv_a104(int *const *volatile *(*const *const volatile *(*)[20U][30U])(void));
#line 291 "input/legacy_function.c"
void a104(int *const *volatile *(*const *const volatile *(*arg)[20U][30U])(void));
#line 299 "input/legacy_function.c"
void (*ldv_a110(void))(void)
{
  return ( ( void (*)(void)) 0 );
}
#line 304 "input/legacy_function.c"
void (*ldv_a110(void))(void);
#line 299 "input/legacy_function.c"
void (*a110(void))(void);
#line 307 "input/legacy_function.c"
void ldv_a111(int (*(*arg)(void))(void))
{
}
#line 311 "input/legacy_function.c"
void ldv_a111(int (*(*)(void))(void));
#line 307 "input/legacy_function.c"
void a111(int (*(*arg)(void))(void));
#line 314 "input/legacy_function.c"
void ldv_a112(int (*(*arg)(void))(void))
{
}
#line 318 "input/legacy_function.c"
void ldv_a112(int (*(*)(void))(void));
#line 314 "input/legacy_function.c"
void a112(int (*(*arg)(void))(void));
#line 321 "input/legacy_function.c"
void ldv_a113(int (*const *(*arg)(void))(void))
{
}
#line 325 "input/legacy_function.c"
void ldv_a113(int (*const *(*)(void))(void));
#line 321 "input/legacy_function.c"
void a113(int (*const *(*arg)(void))(void));
#line 328 "input/legacy_function.c"
void ldv_a114(int (*const *(*arg)(void))(void))
{
}
#line 333 "input/legacy_function.c"
void ldv_a114(int (*const *(*)(void))(void));
#line 328 "input/legacy_function.c"
void a114(int (*const *(*arg)(void))(void));
#line 336 "input/legacy_function.c"
void **(*ldv_a120(void))(void)
{
  return ( ( void **(*)(void)) 0 );
}
#line 341 "input/legacy_function.c"
void **(*ldv_a120(void))(void);
#line 336 "input/legacy_function.c"
void **(*a120(void))(void);
#line 344 "input/legacy_function.c"
void ldv_a121(int **(*(*arg)(void))(void))
{
}
#line 348 "input/legacy_function.c"
void ldv_a121(int **(*(*)(void))(void));
#line 344 "input/legacy_function.c"
void a121(int **(*(*arg)(void))(void));
#line 351 "input/legacy_function.c"
void ldv_a122(int **(*(*arg)(void))(void))
{
}
#line 355 "input/legacy_function.c"
void ldv_a122(int **(*(*)(void))(void));
#line 351 "input/legacy_function.c"
void a122(int **(*(*arg)(void))(void));
#line 358 "input/legacy_function.c"
void ldv_a123(int *const volatile *(*const *(*arg)(void))(void))
{
}
#line 362 "input/legacy_function.c"
void ldv_a123(int *const volatile *(*const *(*)(void))(void));
#line 358 "input/legacy_function.c"
void a123(int *const volatile *(*const *(*arg)(void))(void));
#line 365 "input/legacy_function.c"
void ldv_a124(int *const volatile *(*const *(*arg)(void))(void))
{
}
#line 370 "input/legacy_function.c"
void ldv_a124(int *const volatile *(*const *(*)(void))(void));
#line 365 "input/legacy_function.c"
void a124(int *const volatile *(*const *(*arg)(void))(void));
#line 373 "input/legacy_function.c"
void ldv_a131(int arg1, double arg2)
{
}
#line 377 "input/legacy_function.c"
void ldv_a131(int, double);
#line 373 "input/legacy_function.c"
void a131(int arg1, double arg2);
#line 380 "input/legacy_function.c"
void ldv_a132(int arg1, double arg2)
{
}
#line 384 "input/legacy_function.c"
void ldv_a132(int, double);
#line 380 "input/legacy_function.c"
void a132(int arg1, double arg2);
#line 387 "input/legacy_function.c"
void ldv_a133(int *const *volatile *(*const *volatile *arg1)[10U][20U][30U], int *const *volatile *(*const *const volatile *(*arg2)[20U][30U])(void))
{
}
#line 391 "input/legacy_function.c"
void ldv_a133(int *const *volatile *(*const *volatile *)[10U][20U][30U], int *const *volatile *(*const *const volatile *(*)[20U][30U])(void));
#line 387 "input/legacy_function.c"
void a133(int *const *volatile *(*const *volatile *arg1)[10U][20U][30U], int *const *volatile *(*const *const volatile *(*arg2)[20U][30U])(void));
#line 394 "input/legacy_function.c"
void ldv_a134(int *const *volatile *(*const *volatile *arg1)[10U][20U][30U], int *const *volatile *(*const *const volatile *(*arg2)[20U][30U])(void))
{
}
#line 399 "input/legacy_function.c"
void ldv_a134(int *const *volatile *(*const *volatile *)[10U][20U][30U], int *const *volatile *(*const *const volatile *(*)[20U][30U])(void));
#line 394 "input/legacy_function.c"
void a134(int *const *volatile *(*const *volatile *arg1)[10U][20U][30U], int *const *volatile *(*const *const volatile *(*arg2)[20U][30U])(void));
#line 402 "input/legacy_function.c"
inline void ldv_a141(int arg1, double arg2)
{
}
#line 407 "input/legacy_function.c"
inline void ldv_a141(int, double);
#line 402 "input/legacy_function.c"
inline void a141(int arg1, double arg2);
#line 410 "input/legacy_function.c"
static void ldv_a151(int arg1, double arg2)
{
}
#line 415 "input/legacy_function.c"
static void ldv_a151(int, double);
#line 410 "input/legacy_function.c"
static void a151(int arg1, double arg2);
#line 418 "input/legacy_function.c"
static inline void ldv_a161(int arg1, double arg2)
{
}
#line 3 "work/legacy_function.c.aux"
static void a011(int arg)
{
#line 7 "work/legacy_function.c.aux"
  ldv_a011 ( arg );
}
#line 11 "work/legacy_function.c.aux"
static void a012(int arg)
{
#line 15 "work/legacy_function.c.aux"
  ldv_a012 ( arg );
}
#line 19 "work/legacy_function.c.aux"
static void a013(long long unsigned int const arg)
{
#line 23 "work/legacy_function.c.aux"
  ldv_a013 ( arg );
}
#line 27 "work/legacy_function.c.aux"
static void a014(long double arg)
{
#line 31 "work/legacy_function.c.aux"
  ldv_a014 ( arg );
}
#line 35 "work/legacy_function.c.aux"
static void *a020(int *arg)
{
#line 39 "work/legacy_function.c.aux"
  ldv_a020 ( arg );
}
#line 43 "work/legacy_function.c.aux"
static void a021(int *arg)
{
#line 47 "work/legacy_function.c.aux"
  ldv_a021 ( arg );
}
#line 51 "work/legacy_function.c.aux"
static void a022(int *arg)
{
#line 55 "work/legacy_function.c.aux"
  ldv_a022 ( arg );
}
#line 59 "work/legacy_function.c.aux"
static void a023(int *const *volatile arg)
{
#line 63 "work/legacy_function.c.aux"
  ldv_a023 ( arg );
}
#line 67 "work/legacy_function.c.aux"
static void a024(int *const *volatile arg)
{
#line 71 "work/legacy_function.c.aux"
  ldv_a024 ( arg );
}
#line 75 "work/legacy_function.c.aux"
static void a031(int *arg)
{
#line 79 "work/legacy_function.c.aux"
  ldv_a031 ( arg );
}
#line 83 "work/legacy_function.c.aux"
static void a032(int *arg)
{
#line 87 "work/legacy_function.c.aux"
  ldv_a032 ( arg );
}
#line 91 "work/legacy_function.c.aux"
static void a033(int (*arg)[20U][30U])
{
#line 95 "work/legacy_function.c.aux"
  ldv_a033 ( arg );
}
#line 99 "work/legacy_function.c.aux"
static void a034(int (*arg)[20U][30U])
{
#line 103 "work/legacy_function.c.aux"
  ldv_a034 ( arg );
}
#line 107 "work/legacy_function.c.aux"
static void a041(int **arg)
{
#line 111 "work/legacy_function.c.aux"
  ldv_a041 ( arg );
}
#line 115 "work/legacy_function.c.aux"
static void a042(int **arg)
{
#line 119 "work/legacy_function.c.aux"
  ldv_a042 ( arg );
}
#line 123 "work/legacy_function.c.aux"
static void a043(int *const *volatile (*arg)[20U][30U])
{
#line 127 "work/legacy_function.c.aux"
  ldv_a043 ( arg );
}
#line 131 "work/legacy_function.c.aux"
static void a044(int *const *volatile (*arg)[20U][30U])
{
#line 135 "work/legacy_function.c.aux"
  ldv_a044 ( arg );
}
#line 139 "work/legacy_function.c.aux"
static void a051(int (*arg)[10U])
{
#line 143 "work/legacy_function.c.aux"
  ldv_a051 ( arg );
}
#line 147 "work/legacy_function.c.aux"
static void a052(int (*arg)[10U])
{
#line 151 "work/legacy_function.c.aux"
  ldv_a052 ( arg );
}
#line 155 "work/legacy_function.c.aux"
static void a053(int (*const *volatile arg)[10U][20U][30U])
{
#line 159 "work/legacy_function.c.aux"
  ldv_a053 ( arg );
}
#line 163 "work/legacy_function.c.aux"
static void a054(int (*const *volatile arg)[10U][20U][30U])
{
#line 167 "work/legacy_function.c.aux"
  ldv_a054 ( arg );
}
#line 171 "work/legacy_function.c.aux"
static void a061(int **(*arg)[10U])
{
#line 175 "work/legacy_function.c.aux"
  ldv_a061 ( arg );
}
#line 179 "work/legacy_function.c.aux"
static void a062(int **(*arg)[10U])
{
#line 183 "work/legacy_function.c.aux"
  ldv_a062 ( arg );
}
#line 187 "work/legacy_function.c.aux"
static void a063(int *const *volatile (*const *volatile arg)[10U][20U][30U])
{
#line 191 "work/legacy_function.c.aux"
  ldv_a063 ( arg );
}
#line 195 "work/legacy_function.c.aux"
static void a064(int *const *volatile (*const *volatile arg)[10U][20U][30U])
{
#line 199 "work/legacy_function.c.aux"
  ldv_a064 ( arg );
}
#line 203 "work/legacy_function.c.aux"
static void a071(int (*arg)(void))
{
#line 207 "work/legacy_function.c.aux"
  ldv_a071 ( arg );
}
#line 211 "work/legacy_function.c.aux"
static void a072(int (*arg)(void))
{
#line 215 "work/legacy_function.c.aux"
  ldv_a072 ( arg );
}
#line 219 "work/legacy_function.c.aux"
static void a073(int (*const arg)(void))
{
#line 223 "work/legacy_function.c.aux"
  ldv_a073 ( arg );
}
#line 227 "work/legacy_function.c.aux"
static void a074(int (*const arg)(void))
{
#line 231 "work/legacy_function.c.aux"
  ldv_a074 ( arg );
}
#line 235 "work/legacy_function.c.aux"
static void a081(int **(*arg)(void))
{
#line 239 "work/legacy_function.c.aux"
  ldv_a081 ( arg );
}
#line 243 "work/legacy_function.c.aux"
static void a082(int **(*arg)(void))
{
#line 247 "work/legacy_function.c.aux"
  ldv_a082 ( arg );
}
#line 251 "work/legacy_function.c.aux"
static void a083(int *const *volatile *(*const arg)(void))
{
#line 255 "work/legacy_function.c.aux"
  ldv_a083 ( arg );
}
#line 259 "work/legacy_function.c.aux"
static void a084(int *const *volatile *(*const arg)(void))
{
#line 263 "work/legacy_function.c.aux"
  ldv_a084 ( arg );
}
#line 267 "work/legacy_function.c.aux"
static void a091(int (**arg)(void))
{
#line 271 "work/legacy_function.c.aux"
  ldv_a091 ( arg );
}
#line 275 "work/legacy_function.c.aux"
static void a092(int (**arg)(void))
{
#line 279 "work/legacy_function.c.aux"
  ldv_a092 ( arg );
}
#line 283 "work/legacy_function.c.aux"
static void a093(int (*const (*arg)[20U][30U])(void))
{
#line 287 "work/legacy_function.c.aux"
  ldv_a093 ( arg );
}
#line 291 "work/legacy_function.c.aux"
static void a094(int (*const (*arg)[20U][30U])(void))
{
#line 295 "work/legacy_function.c.aux"
  ldv_a094 ( arg );
}
#line 299 "work/legacy_function.c.aux"
static void a101(int **(**arg)(void))
{
#line 303 "work/legacy_function.c.aux"
  ldv_a101 ( arg );
}
#line 307 "work/legacy_function.c.aux"
static void a102(int **(**arg)(void))
{
#line 311 "work/legacy_function.c.aux"
  ldv_a102 ( arg );
}
#line 315 "work/legacy_function.c.aux"
static void a103(int *const *volatile *(*const *const volatile *(*arg)[20U][30U])(void))
{
#line 319 "work/legacy_function.c.aux"
  ldv_a103 ( arg );
}
#line 323 "work/legacy_function.c.aux"
static void a104(int *const *volatile *(*const *const volatile *(*arg)[20U][30U])(void))
{
#line 327 "work/legacy_function.c.aux"
  ldv_a104 ( arg );
}
#line 331 "work/legacy_function.c.aux"
static void (*a110(void))(void)
{
#line 335 "work/legacy_function.c.aux"
  ldv_a110 ( );
}
#line 339 "work/legacy_function.c.aux"
static void a111(int (*(*arg)(void))(void))
{
#line 343 "work/legacy_function.c.aux"
  ldv_a111 ( arg );
}
#line 347 "work/legacy_function.c.aux"
static void a112(int (*(*arg)(void))(void))
{
#line 351 "work/legacy_function.c.aux"
  ldv_a112 ( arg );
}
#line 355 "work/legacy_function.c.aux"
static void a113(int (*const *(*arg)(void))(void))
{
#line 359 "work/legacy_function.c.aux"
  ldv_a113 ( arg );
}
#line 363 "work/legacy_function.c.aux"
static void a114(int (*const *(*arg)(void))(void))
{
#line 367 "work/legacy_function.c.aux"
  ldv_a114 ( arg );
}
#line 371 "work/legacy_function.c.aux"
static void **(*a120(void))(void)
{
#line 375 "work/legacy_function.c.aux"
  ldv_a120 ( );
}
#line 379 "work/legacy_function.c.aux"
static void a121(int **(*(*arg)(void))(void))
{
#line 383 "work/legacy_function.c.aux"
  ldv_a121 ( arg );
}
#line 387 "work/legacy_function.c.aux"
static void a122(int **(*(*arg)(void))(void))
{
#line 391 "work/legacy_function.c.aux"
  ldv_a122 ( arg );
}
#line 395 "work/legacy_function.c.aux"
static void a123(int *const volatile *(*const *(*arg)(void))(void))
{
#line 399 "work/legacy_function.c.aux"
  ldv_a123 ( arg );
}
#line 403 "work/legacy_function.c.aux"
static void a124(int *const volatile *(*const *(*arg)(void))(void))
{
#line 407 "work/legacy_function.c.aux"
  ldv_a124 ( arg );
}
#line 411 "work/legacy_function.c.aux"
static void a131(int arg1, double arg2)
{
#line 415 "work/legacy_function.c.aux"
  ldv_a131 ( arg1 , arg2 );
}
#line 419 "work/legacy_function.c.aux"
static void a132(int arg1, double arg2)
{
#line 423 "work/legacy_function.c.aux"
  ldv_a132 ( arg1 , arg2 );
}
#line 427 "work/legacy_function.c.aux"
static void a133(int *const *volatile *(*const *volatile *arg1)[10U][20U][30U], int *const *volatile *(*const *const volatile *(*arg2)[20U][30U])(void))
{
#line 431 "work/legacy_function.c.aux"
  ldv_a133 ( arg1 , arg2 );
}
#line 435 "work/legacy_function.c.aux"
static void a134(int *const *volatile *(*const *volatile *arg1)[10U][20U][30U], int *const *volatile *(*const *const volatile *(*arg2)[20U][30U])(void))
{
#line 439 "work/legacy_function.c.aux"
  ldv_a134 ( arg1 , arg2 );
}
#line 443 "work/legacy_function.c.aux"
static inline void a141(int arg1, double arg2)
{
#line 447 "work/legacy_function.c.aux"
  ldv_a141 ( arg1 , arg2 );
}
#line 451 "work/legacy_function.c.aux"
static void a151(int arg1, double arg2)
{
#line 455 "work/legacy_function.c.aux"
  ldv_a151 ( arg1 , arg2 );
}
#line 459 "work/legacy_function.c.aux"
static inline void a161(int arg1, double arg2)
{
#line 463 "work/legacy_function.c.aux"
  int ldv_a161();
#line 463 "work/legacy_function.c.aux"
  ldv_a161 ( arg1 , arg2 );
}
