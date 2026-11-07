number1 = input("첫 번째 숫자를 입력해주세요")
number2 = input("두 번째 숫자를 입력해주세요")
op =  input("연산기호를 입력해주세요")
if number1.isdigit() and number2.isdigit():
    if op == "+":
        print(int(number1) + int(number2))
    elif op == "-":
        print(int(number1) - int(number2))
    elif op == "*":
        print(int(number1) * int(number2))
    elif op == "/":
        print(int(number1) / int(number2))
    else:
        print("잘못된 입력입니다")
else:
    print("잘못된 입력입니다")
