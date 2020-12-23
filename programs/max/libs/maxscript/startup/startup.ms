(
    RegPath = @"SOFTWARE\ToolsLibrary"
    EvalKey = ((DotNetClass "Microsoft.Win32.Registry").CurrentUser).OpenSubKey RegPath
    TheKey = EvalKey.GetValue "path"
    EvalKey.Close()

    python.ExecuteFile (TheKey + "\\programs\\max\\libs\\python\\startup\\scripts\\startup.py")
)