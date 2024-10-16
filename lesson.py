def lesson():
    fruits = ['apple', 'banana', 'cherry']

    def make_pie(index):
        try:
            fruit = fruits[index]
        except IndexError:
            print("Fruit pie")
        else:
            print(fruit + " pie")

    make_pie(2)
    # make_pie(4)
