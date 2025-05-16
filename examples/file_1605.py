# f-строки

# Десятичное число

name = 'Алиса'
age = 18

print("Меня зовут %s! Мне %d лет" % (name, age))

# ---

name = "Алиса"
age = 18

message = "Привет, меня зовут {} и мне {} лет.".format(name, age)
print(message)

message = "Привет, меня зовут {} и мне {} лет.".format(age, name, )
print(message)

# --- Позиционные аргументы

name = "Алиса"
age = 18
message = "Привет, меня зовут {1} и мне {0} лет.".format(age, name)
print(message)  # 'Привет, меня зовут 18 и мне Алиса лет.'

# Важно, если индекс не существует получите ошибку IndexError
# message_2 = "Привет, меня зовут {1} и мне {4} лет.".format(age, name)
# print(message)  # IndexError: Replacement index 4 out of range for positional args tuple

# --- Наименованные аргументы

message = "Меня зовут {name} и мне {age} лет.".format(name="Алиса", age=18)
print(message)  # Меня зовут Алиса и мне 18 лет.

message_2 = "Меня зовут {age} и мне {name} лет.".format(name="Алиса", age=18)
print(message_2)  # Меня зовут 18 и мне Алиса лет.

# ---

reciept = "Чек"

print(reciept.center(10))  # 10 - 3 = 7 ' '
print(reciept.center(10, '-'))  # 10 - 3 = 7 ' '
print(reciept.center(3))
print(reciept.center(35, "="))

word = 'Python'
print(word.ljust(10))  # 'Python    '
print(word.ljust(10, '-'))  # 'Python----'

print(word.rjust(10))  # '    Python'
print(word.rjust(10, '-'))  # '----Python'

# center - ^
# right - >
# left - <

print(f"{reciept:^10}")
print(f"{reciept:-^10}")

print(f"{word:>10}")
print(f"{word:->10}")
print(f"{word:<10}")
print(f"{word:-<10}")

h = '11'
m = '5'

print(f"{h}:{m:0>2}")
