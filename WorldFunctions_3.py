# coding: utf-8

import unreal

# return: obj List unreal.Actor : The selected actors in the world
def getSelectedActors():
    return unreal.EditorLevelLibrary.get_selected_level_actors()

# Note: Will always clear the selection before selecting.
# actors_to_select: obj List unreal.Actor : The actors to select.
def selectActors(actors_to_select=[]):
    unreal.EditorLevelLibrary.set_selected_level_actors(actors_to_select)

def selectActors_EXAMPLE():
    import WorldFunctions_2
    all_actors = WorldFunctions_2.sortActors()
    actors_to_select = []
    for x in range(len(all_actors)):
        if x % 2:
            actors_to_select.append(all_actors[x])
    selectActors(actors_to_select)

def clearActorSelection_EXAMPLE():
    selectActors()

# import WorldFunctions_3 as wf
# reload(wf)
# wf.selectActors_EXAMPLE()
# print wf.getSelectedActors()