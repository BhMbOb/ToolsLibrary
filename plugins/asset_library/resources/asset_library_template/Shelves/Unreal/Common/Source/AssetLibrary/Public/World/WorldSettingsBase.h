// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/WorldSettings.h"
#include "WorldSettingsBase.generated.h"

/**
 * 
 */
UCLASS()
class ASSETLIBRARY_API AWorldSettingsBase : public AWorldSettings
{
	GENERATED_BODY()

public:
	AWorldSettingsBase();
	void PostEditChangeProperty(struct FPropertyChangedEvent& e) override;


public:	// Sun Light
	UPROPERTY(BlueprintReadWrite, EditAnywhere, Category = "Scene")
		bool bUseSunLight = true;

	UPROPERTY(BlueprintReadOnly, EditAnywhere, Category = "Scene|Sun", meta = (EditCondition = "bUseSunLight"))
		class UDirectionalLightComponent* SunLight;

	UPROPERTY(BlueprintReadWrite, EditAnywhere, Category = "Scene|Sun", meta = (EditCondition = "bUseSunLight"))
		FRotator SunRotation = FRotator(0.0, -45.0, 0.0);

	UPROPERTY(BlueprintReadWrite, EditAnywhere, Category = "Scene|Sun", meta = (EditCondition = "bUseSunLight"))
		float SunIntensity = 10.0f;

	UPROPERTY(BlueprintReadWrite, EditAnywhere, Category = "Scene|Sun", meta = (EditCondition = "bUseSunLight"))
		FLinearColor SunColour = FLinearColor(1.0, 1.0, 1.0, 1.0);

	UPROPERTY(BlueprintReadWrite, EditAnywhere, Category = "Scene|Sun", meta = (EditCondition = "bUseSunLight"))
		bool bSunUseTemp = false;

	UPROPERTY(BlueprintReadWrite, EditAnywhere, Category = "Scene|Sun", meta = (EditCondition = "bUseSunLight"))
		float SunTemp = 6500.0f;


public:	// Ambient Light
	UPROPERTY(BlueprintReadWrite, EditAnywhere, Category = "Scene")
		bool bUseAmbientLight = true;

	UPROPERTY(BlueprintReadOnly, EditAnywhere, Category = "Scene|Ambient Light", meta = (EditCondition = "bUseAmbientLight"))
		class USkyLightComponent* AmbientLight;

	UPROPERTY(BlueprintReadWrite, EditAnywhere, Category = "Scene|Ambient Light", meta = (EditCondition = "bUseAmbientLight"))
		float AmbientLightIntensity = 1.0f;

	UPROPERTY(BlueprintReadWrite, EditAnywhere, Category = "Scene|Ambient Light", meta = (EditCondition = "bUseAmbientLight"))
		FLinearColor AmbientLightColour = FLinearColor(1.0, 1.0, 1.0, 1.0);


public:	// Atmospheric Fog
	UPROPERTY(BlueprintReadWrite, EditAnywhere, Category = "Scene")
		bool bUseAtmosphericFog = true;

	UPROPERTY(BlueprintReadOnly, EditAnywhere, Category = "Scene|Atmospheric Fog", meta = (EditCondition = "bUseAtmosphericFog"))
		class UAtmosphericFogComponent* AtmosphericFog;


public:	// Height Fog
	UPROPERTY(BlueprintReadWrite, EditAnywhere, Category = "Scene")
		bool bUseHeightFog = true;

	UPROPERTY(BlueprintReadOnly, EditAnywhere, Category = "Scene|Height Fog", meta = (EditCondition = "bUseHeightFog"))
		class UExponentialHeightFogComponent* HeightFog;
};
