# coding: utf-8

import unreal

# import AssetFunction_6 as af
# reload(af)
# af.showAssetsInContentBrowser()

# ! 选择指定资产
def showAssetsInContentBrowser():
    paths = [
        '/Game/MyAsset/Sounds/easy',
        '/Game/MyAsset/Textures/dear'
    ]
    unreal.EditorAssetLibrary.sync_browser_to_objects(paths)

# ! 调用 C++ 命令设置选择文件夹
def getSelectedAssets():
    return unreal.CppLib.get_selected_assets(paths)

# ! 调用 C++ 命令设置选择文件夹
def setSelectedAssets():
    paths = [
        '/Game/MyAsset/Sounds/easy',
        '/Game/MyAsset/Textures/dear'
    ]
    return unreal.CppLib.set_selected_assets(paths)

# ! 调用 C++ 命令获取选择文件夹
def getSelectedFolders():
    return unreal.CppLib.get_selected_folders()

# ! 调用 C++ 命令设置文件夹
def setSelectedFolders():
    paths = [
        '/Game/MyAsset/Sounds',
        '/Game/MyAsset/Textures'
    ]
    return unreal.CppLib.set_selected_folders(paths)