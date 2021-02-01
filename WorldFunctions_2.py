# coding: utf-8

import unreal

def getSelectedActors():
    # ! Selected
    selected_actors = unreal.EditorLevelLibrary.get_selected_level_actors()
    return selected_actors

def getClassActors(actor_class):
    # ! Class
    world = unreal.EditorLevelLibrary.get_editor_world()
    class_actors = unreal.GameplayStatics.get_all_actors_of_class(world, actor_class)
    return class_actors

def getTagActors(actor_tag):
    # ! Tag
    world = unreal.EditorLevelLibrary.get_editor_world()
    tag_actors = unreal.GameplayStatics.get_all_actors_with_tag(world, actor_tag)
    return tag_actors

def getAllActors():
    # ! All
    world = unreal.EditorLevelLibrary.get_editor_world()
    all_actors = unreal.GameplayStatics.get_all_actors_of_class(world, unreal.Actor)
    return all_actors

def sortActors(use_selection = False, actor_class = None, actor_tag = None):
    """如果有指定，则筛选指定 Actors。否则返回全部 Actors

    """
    # ! return all actors
    if not use_selection and not actor_class and not actor_tag:
        return getAllActors()

    # ! get sort actors
    selected_actors, class_actors, tag_actors = [], [], []
    if use_selection:
        selected_actors = list(getSelectedActors())
    if actor_class:
        class_actors = list(getClassActors(actor_class))
    if actor_tag:
        tag_actors = list(getTagActors(actor_tag))

    final_actors = selected_actors + class_actors + tag_actors
    for actor in final_actors:
        if use_selection and actor in selected_actors:
            pass
        else:
            final_actors.remove(actor)
            continue
        if actor_class and actor in class_actors:
            pass
        else:
            final_actors.remove(actor)
            continue
        if actor_tag and actor in tag_actors:
            pass
        else:
            final_actors.remove(actor)
            continue
    if final_actors:
        return final_actors
    else:
        return getAllActors()


def cast(object_to_cast, object_class):
    try:
        return object_class.cast(object_to_cast)
    except:
        return getAllActors()

# import WorldFunctions_2 as wf
# reload(wf)
# wf.sortActors(True, unreal.StaticMeshActor, 'MyTag')