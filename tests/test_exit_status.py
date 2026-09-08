import os
import signal
import stat
import subprocess

import utils


# Test how CIF reports aspectator failures and how it cleans up after them.
class TestExitStatus(utils.CIFTestCase):
    # Replace aspectator with a shell script that behaves in a given way. This
    # keeps the failure cases independent of a real aspectator build.
    def make_stub_aspectator(self, name, body):
        stub = os.path.join(utils.WORK_DIR, name)

        with open(stub, 'w', encoding='utf8') as fp:
            fp.write('#!/bin/sh\n' + body + '\n')

        os.chmod(stub, os.stat(stub).st_mode | stat.S_IEXEC)

        return stub

    def run_cif(self, cif_output, aspectator=None, compilation_opts=None, keep=False, stage='compilation'):
        cif = os.environ.get('CIF', '../inst/bin/cif')

        cmd = [cif,
               '--in', 'input/stmts/for.c',
               '--aspect', 'aspect/func-calls.aspect',
               '--back-end', 'src',
               '--stage', stage,
               '--out', cif_output,
               '--debug', 'ALL']

        if aspectator:
            cmd.extend(['--aspectator', aspectator])

        if compilation_opts:
            cmd.extend(['--compilation-opts', compilation_opts])

        if keep:
            cmd.append('--keep')

        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = proc.communicate()

        self.log = (stdout.decode('utf-8') + stderr.decode('utf-8')).strip()

        print('\nCMD: {!r}'.format(' '.join(cmd)))
        print('LOG:', self.log, '\n')

        return proc.returncode

    # Files that CIF creates and registers for removal. Note that aspectator
    # produces some files of its own, e.g. *.aux, that CIF doesn't know about
    # and thus never removes.
    def aux_files(self, cif_output):
        return [cif_output + '.func-calls.aspect.i',
                cif_output + '.func-calls.aspect.i.bak',
                cif_output + '.prepared',
                cif_output + '.macroinstrumented',
                cif_output + '.instrumented']

    # An aspectator killed by a signal used to be reported through
    # WEXITSTATUS(), which is 0 in that case, so CIF exited successfully even
    # though nothing was produced.
    def test_aspectator_killed_by_signal(self):
        stub = self.make_stub_aspectator('segv-aspectator', 'kill -SEGV $$')
        status = self.run_cif(cif_output=utils.WORK_DIR + '/signal.c', aspectator=stub)

        self.assertEqual(status, 128 + int(signal.SIGSEGV))
        self.assertIn('terminated by signal', self.log)
        self.assertFalse(os.path.exists(utils.WORK_DIR + '/signal.c'))

    # A normally exited aspectator should pass its exit code through.
    def test_aspectator_exit_code_is_passed_through(self):
        stub = self.make_stub_aspectator('failing-aspectator', 'exit 3')
        status = self.run_cif(cif_output=utils.WORK_DIR + '/failure.c', aspectator=stub)

        self.assertEqual(status, 3)
        self.assertIn('exit code 3', self.log)

    def test_intermediate_files_are_removed(self):
        out = utils.WORK_DIR + '/removed.c'
        status = self.run_cif(cif_output=out)

        self.assertEqual(status, 0)
        self.assertTrue(os.path.exists(out))

        for aux_file in self.aux_files(out):
            self.assertFalse(os.path.exists(aux_file), aux_file + ' was not removed')

    def test_intermediate_files_are_kept(self):
        out = utils.WORK_DIR + '/kept.c'
        status = self.run_cif(cif_output=out, keep=True)

        self.assertEqual(status, 0)

        for aux_file in self.aux_files(out):
            self.assertTrue(os.path.exists(aux_file), aux_file + ' was removed')

    # Intermediate files obtained thus far are removed when a stage fails. Make
    # the last stage fail so that all the previous ones leave their files.
    def test_intermediate_files_are_removed_on_failure(self):
        out = utils.WORK_DIR + '/failed.c'
        status = self.run_cif(cif_output=out, compilation_opts='-fnonexistent-option-xyz')

        self.assertNotEqual(status, 0)

        for aux_file in self.aux_files(out):
            self.assertFalse(os.path.exists(aux_file), aux_file + ' was not removed')

    # Output of the last stage to be performed is not an intermediate file even
    # though the very same file is one when further stages are performed too.
    def test_output_of_requested_stage_is_not_removed(self):
        out = utils.WORK_DIR + '/staged.c'
        status = self.run_cif(cif_output=out, stage='instrumentation')

        self.assertEqual(status, 0)
        self.assertTrue(os.path.exists(out + '.instrumented'))

        for aux_file in self.aux_files(out):
            if aux_file.endswith('.instrumented'):
                continue

            self.assertFalse(os.path.exists(aux_file), aux_file + ' was not removed')
