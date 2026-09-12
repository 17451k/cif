import os

import utils


# Tests of the aspect grammar itself: composition of pointcuts, advice and
# aspect structure, and what the parser must reject. Aspects are small and
# numerous, so they are written to the work directory instead of tests/aspect.
class TestAspectGrammar(utils.CIFTestCase):
    INFO = 'work/info.txt'

    def write_aspect(self, name, text):
        path = os.path.join(utils.WORK_DIR, name + '.aspect')

        with open(path, 'w', encoding='utf8') as fp:
            fp.write(text)

        return path

    def read_info(self):
        if not os.path.exists(self.INFO):
            return []

        with open(self.INFO, encoding='utf8') as fp:
            return sorted(line.strip() for line in fp if line.strip())

    def accept(self, name, text, cif_input='input/simple.c'):
        self.cif.run(cif_input=cif_input, aspect=self.write_aspect(name, text), stage='instrumentation')
        return self.read_info()

    def reject(self, name, text, message):
        self.cif.run(cif_input='input/simple.c', aspect=self.write_aspect(name, text), stage='instrumentation', expected_fail=True)
        self.assertIn(message, self.cif.log)


# Join points of input/simple.c reachable through macro pointcuts: definitions
# of SOMETHING, CONST and ZERO(x), and expansions of CONST and ZERO. Every
# composite pointcut is put into the only advice of its aspect, since only
# the first matching advice is applied to a join point.
class TestPointcutComposition(TestAspectGrammar):
    PRELUDE = '''
pointcut SOMETHING: define(SOMETHING)
pointcut FUNC_LIKE: define($(..))
pointcut ANY_DEF: define($) || FUNC_LIKE
pointcut ANY_EXPAND: expand($) || expand($(..))
'''

    BODY = '{ $fprintf<"work/info.txt","%s\\n",$macro_name> }'

    def check(self, pointcut, expected):
        matched = self.accept('composition', self.PRELUDE + 'query: ' + pointcut + ' ' + self.BODY + '\n')
        self.assertEqual(matched, sorted(expected))

    def test_named_pointcut(self):
        self.check('SOMETHING', ['SOMETHING'])

    def test_named_pointcut_of_named_pointcuts(self):
        self.check('ANY_DEF', ['SOMETHING', 'CONST', 'ZERO'])

    # "$" alone matches object-like macros only, "$(..)" function-like ones.
    def test_object_like_wildcard(self):
        self.check('define($)', ['SOMETHING', 'CONST'])

    def test_function_like_wildcard(self):
        self.check('FUNC_LIKE', ['ZERO'])

    def test_wildcard_inside_identifier(self):
        self.check('define(SOME$) || define($ST)', ['SOMETHING', 'CONST'])

    def test_or(self):
        self.check('ANY_DEF || ANY_EXPAND', ['SOMETHING', 'CONST', 'ZERO', 'CONST', 'ZERO'])

    def test_and_not(self):
        self.check('ANY_DEF && !SOMETHING', ['CONST', 'ZERO'])

    def test_not_and(self):
        self.check('!SOMETHING && ANY_DEF', ['CONST', 'ZERO'])

    def test_not_parenthesized_or(self):
        self.check('!(SOMETHING || FUNC_LIKE) && ANY_DEF', ['CONST'])

    # A negation alone matches nothing since there is nothing to weave.
    def test_not_alone(self):
        self.check('!SOMETHING', [])

    def test_double_not(self):
        self.check('!!SOMETHING', [])

    def test_and_not_same_wildcard(self):
        self.check('ANY_DEF && !ANY_DEF', [])

    def test_and_not_matched_by_name_only(self):
        self.check('FUNC_LIKE && !define(ZERO(a, b))', ['ZERO'])

    def test_or_not(self):
        self.check('SOMETHING || !SOMETHING', ['SOMETHING'])

    def test_expand_and_not(self):
        self.check('ANY_EXPAND && !expand(CONST)', ['ZERO'])

    def test_nested_parentheses(self):
        self.check('(((SOMETHING)))', ['SOMETHING'])

    # "!" binds tighter than "&&", which binds tighter than "||".
    def test_precedence(self):
        self.check('ANY_DEF && !SOMETHING || ANY_EXPAND', ['CONST', 'ZERO', 'CONST', 'ZERO'])

    def test_precedence_overridden_by_parentheses(self):
        self.check('ANY_DEF && (!SOMETHING || ANY_EXPAND)', ['CONST', 'ZERO'])

    def test_infile(self):
        self.check('ANY_EXPAND && infile("input/simple.c")', ['CONST', 'ZERO'])

    def test_not_infile(self):
        self.check('ANY_EXPAND && !infile("input/simple.c")', [])

    def test_pointcut_on_several_lines(self):
        self.check('\n  SOMETHING\n  ||\n  FUNC_LIKE\n', ['SOMETHING', 'ZERO'])

    def test_info_is_alias_for_query(self):
        matched = self.accept('info', self.PRELUDE + 'info: SOMETHING ' + self.BODY + '\n')
        self.assertEqual(matched, ['SOMETHING'])


