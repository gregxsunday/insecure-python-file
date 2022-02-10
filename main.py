from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def hello():
  filename = request.args.get('filename', default=None)
  file_path = os.path.join("var", "lib", filename)
  return 'ok'

if __name__ == "__main__":
    app.run('127.0.0.1', '8888')
