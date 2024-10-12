numbers = []

while True:
    user_input = input("Введите число (или 'end' для завершения): ")
    
    if user_input.lower() == 'end':
        break  

    if user_input.isdigit() or (user_input[0] == '-' and user_input[1:].isdigit()):
        number = int(user_input)
        numbers.append(number)
    else:
        print("Пожалуйста, введите корректное число или 'end' для завершения.")

even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Количество четных чисел:", even_count)
print("Количество нечетных чисел:", odd_count)
