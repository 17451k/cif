import os

import utils


# "info" is a deprecated alias for "query". Keep checking that it is still
# accepted and that it does not diverge from "query".
class TestInfoAdvice(utils.CIFTestCase):
    def test_info_is_alias_for_query(self):
        self.cif.run(cif_input='input/aspect_patterns.c', aspect='aspect/info_call.aspect',
                     stage='instrumentation')
        os.rename('work/info.txt', 'work/from_info.txt')

        self.cif.run(cif_input='input/aspect_patterns.c', aspect='aspect/query_call_for_info.aspect',
                     stage='instrumentation')

        self.compare(output='work/from_info.txt', expected='output/info_advice.txt')
        self.compare(output='work/info.txt', expected='output/info_advice.txt')
