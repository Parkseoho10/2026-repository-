user_input = int(input("나이를 입력하세요"))
if user_input < 8:
    print("입장료는 무료입니다")
elif user_input <= 19:
    print("입장료는 10000원입니다")
elif 20<= user_input <=64:
    print(" 입장료는 20000원입니다")
else:
    print("입장료는 5000원입니다")
