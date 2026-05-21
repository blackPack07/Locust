from locust import TaskSet, constant, task, HttpUser
import random

class MeinHttpsCat(TaskSet):

    @task
    def get_status_code(self):
        self.client.get("/200")
        print("Get Status code of 200")
        self.interrupt(reschedule=False)

class AnotherHttpCat(TaskSet):
    @task
    def get_500_status(self):
        self.client.get("/500")
        print("Get response for 500 status code")
        self.interrupt(reschedule=False)
        # self.interrupt()

class MyLoadTest(HttpUser):
    host = "https://http.cat"
    tasks = [MeinHttpsCat, AnotherHttpCat]
    wait_time = constant(1)