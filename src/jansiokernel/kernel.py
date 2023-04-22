#!/usr/bin/env python
# *_* coding: utf-8 *_*

"""io kernel module"""

from ipykernel.kernelbase import Kernel
from pexpect import replwrap

notallowed = ["exit"]

iowrapper = replwrap.REPLWrapper("io", "Io> ", None)

class jansiokernel(Kernel):
    implementation = 'IPython'
    implementation_version = '8.12.0'
    language = 'io'
    language_version = '2017.09.06'
    language_info = {
        'name': 'io',
        'mimetype': 'application/io',
        'file_extension': '.io',
    }
    banner = "io"

    def do_execute(self, code, silent, store_history=True, user_expressions=None,
                   allow_stdin=False):
        if not silent:
            if code in notallowed:
                solution = f'"{code}" is not allowed in the io kernel'
            else:
                solution = iowrapper.run_command(code)
                if "==>" in solution[:5]:
                    solution = solution.replace("==>","")
            stream_content = {'name': 'stdout', 'text': solution}
            self.send_response(self.iopub_socket, 'stream', stream_content)

        return {'status': 'ok',
                'execution_count': self.execution_count,
                'payload': [],
                'user_expressions': {},
               }
