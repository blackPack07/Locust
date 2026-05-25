from locust import task, HttpUser, constant, SequentialTaskSet

class MySequentialTasks(SequentialTaskSet):

    @task
    def first_task(self):
        self.client.get("/get")
        print("Get status for 200")
    
    @task
    def second_task(self):
        self.client.get("/500")
        print("Get status for 500")


class MyMainTest(HttpUser):

    host = "https://http.cat"
    tasks = [MySequentialTasks]
    wait_time = constant(1)