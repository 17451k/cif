import utils


# Test aspect patterns describing matched variables.
class TestVarPatterns(utils.CIFTestCase):
    # $var_type_name is provided just when an aspect names a type rather than
    # matches it with a wildcard.
    def test_var_type_name(self):
        self.cif.run(cif_input='input/aspect_patterns.c', aspect='aspect/query_var_type_name.aspect',
                     stage='instrumentation')
        self.compare(output='work/info.txt', expected='output/var_type_name.txt')
