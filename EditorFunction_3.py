# coding: utf-8
import unreal
import random

# active_viewport_only: bool : If True, will only affect the active viewport
# actor: obj unreal.Actor : The actor you want to snap to
def focusViewportOnActor(active_viewport_only=True, actor=None):
    # ! focus command
    command = 'CAMERA ALIGN'
    if active_viewport_only:
        command += ' ACTIVEVIEWPORTONLY'
    if actor:
        command += ' NAME=' + actor.get_name()
    unreal.CppLib.execute_console_command(command)

def focusAllViewportsOnSelectedActors_EXAMPLE():
    focusViewportOnActor(False)

def focusActiveViewportOnRandomActor_EXAMPLE():
    actors_in_world = unreal.GameplayStatics.get_all_actors_of_class(unreal.EditorLevelLibrary.get_editor_world(), unreal.Actor)
    random_actor_in_world = actors_in_world[random.randrange(len(actors_in_world))]
    focusViewportOnActor(True, random_actor_in_world)

# import EditorFunction_3 as ef
# reload(ef)
# ef.focusAllViewportsOnSelectedActors_EXAMPLE()
# ef.focusActiveViewportOnRandomActor_EXAMPLE()
