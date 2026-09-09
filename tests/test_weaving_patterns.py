import utils


# Test aspect patterns that are available just while weaving, so they are
# checked in woven in files rather than in query outputs.
class TestWeavingPatterns(utils.CIFTestCase):
    # $res and $ret_type are identifiers of a variable holding a function
    # return value and of a typedef for its type.
    def test_res_and_ret_type(self):
        self.cif.run(cif_input='input/aspect_patterns.c', aspect='aspect/weave_res_ret_type.aspect',
                     cif_output='work/res_ret_type.c')
        self.compare(output='work/res_ret_type.c', expected='output/res_ret_type.c')

    # $aspect_func_name is a name of an auxiliary function created for a
    # matched function definition.
    def test_aspect_func_name(self):
        self.cif.run(cif_input='input/aspect_patterns.c', aspect='aspect/weave_aspect_func_name.aspect',
                     cif_output='work/aspect_func_name.c')
        self.compare(output='work/info.txt', expected='output/aspect_func_name.txt')
