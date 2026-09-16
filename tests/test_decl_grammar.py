from test_aspect_grammar import TestAspectGrammar


# Tests of the declaration grammar used inside pointcuts: docs/aoc.md,
# "Declarations of functions, variables, and types" (~lines 668-800).
INPUT = 'input/decls.c'


class TestFunctionDeclarations(TestAspectGrammar):
    BODY = '{ $fprintf<"work/info.txt","%s\\n",$func_name> }'

    def check(self, pointcut, expected):
        matched = self.accept('func_decl', 'query: execution(' + pointcut + ') ' + self.BODY + '\n', cif_input=INPUT)
        self.assertEqual(matched, sorted(expected))

    ALL = ['fv', 'fi', 'sfi', 'ful', 'fva', 'ftwo', 'farr', 'ffp', 'fcp', 'fs', 'fnp', 'fmy', 'sinlf', 'main']

    def test_any_return_any_params(self):
        self.check('$ $(..)', self.ALL)

    # "void" as the only parameter also matches main() and fcp(), both declared "(void)".
    def test_void_params(self):
        self.check('$ $(void)', ['fv', 'fcp', 'main'])

    # "()" (empty parameter-type-list) is not representable in this grammar.
    def test_empty_params_is_syntax_error(self):
        self.reject('empty_params', 'query: execution($ $()) { }\n', self.SYNTAX_ERROR)

    # "int $(int)" has no storage-class specifier, so it does not match "static int sfi(int)".
    def test_int_return_int_param(self):
        self.check('int $(int)', ['fi'])

    def test_two_params_wildcard_second(self):
        self.check('$ $(int, $)', ['ftwo'])

    def test_two_params_char_ptr(self):
        self.check('$ $(int, char *)', ['ftwo'])

    def test_trailing_wildcard_param(self):
        self.check('$ $(.., char *)', ['ftwo'])

    # A trailing ".." after a fixed parameter also matches zero extra parameters.
    def test_leading_int_then_wildcard(self):
        self.check('$ $(int, ..)', ['fi', 'sfi', 'ftwo', 'sinlf'])

    def test_varargs_with_named_param(self):
        self.check('$ $(const char *, ...)', ['fva'])

    def test_static_any(self):
        self.check('static $ $(..)', ['sfi', 'sinlf'])

    def test_static_int_int_param(self):
        self.check('static int $(int)', ['sfi'])

    def test_inline_any(self):
        self.check('inline $ $(..)', ['sinlf'])

    # "unsigned" followed by a "$" type-specifier is rejected: "$" is only allowed either
    # alone or before all other type-specifiers, not after an explicit one.
    def test_unsigned_wildcard_after_is_syntax_error(self):
        self.reject('unsigned_dollar', 'query: execution(unsigned $ $(..)) { }\n', self.SYNTAX_ERROR)

    def test_wildcard_long(self):
        self.check('$ long $(..)', ['ful'])

    def test_char_ptr_return(self):
        self.check('char *$(..)', ['fcp'])

    def test_wildcard_ptr_return(self):
        self.check('$ *$(..)', ['fcp'])

    def test_array_param_wildcard_size(self):
        self.check('$ $(int[$])', ['farr'])

    def test_array_param_exact_size(self):
        self.check('$ $(int[3])', ['farr'])

    def test_function_pointer_param(self):
        self.check('$ $(int (*)(int))', ['ffp'])

    def test_struct_param(self):
        self.check('struct S $(..)', ['fs'])

    def test_struct_param_wildcard_return(self):
        self.check('$ $(struct S)', ['fs'])

    # "$" matches typedef names too.
    def test_wildcard_matches_typedef_name(self):
        self.check('$ $(myint)', ['fmy'])

    def test_typedef_name_matches_itself(self):
        self.check('myint $(..)', ['fmy'])

    def test_typedef_name_as_param(self):
        self.check('int $(myint)', [])

    def test_name_prefix_wildcard(self):
        self.check('$ f$(..)', ['fv', 'fi', 'ftwo', 'farr', 'ffp', 'fcp', 'fs', 'fnp', 'fmy', 'ful', 'fva'])

    def test_param_with_name(self):
        self.check('$ $(int a)', ['fi', 'sfi', 'sinlf'])


