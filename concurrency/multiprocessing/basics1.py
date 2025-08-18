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

