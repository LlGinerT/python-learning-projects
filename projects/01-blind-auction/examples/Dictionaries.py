dictionary = {"example_key1": "example_value1", "example_key2": "example_value2"}

# Access to dictionary
print(dictionary)

# Access to dictionary value by key
print(dictionary["example_key1"])

# Add new entry to dictionary
dictionary["example_new_key"] = "new_value"

# Edit an item in a dictionary
dictionary["example_new_key"] = "new_value2"

# Loop through a dictionary
for key in dictionary:
    # Print the key name
    print(key)
    # Print value for key
    print(dictionary[key])

# Wipe an existing dictionary
dictionary = {}
