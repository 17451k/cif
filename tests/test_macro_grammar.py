from test_aspect_grammar import TestAspectGrammar


# Macro grammar of pointcuts (docs/aoc.md, "Macros") and syntax of special
# directive parameters (docs/aoc.md, "Special directives"), exercised against
# tests/input/macros_grammar.c, which defines one macro of each shape:
# object-like, empty function-like, fixed-arity, variadic ("..." and named
# "args..."), and mixed fixed+variadic ("a, ..." and "a, rest...").
class TestMacroDefinitions(TestAspectGrammar):
    def check(self, pointcut, expected):
        matched = self.accept_macro('macro_def', 'query: ' + pointcut + ' ' + self.MACRO_BODY + '\n', cif_input='input/macros_grammar.c')
        self.assertEqual(matched, sorted(expected))

    def test_dollar_matches_object_like_only(self):
        self.check('define($)', ['OBJ'])

    def test_dollar_parens_matches_function_like_only(self):
        self.check('define($())', ['EMPTY'])

    def test_dollar_dotdot_matches_any_arity(self):
        self.check('define($(..))', ['EMPTY', 'ONE', 'TWO', 'THREE', 'VAR', 'NVAR', 'PRE', 'NPRE'])

    def test_one_named_param(self):
        self.check('define($(a))', ['ONE'])

    def test_one_wildcard_param_name(self):
        self.check('define($($))', ['ONE'])

    def test_two_named_params(self):
        self.check('define($(a, b))', ['TWO'])

    # ".." matches zero or more parameters at any single position.
    def test_dotdot_then_named_param(self):
        self.check('define($(.., b))', ['ONE', 'TWO', 'THREE'])

    def test_named_param_then_dotdot(self):
        self.check('define($(a, ..))', ['ONE', 'TWO', 'THREE', 'PRE', 'NPRE'])

    def test_dotdot_between_named_params(self):
        self.check('define($(a, .., c))', ['TWO', 'THREE'])

    # Consecutive ".." are treated as one.
    def test_consecutive_dotdot_merged(self):
        self.check('define($(.., ..))', ['EMPTY', 'ONE', 'TWO', 'THREE', 'VAR', 'NVAR', 'PRE', 'NPRE'])

    # "..." with no name matches both unnamed and named variadic macros.
    def test_ellipsis_only(self):
        self.check('define($(...))', ['VAR', 'NVAR'])

    # A name attached to "..." does not narrow matching either: it still
    # matches both the named and unnamed variadic macros.
    def test_named_ellipsis(self):
        self.check('define($(args...))', ['NVAR', 'VAR'])

    def test_one_param_then_ellipsis(self):
        self.check('define($(a, ...))', ['PRE', 'NPRE'])

    def test_one_param_then_named_ellipsis(self):
        self.check('define($(a, rest...))', ['NPRE', 'PRE'])

    # Parameter names are not significant for matching at all, only shape.
    def test_param_name_before_ellipsis_is_wildcard(self):
        self.check('define($(x, ...))', ['PRE', 'NPRE'])

    # "define(T$)" with no parameter list matches object-like macros only,
    # and no object-like macro name starts with "T".
    def test_prefix_wildcard_name_object_like(self):
        self.check('define(T$)', [])

    def test_prefix_wildcard_name_function_like(self):
        self.check('define(T$(..))', ['TWO', 'THREE'])

    # "$O$" means "name contains O somewhere", not "starts and ends with O".
    def test_wildcard_around_name(self):
        self.check('define($O$(..))', ['ONE', 'TWO'])


class TestMacroExpansions(TestAspectGrammar):
    def check(self, pointcut, expected):
        matched = self.accept_macro('macro_expand', 'query: ' + pointcut + ' ' + self.MACRO_BODY + '\n', cif_input='input/macros_grammar.c')
        self.assertEqual(matched, sorted(expected))

    def test_dollar_matches_object_like_expansions(self):
        self.check('expand($)', ['OBJ'])

    def test_two_named_params_expansion(self):
        self.check('expand($(a, b))', ['TWO'])

    def test_ellipsis_only_expansion(self):
        self.check('expand($(...))', ['VAR', 'NVAR'])

    def test_empty_expansion(self):
        self.check('expand(EMPTY())', ['EMPTY'])

    # ".." alone matches zero arguments too, unlike "x, ..".
    def test_dotdot_alone_matches_zero_args(self):
        self.check('expand($(..))', ['EMPTY', 'ONE', 'TWO', 'THREE', 'VAR', 'NVAR', 'PRE', 'NPRE'])


