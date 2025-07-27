import time
from multiprocessing import Process


def work(name):
    print(f"{name} starting...")
    time.sleep(1)
    print(f"{name} done.")


if __name__ == "__main__":
    p1 = Process(target=work, args=("P1",))
    p2 = Process(target=work, args=("P2",))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("Both processes completed")


@app.route("/health/live")
def liveness():
    return "I'm alive!", 200

@app.route("/health/ready")
def readiness():
    if not db.is_connected():
        return "DB not ready", 500
    if not cache.is_available():
        return "Cache not ready", 500
    return "Ready", 200

@app.route("/health/startup")
def startup():
    if not app.startup_complete:
        return "Still starting", 500
    return "Started", 200
