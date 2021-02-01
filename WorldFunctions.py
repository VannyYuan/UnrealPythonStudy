# coding: utf-8

import unreal

def spawnActor():
    actor_class = unreal.EditorAssetLibrary.load_blueprint_class('/Game/BluePrint/MyActor')
    actor_location = unreal.Vector(0.0, 0.0, 0.0)
    actor_rotation = unreal.Rotator(0.0, 0.0, 0.0)
    unreal.EditorLevelLibrary.spawn_actor_from_class(actor_class, actor_location, actor_rotation)

def deferredSpawnActor():
    world = unreal.EditorLevelLibrary.get_editor_world()
    actor_class = unreal.EditorAssetLibrary.load_blueprint_class('/Game/BluePrint/MyActor')
    actor_location = unreal.Vector(0.0, 0.0, 0.0)
    actor_rotation = unreal.Rotator(0.0, 0.0, 0.0)
    actor_scale = unreal.Vector(1.0, 1.0, 1.0)

    actor_transform = unreal.Transform(actor_location, actor_rotation, actor_scale)
    actor = unreal.EditorCppLib.begin_spawn_actor(world, actor_class, actor_transform)
    actor_tags = actor.get_editor_property('tags')
    actor_tags.append('My Python Tag')
    actor.set_editor_property('tags', actor_tags)
    unreal.EditorCppLib.finish_spawn_actor(actor, actor_transform)


# import WorldFunctions as wf
# reload(wf)
# wf.spawnActor()