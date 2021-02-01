# coding: utf-8

import unreal
import os
import sys
sys.path.append('C:/Python27/Lib/site-packages')

from PySide.QtGui import *
from PySide import QtUiTools

WINDOW_NAME = 'Qt Window Three'
UI_FILE_FULLNAME = os.path.join(os.path.dirname(__file__), 'ui', 'window_scale.ui').replace('\\','/')


class QtWindowThree(QWidget):
    def __init__(self, parent=None):
        super(QtWindowThree, self).__init__(parent)
        self.aboutToClose = None
        self.widget = QtUiTools.QUiLoader().load(UI_FILE_FULLNAME)
        self.widget.setParent(self)
        self.setWindowTitle(WINDOW_NAME)
        self.setGeometry(100, 100, self.widget.width(),self.widget.height())
        self.initialiseWidget()

    def clossEvent(self, event):  
        if self.aboutToClose:
            self.aboutToClose(self)
        event.accept()

    def eventTick(self, delta_seconds):
        self.myTick(delta_seconds)

    def initialiseWidget(self):
        self.time_while_this_window_is_open = 0.0
        self.random_actor = None
        self.random_actor_is_going_up = True
        self.widget.pushButton.clicked.connect(self.scaleRandomActorInScene)

    def scaleRandomActorInScene(self):
        import random
        import WorldFunctions_2
        all_actors = WorldFunctions_2.sortActors(use_selection=False, actor_class=unreal.StaticMeshActor, actor_tag=None)
        rand = random.randrange(0, len(all_actors))
        self.random_actor = all_actors[rand]

    def myTick(self, delta_seconds):
        self.time_while_this_window_is_open += delta_seconds
        self.widget.label.setText("{} Seconds".format(self.time_while_this_window_is_open))
        if self.random_actor:
            actor_scale = self.random_actor.get_actor_scale3d()
            speed = 3.0 * delta_seconds
            if self.random_actor_is_going_up:
                if actor_scale.z > 2.0:
                    self.random_actor_is_going_up = False
            else:
                speed = -speed
                if actor_scale.z < 0.5:
                    self.random_actor_is_going_up = True
            self.random_actor.set_actor_scale3d(unreal.Vector(actor_scale.x + speed, actor_scale.y + speed, actor_scale.z + speed))