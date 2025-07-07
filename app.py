from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ Render에 Flask 서버 배포 성공!"
