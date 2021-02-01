# coding: utf-8

import unreal

# import AssetFunction_5 as af
# reload(af)
# print af.getAllOpenedAssets()
# af.closeAssets()

# ! 加载资产
def openAssets():
    assets = [
        unreal.load_asset('/Game/MyAsset/Textures/dear'),
        unreal.load_asset('/Game/MyAsset/Sounds/easy'),
        unreal.load_asset('/Game/MyAsset/StaticMeshes/static_fbx')
    ]
    unreal.AssetToolsHelpers.get_asset_tools().open_editor_for_assets(assets)

# ! 获取已经打开的资产列表
def getAllOpenedAssets():
    return unreal.CppLib.get_assets_opened_in_editor()

# ! 关闭所有打开的资产
def closeAssets():
    assets = getAllOpenedAssets()
    unreal.CppLib.close_editor_for_assets(assets)