from pathlib import Path

PLACEHOLDER = "[name]"
BASE_DIR = Path(__file__).parent


with open(
    BASE_DIR / "Input" / "Names" / "invited_names.txt"
) as invited_names:
    names = invited_names.readlines()

with open(
    BASE_DIR / "Input" / "Letters" / "starting_letter.txt"
) as starting_letter:
    letter = starting_letter.read()
    for name in names:
        stripped_name = (
            name.strip()
        )  # Eliminar los saltos de línea y espacios en blanco
        personalized_letter = letter.replace(
            PLACEHOLDER, stripped_name
        )  # Reemplazar [name] por el nombre actual
        with open(
            BASE_DIR / "Output" / "ReadyToSend" / f"Mail_to_{stripped_name}.txt",
            "w",
        ) as new_mail:
            new_mail.write(personalized_letter)