class TestDirectiveParameters(TestAspectGrammar):
    POINTCUT = 'expand($(..)) && infile("input/macros_grammar.c")'

    def run_body(self, body, cif_input='input/macros_grammar.c'):
        return self.accept('directive_params', 'query: ' + self.POINTCUT + ' { ' + body + ' }\n', cif_input=cif_input)

    def test_plain_string_no_extra_args(self):
        info = self.run_body('$fprintf<"work/info.txt","plain\\n">')
        self.assertEqual(info, sorted(['plain'] * 8))

    def test_percent_percent_escape(self):
        info = self.run_body('$fprintf<"work/info.txt","100%%\\n">')
        self.assertEqual(info, sorted(['100%'] * 8))

    def test_string_with_escaped_quote_comma_and_angle(self):
        info = self.run_body('$fprintf<"work/info.txt","a,b>c \\"q\\"\\n">')
        self.assertEqual(info, sorted(['a,b>c "q"'] * 8))

    def test_integer_parameter(self):
        info = self.run_body('$fprintf<"work/info.txt","%d\\n",42>')
        self.assertEqual(info, sorted(['42'] * 8))

    def test_two_string_parameters(self):
        info = self.run_body('$fprintf<"work/info.txt","%s %s\\n",$macro_name,$macro_name>')
        self.assertEqual(info, sorted(name + ' ' + name for name in ['EMPTY', 'ONE', 'TWO', 'THREE', 'VAR', 'NVAR', 'PRE', 'NPRE']))

    def test_directive_followed_by_semicolon(self):
        info = self.run_body('$fprintf<"work/info.txt","%s\\n",$macro_name>;')
        self.assertEqual(len(info), 8)

    def test_directive_without_semicolon(self):
        info = self.run_body('$fprintf<"work/info.txt","%s\\n",$macro_name>')
        self.assertEqual(len(info), 8)

    def test_expand_actual_args(self):
        matched = self.accept('directive_actual_args', 'query: expand(TWO(..)) { $fprintf<"work/info.txt","%s\\n",$actual_args> }\n', cif_input='input/macros_grammar.c')
        self.assertEqual(matched, ['actual_arg1=1, actual_arg2= 2'])

    def test_combined_macro_directives_on_expansion(self):
        matched = self.accept(
            'directive_combined',
            'query: expand(TWO(..)) { $fprintf<"work/info.txt","%s|%s|%s|%d\\n",$macro_name,$macro_signature,$actual_args,$line> }\n',
            cif_input='input/macros_grammar.c',
        )
        self.assertEqual(matched, ['TWO|TWO (a, b)|actual_arg1=1, actual_arg2= 2|4'])


class TestRejectedMacros(TestAspectGrammar):
    def check_reject(self, pointcut, message=None):
        self.reject('macro_reject', 'query: ' + pointcut + ' ' + self.MACRO_BODY + '\n', message or self.SYNTAX_ERROR)

    def test_space_separated_params(self):
        self.check_reject('define($(a b))')

    def test_trailing_comma(self):
        self.check_reject('define($(a,))')

    def test_leading_comma(self):
        self.check_reject('define($(,a))')

    def test_dotdot_followed_by_dotdot_no_comma(self):
        self.check_reject('define($(..)..)')

    def test_empty_parens_as_name(self):
        self.check_reject('define(())')

    def test_dollar_space_dollar(self):
        self.check_reject('define($ $)')

    def test_leading_digit_name(self):
        self.check_reject('define(1M)')

    def test_expand_extra_token(self):
        self.check_reject('expand($(a) x)')
