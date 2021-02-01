# coding: utf-8

import unreal

# import AssetFunction_4 as af
# reload(af)
# af.generateColoredDirectories()

def generateColoredDirectories():
    for x in range(40, 80):
        dir_path = '/Game/MyAsset/MyColorFolder/' + str(x)
        linear_color = getGradientColor(x)
        unreal.CppLib.set_folder_color(dir_path, linear_color)
        unreal.EditorAssetLibrary.make_directory(dir_path)

def getGradientColor(x):
    x = float(x) / 100
    return unreal.LinearColor(x, 1-x, 1-x, 1)