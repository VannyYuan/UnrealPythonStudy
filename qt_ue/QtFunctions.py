# coding: utf-8

import unreal
import sys
sys.path.append('C:/Python27/Lib/site-packages')

from PySide import QtGui

def __QtAppTick__(delta_seconds):
    for window in opened_windows:
        window.eventTick(delta_seconds)

def __QtAppQuit__():
    unreal.unregister_slate_post_tick_callback(tick_handle)

def __QtWindowClosed__(window=None):
    if window in opened_windows:
        opened_windows.remove(window)

unreal_app = QtGui.QApplication.instance()
if not unreal_app:
    unreal_app = QtGui.QApplication(sys.argv)
    tick_handle = unreal.register_slate_post_tick_callback(__QtAppTick__)
    unreal_app.aboutToQuit.connect(__QtAppQuit__)
    existing_windows = {}
    opened_windows = []

def spawnQtWindow(desired_window_class=None):
    window = existing_windows.get(desired_window_class, None)
    if not window:
        window = desired_window_class()
        existing_windows[desired_window_class] = window
        window.aboutToClose = __QtWindowClosed__
    if window not in opened_windows:
        opened_windows.append(window)
    window.show()
    window.activateWindow()

# import QtFunctions
# reload(QtFunctions)
# import QtWindowOne
# import QtWindowTwo
# import QtWindowThree
# QtFunctions.spawnQtWindow(QtWindowOne.QtWindowOne)
# QtFunctions.spawnQtWindow(QtWindowTwo.QtWindowTwo)
# QtFunctions.spawnQtWindow(QtWindowThree.QtWindowThree)