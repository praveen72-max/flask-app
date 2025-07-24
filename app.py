from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    return "Hi Praveen you've successfully created a CI/CD pipline Congratulations on doing your first devops project"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)