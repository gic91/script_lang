import threading

def update():
    t = threading.Timer(1, update)
    t.start()
    print("update")

update()