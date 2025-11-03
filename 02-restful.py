from flask import Flask, request

app = Flask(__name__)

@app.route("/parameter", methods=['GET'])
def get():
    #URL에 포함된 변수 추출
    my_num1 = request.args.get('num1')
    my_num2 = request.args.get('num2')

    #클라이언트로부터 받은 파라미터는 문자열임
    sum1 = my_num1 + my_num2

    sum2 = int(my_num1) + int(my_num2)

    mydict = {
        "expr": "%s + %s" %(my_num1, my_num2),
        "sum1": sum1,
        "sum2": sum2
    }
    return mydict

@app.route("/parameter", methods=['POST'])
def post():
    x = request.form.get("x")
    y = request.form.get("y")

    z = int(x) * int(y)

    return {
        "expr": "%s * %s" % (x,y),
        "z": z
   }

@app.route("/parameter", methods=['PUT'])
def post():
    a = request.form.get("a")
    b = request.form.get("b")

    c = int(a) - int(b)

    return {
        "expr": "%s - %s" % (a,b),
        "c": c
    }

@app.route("/parameter", methods=['DELETE'])
def post():
    m = request.form.get("m")
    n = request.form.get("n")

    o = int(m) / int(n)

    return {
        "expr": "%s / %s" % (m,n),
        "o": o
    }

@app.route("/parameter/<myname>/<myage>", methods=['GET'])
def path_params(myname,myage):
    msg = "안녕하세요 {name}님. 당신은 {age}세 입니다."

    return {
        "msg": msg.format(name=myname, age=myage)
    }

@app.errorhandler(Exception)
def error_handling(error):
    #에러 내용과 상태코드를 튜플 형식으로 반환한다.
    # -> 500은 웹 서버에서 에러가 발생했음을 클라이언트에 알리는 코드 값
    return ({'message': str(error)},500)

if __name__ == "__main__":
    app.run(port=9091, debug=True)