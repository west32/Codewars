# def number_to_string(num):
#     return str(num)

def decimalToBinary(n):
    return bin(n).replace("0b", "")


# Driver code
if __name__ == '__main__':
    print(decimalToBinary(8))
    print(decimalToBinary(18))
    print(decimalToBinary(7))