from locust import task, HttpUser, User, constant, between, constant_pacing
import time

class AnyUser(User):

    # wait_time = constant(1)
    # wait_time = between(2,3)
    wait_time = constant_pacing(3)

    @task
    def launch(self):
        # print("Injected 1 second delay")
        # print("Injected 2 to 3 second delay")
        time.sleep(5)
        print("Injected constant pacing seconds delay")
