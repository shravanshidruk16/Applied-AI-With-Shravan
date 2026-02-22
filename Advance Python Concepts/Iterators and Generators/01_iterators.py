my_list = [1,2,3,4,5,6,7,8,9]
iterator = iter(my_list)
print("This is type of iterator:",type(iterator))
print("This is memory address:",iterator) 
print("1st iteration",next(iterator))
print("2nd iteration",next(iterator))
print("And so on.")


"""
Iterators - Iterators are advanced Python concepts that allow for efficient looping and memory management . Iterators provide a way to access elements of a collection sequentially without exposing the underlying structure
"""