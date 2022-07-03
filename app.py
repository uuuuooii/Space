from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.ziyis.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/space", methods=["POST"])
def web_space_post():
    name_receive = request.form['name_give']
    person_receive = request.form['person_give']
    place_receive = request.form['place_give']
    
    doc = {
        'name': name_receive,
        'person' : person_receive,
        'place' : place_receive
    }
    db.space.insert_one(doc)
    
    return jsonify({'msg': '주문 완료!'})

@app.route("/space", methods=["GET"])
def web_space_get():
    order_list = list(db.space.find({},{'_id':False}))
    return jsonify({ 'orders': order_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=8000, debug=True)