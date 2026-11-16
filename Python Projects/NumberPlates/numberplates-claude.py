from datetime import date

PLATE_LENGTH = 7
MEMORY_TAG_BANNED = "IQZ"
RANDOM_LETTERS_BANNED = "IQ"
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DIGITS = "0123456789"
FORMAT_START = date(2001, 9, 1)  # when this plate format began

# The plates waiting on the desk (Part 1 STRETCH)
desk = ["ab51 cde", "AB76 CDE", "ab5o cde", "qa51 cde", "ab51 cd3",
        "ab51 cdi", "ab50 cde", "abc", "AB99 CDE", "xy2i kfp"]


# --- Tidying ---

def tidy(typed_plate):
    """Uppercase, take out spaces, and read O as 0 / I as 1 in the age identifier only."""
    tidied_plate = typed_plate.upper().replace(" ", "")
    if len(tidied_plate) == PLATE_LENGTH:
        memory_tag = tidied_plate[0:2]
        age_identifier = tidied_plate[2:4].replace("O", "0").replace("I", "1")
        random_letters = tidied_plate[4:7]
        tidied_plate = memory_tag + age_identifier + random_letters
    return tidied_plate


def all_in(text, allowed):
    """True if every character of text is in allowed."""
    for character in text:
        if character not in allowed:
            return False
    return True


# --- What an age identifier means (Part 2 STRETCH) ---

def age_period(age_identifier):
    """Gives back the months an age identifier stands for, or 'Not a code'."""
    if len(age_identifier) != 2 or not all_in(age_identifier, DIGITS):
        return "Not a code"

    code = int(age_identifier)
    if code > 50:
        year = 2000 + code - 50
        first_day = date(year, 9, 1)
        period = f"September {year} to February {year + 1}"
    else:
        year = 2000 + code
        first_day = date(year, 3, 1)
        period = f"March {year} to August {year}"

    # Never issued: before the format began, or not reached yet
    if first_day < FORMAT_START or first_day > date.today():
        return "Not a code"
    return period


# --- The rules: each takes a tidied plate and gives back True or False ---

def right_length(plate):
    return len(plate) == PLATE_LENGTH


def memory_tag_is_letters(plate):
    memory_tag = plate[0:2]
    return all_in(memory_tag, LETTERS)


def age_identifier_is_digits(plate):
    age_identifier = plate[2:4]
    return all_in(age_identifier, DIGITS)


def age_identifier_issued(plate):
    age_identifier = plate[2:4]
    return age_period(age_identifier) != "Not a code"


def random_letters_are_letters(plate):
    random_letters = plate[4:7]
    return all_in(random_letters, LETTERS)


def letters_allowed(plate):
    memory_tag = plate[0:2]
    random_letters = plate[4:7]
    for letter in memory_tag:
        if letter in MEMORY_TAG_BANNED:
            return False
    for letter in random_letters:
        if letter in RANDOM_LETTERS_BANNED:
            return False
    return True


def isValid(plate):
    """True only when every rule is True."""
    return (right_length(plate)
            and memory_tag_is_letters(plate)
            and age_identifier_is_digits(plate)
            and age_identifier_issued(plate)
            and random_letters_are_letters(plate)
            and letters_allowed(plate))


def reasons(plate):
    """Gives back a list of every rule the plate fails."""
    failed = []

    # Wrong length: the parts mean nothing, so that is the only reason
    if not right_length(plate):
        failed.append(f"it has {len(plate)} characters, not {PLATE_LENGTH}")
        return failed

    memory_tag = plate[0:2]
    age_identifier = plate[2:4]
    random_letters = plate[4:7]

    if not memory_tag_is_letters(plate):
        failed.append(f"memory tag {memory_tag} must be two letters")
    if not age_identifier_is_digits(plate):
        failed.append(f"age identifier {age_identifier} must be two digits")
    elif not age_identifier_issued(plate):
        failed.append(f"age identifier {age_identifier} was never issued")
    if not random_letters_are_letters(plate):
        failed.append(f"random letters {random_letters} must be three letters")

    if not letters_allowed(plate):
        for letter in memory_tag:
            if letter in MEMORY_TAG_BANNED:
                failed.append(f"memory tag never uses {letter}")
        for letter in random_letters:
            if letter in RANDOM_LETTERS_BANNED:
                failed.append(f"random letters never use {letter}")

    return failed


# --- The procedure: tidies, then shows the verdict (prints, gives back nothing) ---

def show_verdict(typed_plate):
    tidied_plate = tidy(typed_plate)
    print(f"Tidied: {tidied_plate}")
    if isValid(tidied_plate):
        age_identifier = tidied_plate[2:4]
        print(f"{tidied_plate}: valid, first registered {age_period(age_identifier)}")
    else:
        print(f"{tidied_plate}: not valid")
        for reason in reasons(tidied_plate):
            print(f"  - {reason}")


# --- One plate ---
typed_plate = input("Plate: ")
show_verdict(typed_plate)

# --- The desk's plates ---
print("\nThe desk's plates:")
valid_count = 0
for typed_plate in desk:
    print(f"\nPlate: {typed_plate}")
    show_verdict(typed_plate)
    if isValid(tidy(typed_plate)):
        valid_count += 1

print(f"\n{valid_count} of {len(desk)} plates are valid")
