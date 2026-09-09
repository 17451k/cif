import pytest
import utils


# Test pointcuts matching accesses to variables of a particular storage.
class TestVarPointcuts(utils.CIFTestCase):
    def test_set_global(self):
        self.cif.run(cif_input='input/var_pointcuts.c', aspect='aspect/weave_set_global.aspect',
                     cif_output='work/set_global.c')
        self.compare(output='work/set_global.c', expected='output/set_global.c')

    def test_get_global(self):
        self.cif.run(cif_input='input/var_pointcuts.c', aspect='aspect/weave_get_global.aspect',
                     cif_output='work/get_global.c')
        self.compare(output='work/get_global.c', expected='output/get_global.c')

    def test_set_local(self):
        self.cif.run(cif_input='input/var_pointcuts.c', aspect='aspect/weave_set_local.aspect',
                     cif_output='work/set_local.c')
        self.compare(output='work/set_local.c', expected='output/set_local.c')

    def test_get_local(self):
        self.cif.run(cif_input='input/var_pointcuts.c', aspect='aspect/weave_get_local.aspect',
                     cif_output='work/get_local.c')
        self.compare(output='work/get_local.c', expected='output/get_local.c')

    def test_init_local(self):
        self.cif.run(cif_input='input/var_pointcuts.c', aspect='aspect/query_init_local.aspect',
                     stage='instrumentation')
        self.compare(output='work/info.txt', expected='output/init_local.txt')


# "infunc" should restrict join points to those within a given function, but
# its matching code in libcpp/ldv-cpp-pointcut-matcher.c is commented out with
# a "TODO: Fix me someday", so it silently matches nothing at all.
class TestInfunc(utils.CIFTestCase):
    @pytest.mark.xfail(strict=True, reason='infunc is not implemented, it never matches')
    def test_infunc_restricts_to_function(self):
        self.cif.run(cif_input='input/infunc.c', aspect='aspect/query_infunc.aspect',
                     stage='instrumentation')
        self.compare(output='work/info.txt', expected='output/infunc.txt')
