from locust import task, HttpUser, constant

class MyLoadTest(HttpUser):

    wait_time = constant(1)

    @task
    def launch_kro_bhai(self):
        self.client.get("/")
    