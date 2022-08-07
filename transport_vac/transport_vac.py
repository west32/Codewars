def rental_car_cost(d):
    total = d * 40
    if 3 < d < 7:
        total -= 20
    elif d >= 7:
        total -= 50
    return total