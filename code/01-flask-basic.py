from flask import Flask, render_template

# Flask 메인 객체 생성
# -> __name__은 이 소스파일의 이름
app = Flask(__name__)

@app.route("/hello")
def hello():
    html = """Hello Flask~!!
            This is Flask Webpage :
            <p style='color:blue'><a href="/world">들여쓰기 페이지</a></p>
            <p style='color:blue'><a href="/myfood">템플릿 예시 페이지</a></p>"""
    return html

@app.route("/world")
def world():
    html = """<h1>안녕 플라스크~!!</h1>
            <p style='color:blue'>첫 번째 플라스크 웹 페이지</p>
            <p style='color:red'><a href="/hello">두 번째 플라스크 웹 페이지</a></p>
            <p style='color:blue'><a href="/myfood">템플릿 예시 페이지</a></p>"""
    return html

@app.route("/myfood")
def myfood():
    return render_template("myfood.html")

@app.route("/mydata")
def mydata():
    mydict = {"name" : "Lee", "age": 24, "height": 175, "weight": 82}
    return mydict

if __name__ == "__main__":
    # 가동할 주소와 포트문호 지정 및 디버그 모드 활성화 -> 포트 기본 값 80
    # 디버그 모드 : 프로그램의 실행 과정을 개발자가 파악할 수 있도록 상세하게 출력
    app.run(port=9091, debug=True)