# The same for function join points, which are matched by a different matcher.
class TestFunctionPointcutComposition(TestAspectGrammar):
    BODY = '{ $fprintf<"work/info.txt","%s\\n",$func_name> }'

    def check(self, pointcut, expected):
        matched = self.accept('func_composition', 'query: ' + pointcut + ' ' + self.BODY + '\n')
        self.assertEqual(matched, sorted(expected))

    def test_execution_and_not(self):
        self.check('execution($ $(..)) && !execution($ main(..))', ['func'])

    def test_execution_and_not_matched_by_name_only(self):
        self.check('execution($ $(..)) && !execution($ func(void))', ['func', 'main'])

    def test_not_and_execution(self):
        self.check('!execution($ main(..)) && execution($ $(..))', ['func'])

    def test_not_alone(self):
        self.check('!execution($ main(..))', [])

    def test_call_and_not_execution(self):
        self.check('call($ func(..)) && !execution($ func(..))', ['func'])


class TestAcceptedSyntax(TestAspectGrammar):
    def test_empty_aspect(self):
        self.accept('empty', '')

    def test_only_named_pointcuts(self):
        self.accept('only_pointcuts', 'pointcut p: call($ func(..))\npointcut q: p\n')

    def test_empty_body(self):
        self.accept('empty_body', 'before: call($ func(..)) {}\n')

    def test_nested_braces_in_body(self):
        self.accept('nested_braces', 'before: call($ func(..)) { if (1) { int y; { y = 2; } } }\n')

    def test_comments(self):
        self.accept('comments', '''
/* block */ pointcut p: call($ /* inside a declaration */ func(..)) // line
// before an advice
before: /* between tokens */ p // after a pointcut
{ /* } inside a comment */ }
''')

    def test_line_directive(self):
        self.accept('line_directive', '# 5 "renamed.aspect"\nbefore: call($ func(..)) { }\n')

    def test_line_directive_with_flags(self):
        self.accept('line_directive_flags', '# 1 "renamed.aspect" 1 3\nbefore: call($ func(..)) { }\n')

    # Keywords of AOC are recognized only in their own positions.
    def test_keyword_as_function_name(self):
        self.accept('keyword_as_func', 'before: call($ before(..)) { }\nbefore: call($ query(..)) { }\n')

    def test_keyword_as_pointcut_name(self):
        self.accept('keyword_as_pointcut', 'pointcut call: call($ func(..))\nbefore: call { }\n')

    def test_all_advice_kinds(self):
        self.accept('advice_kinds', '''
pointcut p: call($ func(..))
before: p { }
after: p { }
around: p { $proceed; }
query: p { $fprintf<"work/info.txt","%s\\n",$func_name> }
new: file("work/new.c") { int created; }
''')
        self.assertTrue(os.path.exists('work/new.c'))

    def test_braces_in_string_literal(self):
        self.accept('string_brace', 'before: call($ func(..)) { char *s = "}{\\"{"; }\n')

    def test_braces_in_char_literal(self):
        self.accept('char_brace', "before: call($ func(..)) { char c = '}'; char q = '\\''; }\n")

    def test_quote_in_comment_in_body(self):
        self.accept('quote_in_comment', 'before: call($ func(..)) { /* don\'t " */ int y; // "\n }\n')