class TestVariableDeclarations(TestAspectGrammar):
    BODY = '{ $fprintf<"work/info.txt","%s\\n",$var_name> }'

    def check(self, pointcut, expected):
        matched = self.accept('var_decl', 'query: use_var(' + pointcut + ') ' + self.BODY + '\n', cif_input=INPUT)
        self.assertEqual(sorted(set(matched)), sorted(expected))

    def test_any_any(self):
        self.check('$ $', ['arr2d', 'arr3', 'arr5', 'bo', 'ccp', 'ci', 'cp', 'cpc', 'd', 'ei', 'f', 'fp', 'fpv',
                            'ge', 'gi', 'gs', 'gu', 'll', 'mi', 'r', 'si', 'sv', 'ul', 'vi'])

    # "extern" is not recorded for source declarations, so "int" matches "extern int ei" too.
    def test_int_any(self):
        self.check('int $', ['ei', 'gi', 'r'])

    def test_static_int(self):
        self.check('static int $', ['si'])

    def test_const_int(self):
        self.check('const int $', ['ci'])

    def test_volatile_any(self):
        self.check('volatile $ $', ['vi'])

    def test_wildcard_ptr(self):
        self.check('$ *$', ['cp', 'ccp'])

    def test_char_ptr(self):
        self.check('char *$', ['cp'])

    def test_const_char_ptr(self):
        self.check('const char *$', ['ccp'])

    def test_char_ptr_const(self):
        self.check('char *const $', ['cpc'])

    def test_array_wildcard_size(self):
        self.check('$ $[$]', ['arr2d', 'arr3', 'arr5'])

    def test_array_size_3(self):
        self.check('int $[3]', ['arr3'])

    def test_array_size_5(self):
        self.check('int $[5]', ['arr5'])

    def test_array2d_wildcard_size(self):
        self.check('int $[$][$]', ['arr2d'])

    def test_array2d_exact_size(self):
        self.check('int $[2][3]', ['arr2d'])

    def test_func_pointer_int_param(self):
        self.check('$ (*$)(int)', ['fp'])

    def test_func_pointer_void_param(self):
        self.check('$ (*$)(void)', ['fpv'])

    def test_struct_s(self):
        self.check('struct S $', ['gs', 'sv'])

    def test_struct_wildcard(self):
        self.check('struct $ $', ['gs', 'sv'])

    def test_union_u(self):
        self.check('union U $', ['gu'])

    def test_enum_e(self):
        self.check('enum E $', ['ge'])

    def test_typedef_name(self):
        self.check('myint $', ['mi'])

    def test_unsigned_long(self):
        self.check('unsigned long $', ['ul'])

    def test_long_long(self):
        self.check('long long $', ['ll'])

    def test_bool(self):
        self.check('_Bool $', ['bo'])


class TestTypeDeclarations(TestAspectGrammar):
    BODY = '{ $fprintf<"work/info.txt","%s\\n",$signature> }'

    def check(self, pointcut, expected):
        matched = self.accept('type_decl', 'query: introduce(' + pointcut + ') ' + self.BODY + '\n', cif_input=INPUT)
        self.assertEqual(matched, sorted(expected))

    def test_struct_s(self):
        self.check('struct S', ['struct S { int a; };'])

    def test_struct_wildcard(self):
        self.check('struct $', ['struct S { int a; };'])

    def test_union_wildcard(self):
        self.check('union $', ['union U { int b; };'])

    def test_enum_wildcard(self):
        self.check('enum $', ['enum E { E0 = 0 };'])

    # "||" combines pointcuts, not declarations, so it must be outside introduce(...).
    def test_struct_or_union_or_enum(self):
        matched = self.accept(
            'type_decl_or',
            'query: introduce(struct $) || introduce(union $) || introduce(enum $) ' + self.BODY + '\n',
            cif_input=INPUT)
        self.assertEqual(matched, sorted(['struct S { int a; };', 'union U { int b; };', 'enum E { E0 = 0 };']))

    # docs: "for a structure, union, or enumeration declaration a corresponding type specifier
    # should be specified ... struct $, union $ and enum $" implies bare "$" matches none of
    # them, but observed it matches all three composite type declarations.
    def test_bare_wildcard(self):
        self.check('$', ['struct S { int a; };', 'union U { int b; };', 'enum E { E0 = 0 };'])

    # docs (line 862 example): "$ $" ("two '$' symbols that match variables or functions")
    # is contrasted with the composite-type forms, implying it should not match a composite
    # type declaration -- but it does match the typedef "typedef int myint;", not nothing.
    def test_two_wildcards_match_no_type(self):
        self.check('$ $', ['typedef int myint;'])


class TestRejectedDeclarations(TestAspectGrammar):
    def test_two_wildcard_type_specifiers(self):
        self.reject('two_dollars', 'query: execution($ $ $(..)) { }\n', self.SYNTAX_ERROR)

    # A query on "get" prints like any other variable query. Only assignments whose
    # right operand is a plain variable are "get" join points.
    def test_get_query_prints_var_name(self):
        matched = self.accept('get_query', 'query: get(int $) { $fprintf<"work/info.txt","%s\\n",$var_name> }\n', cif_input=INPUT)
        self.assertEqual(sorted(set(matched)), ['a', 'r'])

    # Repeated type specifiers are not rejected; "int int $" matches as "int $" does.
    def test_two_int_type_specifiers(self):
        matched = self.accept('two_ints', 'query: use_var(int int $) { $fprintf<"work/info.txt","%s\\n",$var_name> }\n', cif_input=INPUT)
        self.assertEqual(sorted(set(matched)), ['ei', 'gi', 'r'])

    def test_varargs_in_middle(self):
        self.reject('varargs_middle', 'query: execution($ $(int, ..., int)) { }\n',
                     "Used '...' not at the end of parameter list")

    # "[]" (no size and no "$") is accepted by the parser, unlike a genuine syntax error.
    def test_empty_array_brackets_is_accepted(self):
        self.accept('empty_brackets', 'query: get($ $[]) { }\n', cif_input=INPUT)

    def test_varargs_as_return_type(self):
        self.reject('varargs_return', 'query: execution(... $(..)) { }\n', self.SYNTAX_ERROR)

    def test_empty_declaration(self):
        self.reject('empty_decl', 'query: execution() { }\n', self.SYNTAX_ERROR)

    def test_missing_declarator_name(self):
        self.reject('missing_name', 'query: execution(int (..)) { }\n', self.SYNTAX_ERROR)
