capitals = {"France": "Paris", "Spain": "Madrid"}

# Nested list in dictionary
travel_log = {"France": ["Paris", "Lille", "Dijon"], "Germany": ["Stuttgart", "Berlin"]}

# print Lille
print(travel_log["France"][1])

# Nested list (2d list)
nested_list = ["A", "B", ["C", "D"]]

print(nested_list[2][1])

# Nested dictionary in other dictionary
travel_nested_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5,
    },
}

print(travel_nested_log["Germany"]["cities_visited"][2])
