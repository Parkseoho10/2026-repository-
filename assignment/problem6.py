password = ("python123")
a = input("비밀번호를 입력하세요")
while a != password:
    a = input("비밀번호가 틀렸습니다. 다시 입력하세요.")
    if a == password:
        print("로그인 성공! 환영합니다.")


