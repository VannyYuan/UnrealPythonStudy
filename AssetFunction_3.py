# coding: utf-8

import unreal

# import AssetFunction_3 as af
# reload(af)
# af.createDirectory()

# ! 创建文件夹 ~/MyNewDirectory
def createDirectory():
    unreal.EditorAssetLibrary.make_directory('/Game/MyAsset/MyNewDirectory')

# ! 复制文件夹 ~/MyNewDirectory -> ~/MyNewDirectory_Duplicated
def duplicateDirectory():
    return unreal.EditorAssetLibrary.duplicate_directory('/Game/MyAsset/MyNewDirectory', '/Game/MyAsset/MyNewDirectory_Duplicated')

# ! 删除文件夹 ~/MyNewDirectory
def deleteDirectory():
    unreal.EditorAssetLibrary.delete_directory('/Game/MyAsset/MyNewDirectory')

# ! 重命名文件夹 ~/MyNewDirectory_Duplicated -> ~/MyNewDirectory_Renamed
def renameDirectory():
    return unreal.EditorAssetLibrary.rename_directory('/Game/MyAsset/MyNewDirectory_Duplicated', '/Game/MyAsset/MyNewDirectory_Renamed')

# ! 复制资产 ~/dear -> ~/dear_Duplicated
def duplicateAsset():
    return unreal.EditorAssetLibrary.duplicate_asset('/Game/MyAsset/Textures/dear', '/Game/MyAsset/Textures/dear_Duplicated')

# ! 删除资产 ~/dear
def deleteAsset():
    unreal.EditorAssetLibrary.delete_asset('/Game/MyAsset/Textures/dear')

# ! 判断资产是否存在
def assetExist():
    print unreal.EditorAssetLibrary.does_asset_exist('/Game/MyAsset/Textures/dear')
    print unreal.EditorAssetLibrary.does_asset_exist('/Game/MyAsset/Textures/dear_Duplicated')

# ! 重命名资产 ~/dear_Duplicated -> ~/dear_Renamed
def renameAsset():
    unreal.EditorAssetLibrary.rename_asset('/Game/MyAsset/Textures/dear_Duplicated', '/Game/MyAsset/Textures/dear_Renamed')

# ! 显示复制资产提示框 ~/dear_Renamed -> ~/dear_Duplicated
def duplicateAssetDialog(show_dialog=True):
    if show_dialog:
        unreal.AssetToolsHelpers.get_asset_tools().duplicate_asset_with_dialog('dear_Duplicated', '/Game/MyAsset/Textures', unreal.load_asset('/Game/MyAsset/Textures/dear_Renamed'))
    else:
        unreal.AssetToolsHelpers.get_asset_tools().duplicate_asset('dear_Duplicated', '/Game/MyAsset/Textures', unreal.load_asset('/Game/MyAsset/Textures/dear_Renamed'))

# ! 显示重命名提示框 
# ! ~/dear_Renamed -> ~/dear_Renamed_2
# ! ~/dear_Duplicated -> ~/dear_Duplicated_Renamed
def renameAssetDialog(show_dialog=True):
    first_renmae_data = unreal.AssetRenameData(unreal.load_asset('/Game/MyAsset/Textures/dear_Renamed'), '/Game/MyAsset/Textures', 'dear_Renamed_2')
    second_rename_data = unreal.AssetRenameData(unreal.load_asset('/Game/MyAsset/Textures/dear_Duplicated'), '/Game/MyAsset/Textures', 'dear_Duplicated_Renamed')
    if show_dialog:
        unreal.AssetToolsHelpers.get_asset_tools().rename_assets_with_dialog([first_renmae_data, second_rename_data])
    else:
        unreal.AssetToolsHelpers.get_asset_tools().rename_assets([first_renmae_data, second_rename_data])