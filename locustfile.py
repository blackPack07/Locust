from locust import HttpUser, task, between

class HelloWorldGautam(HttpUser):
    wait_time = between(1,4)
    # def print_hello(self):
    #     self.client.get("https://chromewebstore.google.com/?hl=en")
    
    @task
    def say_hello(self):
        self.client.get("/")