from pathlib import Path

import pandas as pd

squirrel_dict = {"fur color": ["Gray", "Black", "Cinnamon"], "count": []}
BASE_DIR = Path(__file__).parent

df = pd.read_csv(
    BASE_DIR / "2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"
)

primary_color = df["Primary Fur Color"]
for color in squirrel_dict["fur color"]:
    total_squirrels = len(df[primary_color == color])
    squirrel_dict["count"].append(total_squirrels)

color_count_df = pd.DataFrame(squirrel_dict)
color_count_df.to_csv(BASE_DIR / "primary_color_count.csv")
