# coding: utf-8

import unreal

def tryCast():
    # ! this run crash use python
    # if unreal.Actor.cast(unreal.load_asset('/Game/MyAsset/Textures/dear')):   
    if unreal.Texture2D.cast(unreal.load_asset('/Game/MyAsset/Textures/dear')):
        print 'Cast Succeeded'
    else:
        print 'Cast Failed'

def castObject():
    # ! this will not crash user C++
    if cast(unreal.load_asset('/Game/MyAsset/Textures/dear'), unreal.Actor):
        print 'Cast Succeeded'
    else:
        print 'Cast Failed'

def cast(object_to_cast, object_class):
    try:
        return object_class.cast(object_to_cast)
    except:
        return None

# import PythonHelpers_2 as ph
# reload(ph)
# ph.castObject()