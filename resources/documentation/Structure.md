# Structure

## Base Project Structure

Structure of the base Tools Library

```
Tools Library
├─── bin                    => Binaries, Executables, Batch files ..
|   └─── Python {version}
├─── config                 => Configuration files (Ie, .json, .ini, .xml)
├─── libs                   => Libraries for different languages
|   ├─── External           => External libraries
|   └─── Python             => 3.x compatible
|       ├─── tools_library
|       └─── ..
├─── plugins                => Contains Tools Library based plugins
|   ├─── asset_library
|   └─── ..
├─── programs               => Contains individual DCC Application plugins
|   ├─── designer
|   ├─── max
|   └─── ..
├─── resources              => 
|   ├─── documentation      =>
|   └─── ..
├─── .vscode                =>
|   └─── ..
├─── scripts                => Single file only scripts - can be any language
|   └─── Startup
|   └─── Install
|   └─── Uninstall
|   └─── ..
├─── .gitignore
├─── open_git_repo.bat
└─── README.md
```

## DCC Program Plugin Structure

Structure for individual DCC Program plugins for the tools library
(Stored under "root/programs/program_name")

```
Program (Ie, 3DS_Max)
├─── bin                    => Binaries, Executables, Batch files ..
├─── config                 => Config files specific to the current DCC Application
├─── libs                   => Program specific libraries / modules
|   └─── Python
|       └─── module_name
|   └─── .. (Ie, Maxscript)
|       └─── module_name
├─── plugins                => Compiled plugins for the program
├─── resources              => Program specific resource files
├─── scripts                => Program specific script files
|   └─── Startup
|   └─── Install
|   └─── Uninstall
|   └─── ..
└─── tools                  => Tools
```

> Note: "Plugins" here does not refer to a plugin in the same way as the Tools Library plugins.
This should contain plugins in the required method for the specific program (Ie, Max DLM/DLE, Designer Python, Unreal module)

## Tools Library Plugin Structure

Structure for a Tools Library plugin
(Stored under "root/plugins/plugin_name")

```
Plugin (Ie, Asset_Library)
├─── bin                    => Binaries, Executables, Batch files ..
├─── config                 => Config files specific to the current Plugin
├─── libs                   => Plugin specific libraries / modules
|   └─── Python
|       └─── module_name
├─── programs
|   └─── ..                 => Matching structure to DCC Program Plugin Structure
|                          this is treated like an extension to the program plugin
|                          but is only used when both the plugin and program are enabled
|
├─── resources              => Plugin specific resource files
└─── scripts                => Plugin specific script files
    └─── Startup
    └─── Install
    └─── Uninstall
    └─── ..
```

> Note: Plugins can contain sub-programs, which are set up the same as a top level program plugin