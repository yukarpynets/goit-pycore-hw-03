import random


def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
  
    if min < 1 or max > 1000 or min > max:
        return []

    if quantity < 1 or quantity > max - min + 1:
        return []

    numbers = set()
    while len(numbers) < quantity:
        numbers.add(random.randint(min, max))

    return sorted(numbers)


if __name__ == "__main__":
    lottery_numbers = get_numbers_ticket(1, 49, 6)
    print("Ваші лотерейні числа:", lottery_numbers)

    print(get_numbers_ticket(0, 49, 6))    
    print(get_numbers_ticket(1, 2000, 6))  
    print(get_numbers_ticket(1, 5, 10))   