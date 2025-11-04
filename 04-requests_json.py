import requests

#세션 객체 생성
with requests.Session() as session:
    #세션 객체에 웹 브라우저 정보 주입
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    })

    url = "https://data.hossam.kr/py/sample.json"
    r = session.get(url)

    # HTTP 상태 값이 200이 아닌 경우는 강제로 에러를 발생시켜서 코드의 진행을 중단

    if r.status_code !=200:
        msg = "[%d Error] %s 에러가 발생함" %(r.status_code, r.reason)
        raise Exception(msg)
    
    print(r)

# JSON 형식의 응답 결과를 딕셔너리로 반환한다.
my_dict = r.json()
print(my_dict)

print(my_dict["name"])
print(my_dict["type"])
print(my_dict["img"])