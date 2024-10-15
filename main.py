import random
# names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
#
# students_score = {item:random.randint(1, 100) for item in names}
# print(f"students_score: {students_score}")
# students_score = {key:value for key, value in students_score.items() if value > 60}
# print(f"students_score: {students_score}")


# sentence = 'What is the Airspeed Velocity of an Unladen Swallow'
# print(f"sentence: {sentence}")
#
# words = sentence.split(' ')
# print(f"words: {words}")
#
# result = {item:len(item) for item in words}
# print(f"result: {result}")

def celsToFar(t):
    return (t * 9/5) + 32


weather_c = {
        "Wednesday": 15,
        "Thursday": 14,
        "Friday": 21,
        "Saturday": 22,
        "Sunday": 24,
        }

weather_f = {key:celsToFar(value) for key,value in weather_c.items()}
print(f"weather_f: {weather_f}")
