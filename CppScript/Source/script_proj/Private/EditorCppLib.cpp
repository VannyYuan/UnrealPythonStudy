// Fill out your copyright notice in the Description page of Project Settings.


#include "EditorCppLib.h"
#include "Runtime/Engine/Classes/Kismet/GameplayStatics.h"

AActor* UEditorCppLib::BeginSpawnActor(const UObject* WorldContextObj, TSubclassOf < AActor > ActorClass, const FTransform& SpawnTransform) {
    return UGameplayStatics::BeginDeferredActorSpawnFromClass(WorldContextObj, ActorClass, SpawnTransform);
}

void UEditorCppLib::FinishSpawnActor(AActor* MyActor, const FTransform& SpawnTransform) {
    UGameplayStatics::FinishSpawningActor(MyActor, SpawnTransform);
}

