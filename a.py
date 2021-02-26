# 사람별 평균 구하기

def main():
    kor_score = [49, 79, 20, 100, 80]
    math_score = [43, 59, 85, 30, 90]
    eng_score = [42, 79, 48, 60, 100]
    midterm_score = [kor_score, math_score, eng_score]
    total_score = [0,0,0,0,0]
    index = 0

    for scores in midterm_score:
        for value in scores:            
            total_score[index] += value
            print(total_score)
            index += 1
        index = 0
    print(total_score)



    

        # avg = int(midterm_score[i][i] + midterm_score[i+1][i] + midterm_score[i+2][i])/3
        # if(i == 0):
        #     print("A의 평균은 : ", avg)
        # elif(i == 1):
        #     print("B의 평균은 : ", avg)
        # elif(i == 2):
        #     print("C의 평균은 : ", avg)
        # elif(i == 3):
        #     print("D의 평균은 : ", avg)
        # else:
        #     print("E의 평균은 : ", avg)


if __name__ == '__main__':
    main()
