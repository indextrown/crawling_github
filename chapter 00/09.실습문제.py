gudok = int(input("구독자 수를 입력하시오"))
if gudok >= 1000:    
    print("수익 창출이 가능합니다!")
elif gudok == "":
    print("아무것도 입력하지 않았습니다")
else:
    print("수익 창출이 불가능 합니다")