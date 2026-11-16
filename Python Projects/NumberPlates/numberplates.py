import random
from datetime import date, datetime

PLATE_LENGTH = 7
MEMORY_TAG_BANNED = "IQZ"
RANDOM_LETTERS_BANNED = "IQ"

typed_plate = input("What is your vehicles registration? ")
tidied_plate = typed_plate.upper().replace(" ", "")

memory_tag = tidied_plate[0:2]
age_identifier = tidied_plate[2:4]
random_letters = tidied_plate[4:7]
print(f"Typed: {typed_plate}, Upper: {tidied_plate}, Memory Tag: {memory_tag}, Age Ident: {age_identifier}, Random Letters: {random_letters}")

valid_count = 0

def isValid(plate):
    if len(plate) != PLATE_LENGTH:
        return False

    memory_tag = plate[0:2]
    age_identifier = plate[2:4]
    random_letters = plate[4:7]

    if not memory_tag.isalpha():
        return False
    if not age_identifier.isdigit():
        return False
    if not random_letters.isalpha():
        return False

    return True

if isValid(tidied_plate):
    print(f"{tidied_plate}: valid")
else:
    print(f"{tidied_plate}: not valid")


# --- Make a random plate ---

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Ask until a real date between 1 September 2001 and today is typed
while True:
    typed_date = input("\nFirst registered (dd/mm/yyyy): ")
    try:
        registered = datetime.strptime(typed_date.strip(), "%d/%m/%Y").date()
    except ValueError:
        print("Please type a real date as dd/mm/yyyy.")
        continue
    if date(2001, 9, 1) <= registered <= date.today():
        break
    print("The date must be between 01/09/2001 and today.")

# Age identifier: Mar-Aug = year, Sep-Dec = year + 50, Jan-Feb = last September's code
if registered.month >= 9:
    code = registered.year - 2000 + 50
elif registered.month >= 3:
    code = registered.year - 2000
else:
    code = registered.year - 2000 - 1 + 50
age_identifier = f"{code:02d}"  # 2 becomes "02"

# Pick random letters, skipping any that are banned
memory_tag = ""
while len(memory_tag) < 2:
    letter = LETTERS[random.randint(0, 25)]
    if letter not in MEMORY_TAG_BANNED:
        memory_tag += letter

random_letters = ""
while len(random_letters) < 3:
    letter = LETTERS[random.randint(0, 25)]
    if letter not in RANDOM_LETTERS_BANNED:
        random_letters += letter

print(f"Age identifier: {age_identifier}")
print(f"Plate: {memory_tag}{age_identifier} {random_letters}")
