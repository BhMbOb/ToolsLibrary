import tools_library


class __ProgramContextDecorators(object):
    def __init__(self, ctx=""):
        self.ctx = ctx

    def program_method(self, func):
        """Template for a decorator which ensures a method can only be
        called from within a certain program's context"""
        def wrapper(*args, **kwargs):
            if(tools_library.program_context() == self.ctx):
                return func(*args, **kwargs)
            else:
                assert False, ("{}: The method \"{}\" cannot be called outside of {}.".format(
                    __file__, func.__name__, self.ctx))
        return wrapper


# create a "program_method" decorator for all of the available programs
# Ie, `@ue4_method`
for program_name in tools_library.program_names():
    exec("globals()[\"{}_method\"] = __ProgramContextDecorators(ctx=\"{}\").program_method".format(
        program_name, program_name))
