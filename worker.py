import time

def background_task(n):

    delay = 2

    print("Task running")
    print(f"Simulating {delay} second delay")

    time.sleep(delay)

    print(len(n))
    print("Task completed")

    return len(n)

if __name__ == "__main__":
    background_task("hello")