from flask import Flask, request
import redis
from rq import Queue
from worker import background_task

app = Flask(__name__)


r = redis.Redis(host='my_redis_service', port=6379, decode_responses=True)
q = Queue('kwrun_queue',connection=r)
#q = Queue(connection=r)

@app.route("/task")
def add_task():

    if request.args.get("n"):
        n = request.args.get("n")
        print(n)
        job = q.enqueue(background_task, n)

        q_len = len(q)
        return f"Task {job.id} added to background at {job.enqueued_at}. {q_len} task in the  queue"

    return "No value for n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=22006, debug=True)

# rq worker --path /home/metin/codes/test3 kwrun_queue
# redis-server