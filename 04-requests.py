import requests

#세션 객체 생성
with requests.Session() as session:
    #세션 객체에 웹 브라우저 정보 주입
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    })

    url = "https://data.hossam.kr/py/sample.txt"
    r = session.get(url)

    # HTTP 상태 값이 200이 아닌 경우는 강제로 에러를 발생시켜서 코드의 진행을 중단

    if r.status_code !=200:
        msg = "[%d Error] %s 에러가 발생함" %(r.status_code, r.reason)
        raise Exception(msg)
    
    print(r)

# 수신된 데이터의 인코딩 설정( 한글이 깨지면 euc-kr로 변경 )

r.encoding = "utf-8"

#수신된 결과 확인 --> 웹에서 가져온 모든 데이터는 문자열임
print(r.text)