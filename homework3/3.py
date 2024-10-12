numbers = []

while True:
    user_input = input("Введите число (или 'end' для завершения): ")
    if user_input.lower() == 'end':
        break
    try:
        number = int(user_input)
        numbers.append(number)
    except ValueError:
        print("Пожалуйста, введите корректное целое число.")

odd_numbers = [num for num in numbers if num % 2 != 0]
print("Нечетные числа в списке:", odd_numbers)
