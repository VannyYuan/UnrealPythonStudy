// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "Kismet/BlueprintFunctionLibrary.h"
#include "EditorCppLib.generated.h"

/**
 * 
 */
UCLASS()
class SCRIPT_PROJ_API UEditorCppLib : public UBlueprintFunctionLibrary
{
	GENERATED_BODY()
	
public:

	UFUNCTION(BlueprintCallable, Category = "Unreal Python")
		static AActor* BeginSpawnActor(const UObject* WorldContextObj,TSubclassOf < AActor > ActorClass, const FTransform& SpawnTransform);

	UFUNCTION(BlueprintCallable, Category = "Unreal Python")
		static void FinishSpawnActor(AActor* MyActor, const FTransform& SpawnTransform);
};
