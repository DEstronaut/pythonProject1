print('최대공약수 구하기.')
first_num = int(input('첫번째 숫자를 입력하세요:'))
second_num = int(input('두번째 숫자를 입력하세요:'))
remainder1 = first_num % second_num
print(remainder1)
i = 0
while remainder1 > 0: ##while 값 어떻게 끊을까?
    remainder2 = second_num % remainder1
    if remainder1 == first_num:
        GCD = remainder1 % remainder2
        print(GCD)