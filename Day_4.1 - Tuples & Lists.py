# Tuples vs Lists in Python

# ----- Tuple Example (Immutable) -----
name = 'ishant'
names = ('john', 'jennie', 'jim')  # tuple

print("Tuple Example")
print(name, type(name), id(name))
print(names, type(names), id(names))
print(names[0], type(names[0]), id(names[0]))

# Updating values
name = 'auribises'
names = 'sia', 'leo', 'kim'  # tuple

print("\nAfter Re-assignment")
print(name, type(name), id(name))
print(names, type(names), id(names))

# The below line will raise an error, as tuples are immutable
# names[0] = 'harry'

print("\nTuples are immutable, so direct modification is not allowed.")

# ----- List Example (Mutable) -----
names = ["john", "jennie", "jim"]  # list

print("\nList Example")
print('names:', names, type(names), id(names))

# Reference Copy
followers = names

print('followers:', followers, type(followers), id(followers))
print('Original names[1]:', names[1], type(names[1]), id(names[1]))

# Updating value using reference
followers[1] = "george"

print("\nAfter updating followers[1] to 'george':")
print('names now:', names, type(names), id(names))
print('followers now:', followers, type(followers), id(followers))
print('Updated names[1]:', names[1], type(names[1]), id(names[1]))

# Assigning a new list to 'names'
names = ['leo', 'george', 'ben']

print("\nAfter re-assigning a new list to 'names':")
print('names now:', names, type(names), id(names))
print('followers remains:', followers, type(followers), id(followers))
print('names[1]:', names[1], id(names[1]))
print('followers[1]:', followers[1], id(followers[1]))
