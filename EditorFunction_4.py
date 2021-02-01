# coding: utf-8
import unreal
import random

# return: int : The index of the active viewport
def getActiveViewportIndex():
    return unreal.CppLib.get_active_viewport_index()

# viewport_index: int : The index of the viewport you want to affect
# location: obj unreal.Vector : The viewport location
# rotation: obj unreal.Rotator : The viewport rotation
def setViewportLocationAndRotation(viewport_index=1, location=unreal.Vector(), rotation=unreal.Rotator()):
    unreal.CppLib.set_viewport_location_and_rotation(viewport_index, location, rotation)

# viewport_index: int : The index of the viewport you want to affect
# actor: obj unreal.Actor : The actor you want to snap to
def snapViewportToActor(viewport_index=1, actor=None):
    setViewportLocationAndRotation(viewport_index, actor.get_actor_location(), actor.get_actor_rotation())

def setViewportLocationAndRotation_EXAMPLE():
    viewport_index = getActiveViewportIndex()
    setViewportLocationAndRotation(viewport_index, unreal.Vector(0.0, 0.0, 0.0), unreal.Rotator(0.0, 90.0, 0.0))

def snapViewportToActor_EXAMPLE():
    actors_in_world = unreal.GameplayStatics.get_all_actors_of_class(unreal.EditorLevelLibrary.get_editor_world(), unreal.Actor)
    random_actor_in_world = actors_in_world[random.randrange(len(actors_in_world))]
    viewport_index = getActiveViewportIndex()
    snapViewportToActor(viewport_index, random_actor_in_world)

# import EditorFunction_4 as ef
# reload(ef)
# ef.setViewportLocationAndRotation_EXAMPLE()
# ef.snapViewportToActor_EXAMPLE()
