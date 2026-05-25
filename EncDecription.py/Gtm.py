from locust import HttpUser, constant, task

class MeinEncriptionTestClass(HttpUser):

    wait_time = constant(1)

    @task
    def my_first_kaam(self):
        self.client.get("/")
        print("Kaam ho gaya!")