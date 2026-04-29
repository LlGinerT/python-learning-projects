from pathlib import Path

import pandas

BASE_DIR = Path(__file__).parent
df = pandas.read_csv(BASE_DIR / "nato_phonetic_alphabet.csv")

nato_alphabet = {row.letter: row.code for (index, row) in df.iterrows()}

while True:
    user_input = str(input("Enter a word: ").upper())
    try:
        output_list = [nato_alphabet[char] for char in user_input]
    except KeyError as e:
        print(f"{e}: Invalid value, please entry alphabetic character")
    else:
        print(output_list)
        break
