# This snippet converts a dna sequence to an RNA sequence
# Remember to change user_name to the user name on your computer
# A simple way to check your user name is to right click on your file go to properties, and look at the name after Users

file_name = r"C:\Users\user_name\Desktop\epigenetics_file_1.txt"

def read_file(file_name):
    with open(file_name, 'r') as file:
        content = file.readlines()
        sequence = "".join([line.strip() for line in content if not line.startswith('>')])
    return sequence

sequence = read_file(file_name)

transcription = sequence.replace("T", "U")

print(transcription)
