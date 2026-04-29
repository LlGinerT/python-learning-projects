from pathlib import Path

import pandas

BASE_DIR = Path(__file__).parent
data = pandas.read_csv(BASE_DIR / "weather_data.csv")

# print(data)

""" data_dict = data.to_dict()
print(data_dict)

data["temp"].to_list() """  # take single column/serie and convert to list

print(data["temp"].mean())
print(data["temp"].max())

# Get data in series
print(
    data["condition"]
)  # like list, no with index, only with string name of the column
print(data.condition)  # or like method without ()

# Access to specific row
print(data[data.day == "Monday"])

# Access to specific row with max temp in the DataFrame
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.temp)
fahrenheit = monday.temp * (9 / 5) + 32
print(fahrenheit)


# Create a DataFrame from dict
data_dict = {"students": ["Amy", "James", "Angela"], "scores": [76, 56, 65]}

data = pandas.DataFrame(data_dict)
print(data)

# Store the DataFrame into a csv
data.to_csv(BASE_DIR / "students.csv")
