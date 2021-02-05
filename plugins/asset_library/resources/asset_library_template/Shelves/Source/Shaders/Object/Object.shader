{
    "properties":{
        "two_sided": false,
        "abstract": true
    },

    "parameters:default":{
        "UvScale": 1.0,
        "HeightRatio":0.0,
        "AlbedoMap": "",
        "NormalMap": "",
        "NormalMapStrength": 1.0,
        "bUseAmbientOcclusion": true,
        "bUseMetalness": true,
        "bUseOpacity": false,
        "Opacity": 1.0,
        "Metalness": 0.0,
        "bUseNormals": true,
        "Roughness": 0.5,
        "AlbedoHue": 1.0,
        "AlbedoSaturation": 1.0,
        "AlbedoLightness": 1.0,
        "IndexOfRefraction": 1.0,
        "Specular": 0.5,
        "bUseIndexOfRefraction": false,
        "InnerDarkenAmount": 0.0,
        "OuterLightenAmount": 0.0,
        "InnerSpecular": 0.5,
        "OuterSpecular": 0.5,
        "FuzzStrength": 1.0,
        "bEnableFuzz": false,
        "SurfaceTint": [0.0, 0.0, 0.0, 1.0],
        "bEnableSurfaceTint": false,
        "bUseDitheredOpacity": false
    },
    
    "parameters:effect-metallic":{
        "bEnableMetallicEffect": false,
        "MetallicPurity": 0.0
    },

    "unreal":{
        "path": "common/manual/shaders/object/shd_abs_object"
    }
}