# coding: utf-8

import unreal

def executeConsoleCommand():
    console_commands = ['r.ScreenPercentage 0.1', 'r.Color.Max 6', 'stat fps', 'stat unit']
    for x in console_commands:
        unreal.CppLib.execute_console_command(x)

import EditorFunction_2 as ef
reload(ef)
ef.executeConsoleCommand()
