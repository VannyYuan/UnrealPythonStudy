// Fill out your copyright notice in the Description page of Project Settings.


#include "CppLib.h"
#include "Editor/ContentBrowser/Public/ContentBrowserModule.h"
#include "Editor/ContentBrowser/Private/SContentBrowser.h"
#include "Runtime/AssetRegistry/Public/AssetRegistryModule.h"
#include "Editor/UnrealEd/Public/Editor.h"
#include "Editor/UnrealEd/Public/LevelEditorViewport.h"
#include "../Plugins/Experimental/PythonScriptPlugin/Source/PythonScriptPlugin/Private/PythonScriptPlugin.h"


TArray<FString> UCppLib::GetSelectedAssets() {
    FContentBrowserModule& ContentBrowserModule = FModuleManager::LoadModuleChecked<FContentBrowserModule>("ContentBrowser");
    // get selected assets(
    TArray<FAssetData> SelectedAssets;
    ContentBrowserModule.Get().GetSelectedAssets(SelectedAssets);
    // convert assets to string
    TArray<FString> Result;
    for (FAssetData& AssetData : SelectedAssets) {
        Result.Add(AssetData.PackageName.ToString());
    }
    return Result;
}

void UCppLib::SetSelectedAssets(TArray<FString> Paths) {
    FContentBrowserModule& ContentBrowserModule = FModuleManager::LoadModuleChecked<FContentBrowserModule>("ContentBrowser");
    FAssetRegistryModule& AssetRegistryModule = FModuleManager::LoadModuleChecked<FAssetRegistryModule>("AssetRegistry");
    // convert the string to FName
    TArray<FName> PathsName;
    for (FString Path : Paths) {
        PathsName.Add(*Path);
    }
    FARFilter AssetFilter;
    AssetFilter.PackageNames = PathsName;
    // Find the assets
    TArray<FAssetData> AssetDatas;
    AssetRegistryModule.Get().GetAssets(AssetFilter, AssetDatas);
    // Ask the ContentBrowser to select them Different to python, the folder levels is also selected.
    ContentBrowserModule.Get().SyncBrowserToAssets(AssetDatas);
}

TArray<FString> UCppLib::GetSelectedFolders() {
    FContentBrowserModule& ContentBrowserModule = FModuleManager::LoadModuleChecked<FContentBrowserModule>("ContentBrowser");
    TArray<FString> SelectedFolders;
    ContentBrowserModule.Get().GetSelectedFolders(SelectedFolders);
    return SelectedFolders;
}

void UCppLib::SetSelectedFolders(TArray<FString> Paths) {
    FContentBrowserModule& ContentBrowserModule = FModuleManager::LoadModuleChecked<FContentBrowserModule>("ContentBrowser");
    TArray<FString> SelectedFolders;
    ContentBrowserModule.Get().SyncBrowserToFolders(Paths);
}

TArray<FString> UCppLib::GetAllProperties(UClass* Class) {
    TArray<FString> Ret;
    if (Class != nullptr) {
        for (TFieldIterator<UProperty> It(Class); It; ++It) {
            UProperty* Property = *It;
            if (Property->HasAnyPropertyFlags(EPropertyFlags::CPF_Edit)) {
                Ret.Add(Property->GetName());
            }
        }
    }
    return Ret;
}

void UCppLib::ExecuteConsoleCommand(FString ConsoleCommand) {
    if (GEditor) {
        UWorld* World = GEditor->GetEditorWorldContext().World();
        if (World) {
            GEditor->Exec(World, *ConsoleCommand, *GLog);
        }
    }
}

void UCppLib::SetViewportLocationAndRotation(int ViewportIndex, FVector Location, FRotator Rotation) {
    if (GEditor != nullptr && ViewportIndex < GEditor->GetLevelViewportClients().Num()) {
        FLevelEditorViewportClient* LevelViewportClient = GEditor->GetLevelViewportClients()[ViewportIndex];
        if (LevelViewportClient != nullptr) {
            LevelViewportClient->SetViewLocation(Location);
            LevelViewportClient->SetViewRotation(Rotation);
        }
    }
}

int UCppLib::GetActiveViewportIndex() {
    int Index = 1;
    if (GEditor != nullptr && GCurrentLevelEditingViewportClient != nullptr) {
        GEditor->GetLevelViewportClients().Find(GCurrentLevelEditingViewportClient, Index);
    }
    return Index;
}

void UCppLib::ExecutePythonScript(FString PythonScript) {
    FPythonScriptPlugin::Get()->ExecPythonCommand(*PythonScript);
}
