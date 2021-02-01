// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "Kismet/BlueprintFunctionLibrary.h"
#include "CppLib.generated.h"

/**
*
*/
UCLASS()
class SCRIPT_PROJ_API UCppLib : public UBlueprintFunctionLibrary
{
    GENERATED_BODY()

public:

    UFUNCTION(BlueprintCallable, Category = "Unreal Python")
        static TArray<FString> GetSelectedAssets();

    UFUNCTION(BlueprintCallable, Category = "Unreal Python")
        static TArray<FString> GetSelectedFolders();

    UFUNCTION(BlueprintCallable, Category = "Unreal Python")
        static void SetSelectedAssets(TArray<FString> Paths);

    UFUNCTION(BlueprintCallable, Category = "Unreal Python")
        static void SetSelectedFolders(TArray<FString> Paths);

    UFUNCTION(BlueprintCallable, Category = "Unreal Python")
        static TArray<FString> GetAllProperties(UClass* Class);

    UFUNCTION(BlueprintCallable, Category = "Unreal Python")
        static void ExecuteConsoleCommand(FString ConsoleCommand);

    UFUNCTION(BlueprintCallable, Category = "Unreal Python")
        static void SetViewportLocationAndRotation(int ViewportIndex, FVector Location, FRotator Rotation);

    UFUNCTION(BlueprintCallable, Category = "Unreal Python")
        static int GetActiveViewportIndex();

    UFUNCTION(BlueprintCallable, Category = "Unreal Python")
        static void ExecutePythonScript(FString PythonScript);
};