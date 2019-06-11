import inspect

def a_generator_function():
    yield

print(a_generator_function)
print(inspect.isgeneratorfunction(a_generator_function))

result = a_generator_function()
print(result)
