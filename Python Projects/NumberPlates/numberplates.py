PLATE_LENGTH = 7
MEMORY_TAG_BANNED = "IQZ"
RANDOM_LETTERS_BANNED = "IQ"

# --- One plate ---
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
