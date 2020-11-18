#map is an iterator
 #   https://www.geeksforgeeks.org/python-map-function/
# Python program to demonstrate working 
# of map. 
  
# Return double of n 
def addition(n): 
    return n + n 
  
# We double all numbers using map() 
numbers = (1, 2, 3, 4) 
result = map(addition, numbers) 

print(list(result))
#[2,4,6,8] 
print(result)
#<map object>


# Initialize the `kilometer` list
kilometer = [39.2, 36.5, 37.3, 37.8]

# Construct `feet` with `map()`
feet = list(map(lambda x: float(3280.8399)*x, kilometer))

# Print `feet` as a list
print(feet)

#lambda is an anonymous function, a function without a name


integer_feet = [int(i) for i in feet]

print(integer_feet)
uneven = []

def test_mod(n):
	for i in integer_feet:
		if i % 2 != 0:
			uneven.append(i)

test_mod(feet)
print(uneven)



