# coding: utf-8

import unreal


def createGenericAsset(asset_path='', unique_name=True, asset_class=None, asset_factory=None):
    if unique_name:
        asset_path, asset_name = unreal.AssetToolsHelpers.get_asset_tools().create_unique_asset_name(base_package_name=asset_path, suffix='')
    if not unreal.EditorAssetLibrary.does_asset_exist(asset_path=asset_path):
        path = asset_path.rsplit('/', 1)[0]
        name = asset_path.rsplit('/', 1)[1]
        return unreal.AssetToolsHelpers.get_asset_tools().create_asset(asset_name=name, package_path=path, asset_class=asset_class, factory=asset_factory)
    return unreal.load_asset(asset_path)

def createGenericAsset_EXAMPLE():
    base_path = '/Game/MyAsset/GenericAssets/'
    generic_assets = [
        [base_path + 'sequence',        unreal.LevelSequence,  unreal.LevelSequenceFactoryNew()],
        [base_path + 'material',        unreal.Material,       unreal.MaterialFactoryNew()],
        [base_path + 'world',           unreal.World,          unreal.WorldFactory()],
        [base_path + 'particle_system', unreal.ParticleSystem, unreal.ParticleSystemFactoryNew()],
        [base_path + 'paper_flipbook',  unreal.PaperFlipbook,  unreal.PaperFlipbookFactory()],
        [base_path + 'data_table',      unreal.DataTable,      unreal.DataTableFactory()], # Will not work
    ]
    for asset in generic_assets:
        print createGenericAsset(asset[0], True, asset[1], asset[2])

# import AssetFunction_7 as af
# reload(af)
# af.createGenericAsset_EXAMPLE()