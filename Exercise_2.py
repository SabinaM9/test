# Original code:
Class MyClass:
    def init (self):
        self._my_dict = {"a":123, "b": True}
    def set_c(self, value):
        self._my_dict["c"] = value
    def get_c(self):
        return self._my_dict["c"]
    def get_dict_with_twice_a(self):
        buffer = self._my_dict
        buffer[“a”] *= 2
        return buffer

# 1) 'class' must be lowercase

# 2) 'init' is not the right form for constructor, it must be with double underscores '__init__'.
# Interpreter will recognize 'init' as a simple method, not a constructor.
# 3) Logical inconsistency. Constructor suggests creating different values for classes instances,
# but in this case all instances has equal values - so we can delete constructor and create global variables
# 4) In the method 'set_c' we refer to the parameter which is not exist. If we want to set 'c' we should create '__init__' because this parameter depends on instance

# My decision:
class MyClass:
    _my_dict = {"a": 123, "b": True}

    def __init__(self, value):
        self._my_dict.update(c=value)

    def get_c(self):
        return self._my_dict["c"]

    def get_dict_with_twice_a(self):
        buffer = self._my_dict
        buffer["a"] *= 2
        return buffer
