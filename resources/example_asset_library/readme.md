
#Asset Library
---------------------------------------

## Top-Level Library Types: 
#### *Content*: 

Contains actual assets - Ie, materials, geometry, etc

#### *Shaders*: 

Contains either usable shaders or commonly used hlsl libs

#### *Shelves*: 

Contains sub-shelves for different program types, each with their own sub-libraries, Ie:

> **Example structure:**
├── Houdini
│   ├── Common
│   └── ...
├── Painter
│   ├── Common
│   └── ...
├── Designer
│   ├── Common
│   └── ...
└── ...