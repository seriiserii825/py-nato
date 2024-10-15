import pandas

data = pandas.read_csv("nato.csv")
nato_dict = {row.letter:row.code for (_, row) in data.iterrows()}

user_input = input("Enter a word: ").upper()
if user_input != '':
    words = [nato_dict[item] for item in user_input]
    print(f"words: {words}")
