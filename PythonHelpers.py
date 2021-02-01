# coding: utf-8

import unreal

def getAllProperties(object_class):
    return unreal.CppLib.get_all_properties(object_class)

def printAllProperties():
    obj = unreal.Actor()
    object_class = obj.get_class()
    for x in getAllProperties(object_class):
        name = x
        while len(name) < 50:
            name = ' ' + name
        print name + ':' + str(obj.get_editor_property(x))


# import PythonHelpers as ph
# reload(ph)
# ph.printAllProperties()