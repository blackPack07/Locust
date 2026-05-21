from locust import HttpUser, constant, task

class MyReqResScript(HttpUser):

    host = "https://reqres.in"
    wait_time = constant(1)

    @task
    def get_users(self):
        self.client.get("/api/users")
    

    @task
    def create_user(self):
        self.client.post()