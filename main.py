import pandas

data = pandas.read_csv("nato.csv")
nato_dict = {row.letter:row.code for (_, row) in data.iterrows()}
print(f"nato_dict: {nato_dict}")

def generate_phonetic():
    user_input = input("Enter a word: ").upper()
    if user_input != '':
        try:
            words = [nato_dict[item] for item in user_input]
        except KeyError as error_message:
            print("Please enter only letters")
            generate_phonetic()
        else:
            print(f"words: {words}")

generate_phonetic()

# from lesson import lesson
# lesson()
