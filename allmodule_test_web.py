from allmodule_web import *

#오늘 일기 끝! 입력시 종료

def diary(input_data):
# end = 1
# while end == 1 :
    # sentence = input("하고싶은 말을 입력해주세요 : ")
    # if sentence == "오늘 일기 끝!" :
        # break
    # sentence = input_data
    result = predict(input_data)
    return result

    # print(predict.result)
    # print("\n")


# diary