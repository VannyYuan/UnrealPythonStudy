# coding: utf-8

import unreal
import random
import time

def executeSlowTask():
    quantity_steps_in_slow_task = 10
    with unreal.ScopedSlowTask(quantity_steps_in_slow_task, 'My Slow Task Text ...') as slow_task:
        slow_task.make_dialog(True)
        for x in range(quantity_steps_in_slow_task):
            if slow_task.should_cancel():
                break
            slow_task.enter_progress_frame(1, 'My Slow Task Text ...' + str(x) + ' / ' + str(quantity_steps_in_slow_task))
            # Execute slow logic
            deferredSpawnActor()
            time.sleep(1)

def deferredSpawnActor():
    world = unreal.EditorLevelLibrary.get_editor_world()
    # ! blueprint actor
    actor_class = unreal.EditorAssetLibrary.load_blueprint_class('/Game/BluePrint/bp_actor')
    actor_location = unreal.Vector(random.uniform(0.0, 2000.0), random.uniform(0.0, 2000.0), 0.0)
    actor_rotation = unreal.Rotator(random.uniform(0.0, 360.0), random.uniform(0.0, 360.0), random.uniform(0.0, 360.0))
    actor_scale = unreal.Vector(random.uniform(0.1, 2.0), random.uniform(0.1, 2.0), random.uniform(0.1, 2.0))
    actor_transform = unreal.Transform(actor_location, actor_rotation, actor_scale)
    # ! "GameplayStatics.begin_spawning_actor_from_class()" is deprecated. Use BeginDeferredActorSpawnFromClass instead.
    # actor = unreal.GameplayStatics.begin_spawning_actor_from_class(world, actor_class, actor_transform)
    # unreal.GameplayStatics.finish_spawning_actor(actor, actor_transform)
    actor = unreal.EditorCppLib.begin_spawn_actor(world, actor_class, actor_transform)
    unreal.EditorCppLib.finish_spawn_actor(actor, actor_transform)


# import EditorFunction_1 as ef
# reload(ef)
# ef.executeSlowTask()