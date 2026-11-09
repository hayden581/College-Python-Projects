PLATE_LENGTH = 7
MEMORY_TAG_BANNED = "IQZ"      # letters never used in the memory tag
RANDOM_LETTERS_BANNED = "IQ"   # letters never used in the random letters

# --- One plate ---
typed_plate = input("What is your vehicles registration? ")      #what the staff member types, e.g. "ab51 cde"
tidied_plate = typed_plate.upper().replace(" ", "")      #typed_plate in uppercase with spaces removed, e.g. "AB51CDE"

memory_tag = tidied_plate[0:2]      #slice of tidied_plate, positions 0-1
age_identifier = tidied_plate[2:4]    #slice of tidied_plate, positions 2-3
random_letters = tidied_plate[4:7]    #slice of tidied_plate, positions 4-6

reasons = []           # each failed check appends its reason; empty list = valid

# --- STRETCH: the desk's plates ---
valid_count = 0        # goes up by 1 for each valid plate in desk
# total plates = the length of desk (no separate counter needed)

print(f"Typed: {typed_plate}, Upper: {tidied_plate}, Memory Tag: {memory_tag}, Age Ident: {age_identifier}, Random Letters: {random_letters}")