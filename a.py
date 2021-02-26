import random

# 1~ 100 임의의 숫자를 맞추시오

def main():
    ran_num = random.randint(1,100)
    input_num = int(input("숫자를 입력하세요."))

    while(input_num is not ran_num):
        if(input_num > ran_num):
            print("입력한 숫자가 큽니다.")
        else:
            print("입력한 숫자가 작습니다.")
        input_num = int(input())
    else: print("정답 입력한 숫자 ", input_num);





if __name__ == '__main__':
    main()
