import utils


# The "new" advice creates a file that is specified in its pointcut.
class TestNewAdvice(utils.CIFTestCase):
    def test_new_creates_file(self):
        self.cif.run(cif_input='input/aspect_patterns.c', aspect='aspect/new_file.aspect',
                     cif_output='work/new_advice.c')
        self.compare(output='work/generated.c', expected='output/new_advice.c')
