import requests
import json

search = input("원하는 검색어를 입력하시오")

sub_list = ['ㄱ', 'ㄴ','ㄷ','ㄹ','ㅁ','ㅂ','ㅅ','ㅇ', 'ㅈ' ,'ㅊ','ㅋ','ㅌ','ㅍ','ㅁ']

## 파일 열기 모드 w: 새로 쓰기 a: 추가 하기 r: 읽기
## = f = open(f'{search}.txt', 'w', encoding='UTF-8')
with open(f'{search}.txt', 'w', encoding='UTF-8') as f:
    for sub in sub_list:
        keyword = search + '' + sub
        response = requests.get(f"https://ac.search.naver.com/nx/ac?q={keyword}&con=0&frm=nv&ans=2&r_format=json&r_enc=UTF-8&r_unicode=0&t_koreng=1&run=2&rev=4&q_enc=UTF-8&st=100&_callback=_jsonp_1")

        str_data = response.text.split("_jsonp_1(")[1][:-1]

        # str_data를 dic_data로 바꿈
        dic_data = json.loads(str_data)

        #dic_data['items'] 는 items키의 값 불러오기
        #print(dic_data['items'][0])

        # 리스트 한칸 없애기(3차원의 0번째 요소 가져오기)
        first_dic_data = dic_data['items'][0]

        for i in first_dic_data:
            savedata = i[0]
            f.write(str(savedata) + '\n')

    '''    with open(f'{search}.txt','w',encoding='UTF-8') as f:
            # 리스트 형식이므로 i변수에 반복문으로 하나씩 집어넣음
            for i in first_dic_data:
    
                # 각 요소에서 첫번째 인덱스만 가지고 옴
                
    
    '''