def get_fabonacci(total):
    if total == 0:
        return None
    if total == 1:
        return [1]
    if total == 2:
        return [1,1]

    fibonacci_numbers = [1,1]
    for i in range(2, 700):
        fibonacci_numbers.append(fibonacci_numbers[i - 1] + fibonacci_numbers[i - 2])
        if len(fibonacci_numbers) >= total:
            break

    return fibonacci_numbers


