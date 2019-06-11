def a_generator_function():
    print("First execution")
    i = 0
    while True:
        print("Before yield: {}".format(i))
        yield
        i += 1
        print("After yield: {}".format(i))
        if i > 2:
            return

print('\n\tCalling a generator function returns a generator iterator')
generator_iterator = a_generator_function()
print(generator_iterator)

print('\n\tCalling __iter__() on a generator iterator returns itself')
test_me = generator_iterator.__iter__()
print(test_me)

print('\n\tGenerator iterators implement next')
generator_iterator = a_generator_function()
test_me = generator_iterator.__next__
print(test_me)

print('\n\tGenerator iterators track state')
generator_iterator = a_generator_function()
generator_iterator.__next__()
generator_iterator.__next__()
generator_iterator.__next__()

print('\n\tGenerator iterators raise StopIteration')
generator_iterator.__next__()
