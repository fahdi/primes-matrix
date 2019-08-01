def get_fabonacci(total):
    fibonacci_numbers = [1, 1]
    for i in range(2, 700):
        fibonacci_numbers.append(fibonacci_numbers[i - 1] + fibonacci_numbers[i - 2])
        if len(fibonacci_numbers) >= total:
            break
    return fibonacci_numbers

print(get_fabonacci(9))
