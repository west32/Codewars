#
#
# # def fibonnaci_numbers():
# #     number = int(input("how many Fibonnacci numbers you want me to generate? "))
# #     numbers=[]
# #     if number == 1:
# #         numbers = [1]
# #     elif number == 2:
# #         numbers=[1,1]
# #     elif number > 2:
# #         numbers=[1,1]
# #         while len(numbers) != number:
# #             new_number= numbers[-1] + numbers [-2]
# #             numbers.append(new_number)
# #     return print(numbers)
#
# # fibonnaci_numbers()
#
# # def fibonacci(n):
# #
# #     if n <= 1:
# #         return n
# #     else:
# #         print(f"{(n-1)}+{(n-2)}= {(n-1)+(n-2)}")
# #         return fibonacci(n-1)+fibonacci(n-2)
# #
# # print(fibonacci(10))
#
# fib(4) = fib(3)+fib(2) = (fib(2)+fib(1))
# fib(3) = fib(2)+fib(1) = (fib(1)+fib(0))
# fib(0) = 0
# fib(1) = 1
# fib(2) = fib(1) + fib(0)
# fib(3) = fib(2) + fib(1) =(fib(1) + fib(0)) + fib(1)
# fib(4) fib(3) + fib(2) = (fib(2) + fib(1)) + (fib(1) + fib(0)) = ((fib(1) + fib(0)+fib(1)))  +  (fib(1) + fib(0))


# print(type(15904003580097631118647021768+
# 56332092792582356848149566193))

lista=[0,0,1,2,3,1,2,3,1,3,2,1,1]
print(lista)
lista.reverse()
print(lista)
strlist=""
for element in lista:
    strlist+=(str(element))

print(strlist)