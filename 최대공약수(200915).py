print('최대공약수 구하기.')
first_num = int(input('첫번째 숫자를 입력하세요:'))
second_num = int(input('두번째 숫자를 입력하세요:'))

remainder = first_num % second_num
i = 0
while remainder != 0:
    i += 1

    first_num = second_num
    second_num = remainder
    print(first_num, '/', second_num, '=', remainder)

    remainder = first_num % second_num
    print(second_num)


# remainder = first_num % second_num
# while remainder != 0:
#     first_num = second_num
#     second_num = remainder
#     remainder1 = second_num % remainder
#     if remainder1 == 0:
#         remainder1 = second_num % remainder
#         print('GCD =', remainder)