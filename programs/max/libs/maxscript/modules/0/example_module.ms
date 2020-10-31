struct example_module
(
    module_name = "example_module",

    function example_function =
    (
        print("Example Function!")
    )
)

tools_library.add_library(example_module())
