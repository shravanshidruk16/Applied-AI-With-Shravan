"""
Generators 
They are a simpler way to create iterators . They use the yield keyword to produce a series of values lazily, which means they generate values on the fly and do not store them in memory

"""

def square(n):
    for i in range(3):
        yield i**2

# First way of using generator
print("# First way of using generator")    
for i in square(3):
    print(i)

# Second way of using generator
print("# Second way of using generator")
a = square(3)
for i in range(3):
    print(next(a))


print("Another method of using generators")

def my_generator():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

gen = my_generator()

for _ in range(5):
    print(next(gen))