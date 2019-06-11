import inspect

def a_function():
    return

print(a_function)
print(inspect.isfunction(a_function))

result = a_function()
print(result)
