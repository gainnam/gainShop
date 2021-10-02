from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('mongodb://test:test@localhost', 27017)
# client = MongoClient('localhost', 27017)
db = client.dbhomework


## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index.html')


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
    # 이름, 수량, 주소, 번호
    name_receive = request.form['name_give']
    quantity_receive = request.form['quantity_give']
    adres_receive = request.form['adres_give']
    number_receive = request.form['number_give']

    doc = {
        'name': name_receive,
        'quantity': quantity_receive,
        'adres': adres_receive,
        'number': number_receive
    }
    db.orderList.insert_one(doc)

    return jsonify({'msg': '주문이 완료되었습니다!'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
    orderList = list(db.orderList.find({}, {'_id': False}))
    return jsonify({'all_orders': orderList})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
