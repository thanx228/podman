from flask import Flask
import os
app = Flask(__name__)

@app.route('/')
def hello():
    with open("/data/message", "w") as f:
        f.write(os.getenv("PODMAN_MSG"))
    return "done"

if __name__ == '__main__':
	app.run(host='0.0.0.0')
