from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home(): return "Flask Backend is Running!"

@app.route('/margin', methods=['POST'])
def margin():
    data = request.json
    total = int(data.get("conducted", 0))
    absent = int(data.get("absent", 0))
    present = total - absent

    if present / total < 0.75:
        req = 3 * absent - present
        result = "Required: {} hours".format(ceil(req))
    else:
        margin = present / 3 - absent
        result = "Margin: {} hours".format(int(margin))
    
    return jsonify({"result": result})

def ceil(x: float):
    if x*10%10 >= 5: return int(x) + 1
    else: return int(x)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True)