class TestRejectedSyntax(TestAspectGrammar):
    SYNTAX_ERROR = 'aspect file processed has incorrect syntax'

    def test_undefined_named_pointcut(self):
        self.reject('undefined', 'before: undefined_pc { }\n', 'undefined pointcut with name "undefined_pc"')

    def test_self_referencing_named_pointcut(self):
        self.reject('self_ref', 'pointcut p: p\nbefore: p { }\n', 'undefined pointcut with name "p"')

    def test_wildcard_in_named_pointcut_name(self):
        self.reject('dollar_name', 'pointcut $p: call($ func(..))\nbefore: $p { }\n', "'$' wildcard was used in pointcut name")

    def test_named_pointcuts_with_same_name(self):
        self.reject('same_name', 'pointcut p: call($ func(..))\npointcut p: call($ main(..))\nbefore: p { }\n', 'duplicate pointcut name "p"')

    def test_missing_body(self):
        self.reject('no_body', 'before: call($ func(..))\n', self.SYNTAX_ERROR)

    def test_missing_colon(self):
        self.reject('no_colon', 'before call($ func(..)) { }\n', self.SYNTAX_ERROR)

    def test_missing_pointcut(self):
        self.reject('no_pointcut', 'before: { }\n', self.SYNTAX_ERROR)

    def test_unknown_advice_kind(self):
        self.reject('unknown_kind', 'instead: call($ func(..)) { }\n', 'incorrect advice declaration kind "instead"')

    def test_unbalanced_parenthesis(self):
        self.reject('unbalanced', 'before: call($ func(..) { }\n', self.SYNTAX_ERROR)

    def test_binary_operator_without_operand(self):
        self.reject('no_operand', 'before: call($ func(..)) || { }\n', self.SYNTAX_ERROR)

    def test_stray_token_after_advice(self):
        self.reject('stray', 'before: call($ func(..)) { } ;\n', self.SYNTAX_ERROR)

    def test_unterminated_body(self):
        self.reject('unterminated_body', 'before: call($ func(..)) {\n', "End of file is reached but advice body")

    def test_unterminated_file_name(self):
        self.reject('unterminated_file', 'before: infile("foo { }\n', "file path isn't terminated with quote")

    def test_non_ascii_identifier(self):
        self.reject('non_ascii', 'before: call($ fúnc(..)) { }\n', self.SYNTAX_ERROR)

    def test_unknown_special_directive(self):
        self.reject('unknown_directive', 'before: call($ func(..)) { $nonexistent; }\n', 'aspect pattern "nonexistent" wasn\'t weaved')

    def test_argument_number_zero(self):
        self.reject('arg_zero', 'before: call($ func(..)) { $arg0; }\n', 'required parameter has number "0"')

    def test_argument_number_too_big(self):
        self.reject('arg_big', 'before: call($ func(..)) { $arg99; }\n', 'required parameter has number "99"')

    def test_env_without_parameter(self):
        self.reject('env', 'query: call($ func(..)) { $env }\n', 'should have the only string parameter')

    def test_unterminated_directive_parameters(self):
        self.reject('unterminated_params', 'query: call($ func(..)) { $fprintf<"work/info.txt","%s\\n",$func_name }\n', 'aspect pattern parameters list has incorrect format')

    def test_new_with_composite_pointcut(self):
        self.reject('new_composite', 'new: file("work/a.c") || file("work/b.c") { int x; }\n', 'pointcut of "new" advice should be "file" primitive pointcut')

    def test_new_with_non_file_pointcut(self):
        self.reject('new_nonfile', 'new: call($ func(..)) { int x; }\n', 'pointcut of "new" advice should be "file" primitive pointcut')

    def test_unterminated_string_in_body(self):
        self.reject('unterminated_body_string', 'before: call($ func(..)) { char *s = "}; }\n', "End of file is reached but advice body")
