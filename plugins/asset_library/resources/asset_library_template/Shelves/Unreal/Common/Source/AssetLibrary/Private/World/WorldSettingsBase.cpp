// Fill out your copyright notice in the Description page of Project Settings.


#include "AssetLibrary/Public/World/WorldSettingsBase.h"

#include "Components/DirectionalLightComponent.h"
#include "Components/SkyLightComponent.h"
#include "Atmosphere/AtmosphericFogComponent.h"
#include "Components/ExponentialHeightFogComponent.h"

AWorldSettingsBase::AWorldSettingsBase()
{
    //-- Init Components

    SunLight = CreateDefaultSubobject<UDirectionalLightComponent>(TEXT("Sun Light"));
    SunLight->SetupAttachment(RootComponent);

    AmbientLight = CreateDefaultSubobject<USkyLightComponent>(TEXT("Ambient Light"));
    AmbientLight->SetupAttachment(RootComponent);

    AtmosphericFog = CreateDefaultSubobject<UAtmosphericFogComponent>(TEXT("Atmospheric Fog"));
    AtmosphericFog->SetupAttachment(RootComponent);

    HeightFog = CreateDefaultSubobject<UExponentialHeightFogComponent>(TEXT("Height Fog"));
    HeightFog->SetupAttachment(RootComponent);

}

void AWorldSettingsBase::PostEditChangeProperty(struct FPropertyChangedEvent& e)
{
    Super::PostEditChangeProperty(e);

    //-- Sun Light
    SunLight->SetWorldRotation(SunRotation);
    SunLight->SetVisibility(bUseSunLight);
    SunLight->SetIntensity(SunIntensity);
    SunLight->SetLightColor(SunColour);
    SunLight->bUseTemperature = bSunUseTemp;
    SunLight->SetTemperature(SunTemp);

    //-- Ambient Light
    AmbientLight->SetVisibility(bUseAmbientLight);
    AmbientLight->SetIntensity(AmbientLightIntensity);
    AmbientLight->SetLightColor(AmbientLightColour);

    //-- Atmospheric Fog
    AtmosphericFog->SetVisibility(bUseAtmosphericFog);
    AtmosphericFog->SetDefaultLightColor(FLinearColor(0.125f, 0.125f, 0.125f, 1.0f));
    AtmosphericFog->DisableSunDisk(true);

    //-- Height Fog
    HeightFog->SetVisibility(bUseHeightFog);
}