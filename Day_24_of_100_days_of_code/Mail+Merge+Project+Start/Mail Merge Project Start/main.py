# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

sample_name = '[name]'
with open("./Input/Names/invited_names.txt") as invitees:
    names = invitees.readlines()

with open("./Input/Letters/starting_letter.txt") as sample_letter:
    letters = sample_letter.read()
    for name in names:
        new_name = name.strip()
        final_letter = letters.replace(sample_name, new_name)

        with open(f"./Output/ReadyToSend/individual_letter_for_{new_name}.txt", 'w') as ready_letter:
            ready_letter.write(final_letter)
