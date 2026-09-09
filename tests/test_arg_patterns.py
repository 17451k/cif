import pytest
import utils


# Test aspect patterns describing arguments of matched function calls.
class TestArgPatterns(utils.CIFTestCase):
    def test_arg_patterns(self):
        self.cif.run(cif_input='input/aspect_patterns.c', aspect='aspect/query_arg_patterns.aspect',
                     stage='instrumentation')
        self.compare(output='work/info.txt', expected='output/arg_patterns.txt')

    # $arg_size is an array size when an actual parameter is a pointer to a
    # one-dimensional array and -1 otherwise (#2954).
    def test_arg_size(self):
        self.cif.run(cif_input='input/aspect_patterns.c', aspect='aspect/query_arg_size.aspect',
                     stage='instrumentation')
        self.compare(output='work/info.txt', expected='output/arg_size.txt')

    # $arg_name is weaved just for actual parameters that are plain variables.
    # For all the others stub "NULL" is generated, like $arg_size and
    # $arg_value generate "-1" and "0" respectively.
    def test_arg_name_without_name(self):
        self.cif.run(cif_input='input/aspect_patterns.c', aspect='aspect/query_arg_name_of_array.aspect',
                     stage='instrumentation')
        self.compare(output='work/info.txt', expected='output/arg_name_without_name.txt')

    # $arg works in advices that are weaved in, but for source code queries
    # Aspectator does not collect formal parameters and fails with an internal
    # compiler error instead (#11295, still open).
    @pytest.mark.xfail(strict=True, reason='$arg does not work for source code queries (#11295)')
    def test_arg_in_query(self):
        self.cif.run(cif_input='input/aspect_patterns.c', aspect='aspect/query_arg.aspect',
                     stage='instrumentation')
