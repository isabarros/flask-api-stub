from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/reports/123/sent-to')
def hello():
  return jsonify({
    "sent-to": [
      {
        "email": "isadora@gmail.com"
      }
    ]
  })

if __name__ == '__main__':
  app.run(debug=True,host='0.0.0.0')
