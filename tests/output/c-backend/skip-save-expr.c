#define LDV_MIN(X,Y) ((X) < (Y) ? (X) : (Y))
#define LDV_MAX(X,Y) ((X) > (Y) ? (X) : (Y))
#define LDV_ABS(X) ((X) < 0 ? -(X) : (X))
#define LDV_LROTATE(X,Y) (((X) << (Y)) | ((X) >> (__CHAR_BIT__ * sizeof (X) - Y)))
#define LDV_RROTATE(X,Y) (((X) >> (Y)) | ((X) << (__CHAR_BIT__ * sizeof (X) - Y)))
#line 1 "input/c-backend/skip-save-expr.c"
void func(long unsigned int arg)
{
  ( void ) ( long unsigned int ) ( __builtin_constant_p ( arg ) == 0 ? -1 : 1 );
}
