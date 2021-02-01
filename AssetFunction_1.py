# coding: utf-8
import os

import unreal

# import AssetFunction_1 as af
# reload(af)
# af.importMyAssets()

asset_folder = 'D:/ue4/test/asset'
texture_jpg = os.path.join(asset_folder, 'dear.jpg').replace('\\','/')
sound_mp3 = os.path.join(asset_folder, 'easy.mp3').replace('\\','/')

def importMyAssets():
    texture_task = bulidImportTask(texture_jpg, '/Game/MyAsset/Textures')
    sound_task = bulidImportTask(sound_mp3, '/Game/MyAsset/Sounds')
    executeImportTasks([texture_task, sound_task])

# ! 设置导入资产属性
def bulidImportTask(filename, destination_path):
    task = unreal.AssetImportTask()
    task.set_editor_property('automated', True)
    task.set_editor_property('destination_name', '')
    task.set_editor_property('destination_path', destination_path)
    task.set_editor_property('filename', filename)
    task.set_editor_property('replace_existing', True)
    task.set_editor_property('save', True)
    return task

def executeImportTasks(tasks):
    unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks(tasks)
    for task in tasks:
        for path in task.get_editor_property('imported_object_paths'):
            print 'Imported {}'.format(path)