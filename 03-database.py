from flask import Flask , request
from sqlalchemy import text
import datetime as dt
from mylibrary import MyDB

app = Flask(__name__)
app.json.sort_keys = False

# GET - 다중행 데이터 조회하기
@app.route("/departments", methods=['GET'])
def get_list():
    # 실행할 SQL문 정의
    sql = text("SELECT id, dname, loc, phone, email FROM departments")

    conn = MyDB.connect()
    result = conn.execute(sql)
    MyDB.disconnect()

    resultset = result.mappings().all()

    for i in range(0, len(resultset)):
        resultset[i] = dict(resultset[i])

    return {
        "result": resultset,
        "timestamp": dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

@app.route("/departments/<id>", methods=['GET'])
def get_item(id):
    #SQL문 정의
    sql = text("""SELECT id, dname, loc, phone, email, established, homepage
                FROM departments WHERE id=:id""")
    
    conn = MyDB.connect()                   #DB 접속 (MyDB의 connect 함수 실행)
    result = conn.execute(sql, {"id":id})   #SQL문을 실행하여 결과 객체 저장, sql문에서 변수로 사용한 것을 키로 사용
    MyDB.disconnect()                       #DB 접속 해제

    #단일행 조회에 대한 결과 집합 추출
    resultset=result.mappings().all()

    return {
        "result": dict(resultset[0]),        #조회 결과에 대한 딕셔너리 반환, 단일 행이므로 [0]으로 하드코딩
        "timestamp": dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

@app.route("/departments", methods=['POST'])
def post():
    #db 접속
    conn = MyDB.connect()
    # 1. 데이터 저장
    dname = request.form.get("dname")
    loc = request.form.get("loc")
    phone = request.form.get("phone")
    email = request.form.get("email")
    established = request.form.get("established")
    homepage = request.form.get("homepage")

    sql = text("""INSERT INTO departments (dname, loc, phone, email, established, homepage)
                VALUES (:dname, :loc, :phone, :email, :established, :homepage)""")

    #Post 파라미터를 SQL에 맵핑하기 위해 딕셔너리로 묶음
    params = {
        "dname": dname, "loc" : loc, "phone" : phone, "email": email,
        "established" : established, "homepage": homepage
    }

    conn.execute(sql,params)
    conn.commit()

    # 2. 데이터 저장 결과 조회
    pk_result = conn.execute(text("SELECT LAST_INSERT_ID()"))
    pk = pk_result.scalar()

    sql = text("""SELECT id, dname, loc, phone, email, established, homepage 
                FROM departments where id=:id""")
    
    result = conn.execute(sql, {"id" : pk}) #sql문을 실행하여 결과 객체 받기
    resultset = result.mappings().all()     #단일행 조회에 대한 결과 집합 추출

    # DB 접속 해제
    MyDB.disconnect()

    return {
        "result" : dict(resultset[0]),
        "timestamp": dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

# PUT - 데이터 수정하기 -> WHERE절에 사용할 PK값을 PATH 파라미터로 정의
@app.route("/departments/<id>", methods=['PUT'])
def put(id):
    # DB접속하기
    conn = MyDB.connect()

    dname = request.form.get("dname")
    loc = request.form.get("loc")
    phone = request.form.get("phone")
    email = request.form.get("email")
    established = request.form.get("established")
    homepage = request.form.get("homepage")

    sql = text("""UPDATE departments SET
               dname=:dname, loc=:loc, phone=:phone, email=:email, established=:established, homepage=:homepage
               WHERE id=:id""")
    
    # PUT 파라미터를 SQL에 맵핑하기 위해 딕셔너리로 묶음 -> WHERE절에 사용할 id값은 PATH 파라미터
    params ={
        "id":id, "dname":dname, "loc":loc, "phone":phone,
        "email":email, "established":established, "homepage":homepage
    }

    conn.execute(sql,params)
    conn.commit()

    sql = text("""SELECT id, dname, loc, phone, email, established, homepage
               FROM departments WHERE id=:id""")
    
    result = conn.execute(sql, {"id": id})

    resultset = result.mappings().all()

    MyDB.disconnect()

    return {
        "result": dict(resultset[0]),
        "timestamp": dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

@app.route("/departments/<id>", methods = ['DELETE'])
def delete(id):
    conn=MyDB.connect()

    sql1=text("""DELETE FROM enrollments
              WHERE subject_id IN(SELECT id FROM subjects WHERE department_id=:id)
              OR student_id IN(SELECT id FROM students WHERE department_id=:id)""")
    sql2 = text("DELETE FROM subjects WHERE department_id=:id")
    sql3 = text("DELETE FROM students WHERE department_id=:id")
    sql4 = text("DELETE FROM professors WHERE department_id=:id")
    sql5 = text("DELETE FROM departments WHERE id=:id")

    params = {"id": id}

    conn.execute(sql1, params)
    conn.execute(sql2, params)
    conn.execute(sql3, params)
    conn.execute(sql4, params)
    conn.execute(sql5, params)

    conn.commit()
    MyDB.disconnect()

    return {"timestamp": dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}


@app.errorhandler(Exception)
def error_handling(error):
    MyDB.disconnect()
    return {
        'message' : "".join(error.args),
        'timestamp' : dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }, 500

if __name__ == "__main__":
    app.run(host='127.0.0.1',port=9091,debug=True)