from flask import Flask
import redis as rdis
import time as t

app = Flask(__name__)
r =rdis.StrictRedis(host="redis", port=6379, db=0)

@app.route("/")
def index():
    r.rpush("visits", t.time())
    count = r.llen("visits")
    if count == 1:
        return "You have accessed this Website {count} time".format(count=count)
    else:
        return "You have accessed this website {count} times".format(count=count)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
