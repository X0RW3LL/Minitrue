#!/usr/bin/env python3

import os, sys
cwd = os.getcwd()
sys.path.insert(0, "/home/x0rw3ll/Minitrue/packages")
from prompt_toolkit.completion import WordCompleter as w_com

payloads = w_com([
    'windows/shell_reverse_tcp',
    'windows/x64/shell_reverse_tcp',
    'windows/meterpreter/reverse_tcp',
    'windows/x64/meterpreter/reverse_tcp'
    ])

modes = w_com([
        'VBA Macro',
        'OLE (Embedded Icon)'
        ])

ports = w_com([
        '80',
        '443',
        '445',
        '21',
        '22',
        '25',
        '53',
        '110',
        '143'
        ])

encoders = w_com([
        'None',
        'x86/shikata_ga_nai',
        'x86/shikata_ga_nai -i 3',
        'x86/shikata_ga_nai -i 5',
        'x86/shikata_ga_nai -i 7',
        'x86/shikata_ga_nai -i 9'
        ])

srv_ports = w_com([
        'No',
        'Yes - Port 80',
        'Yes - Port 443',
        'Yes - Port 445',
        'Yes - Port 8000',
        'Yes - Port 8080',
        ])

filenames = w_com([
        'abstract',
        'bonus',
        'business_plan',
        'cover_letter',
        'credentials',
        'draft',
        'employees',
        'financial_report',
        'report',
        'research',
        'resume',
        'statistics',
        'urgent_patch',
        'users'
        ])

