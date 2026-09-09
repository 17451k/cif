import utils


# Test aspect patterns describing a join point context and signatures.
class TestContextPatterns(utils.CIFTestCase):
    def test_context_patterns(self):
        self.cif.run(cif_input='input/aspect_patterns.c', aspect='aspect/query_context_patterns.aspect',
                     stage='instrumentation')
        self.compare(output='work/info.txt', expected='output/context_patterns.txt')

    def test_func_signature(self):
        self.cif.run(cif_input='input/aspect_patterns.c', aspect='aspect/query_func_signature.aspect',
                     stage='instrumentation')
        self.compare(output='work/info.txt', expected='output/func_signature.txt')
