from locust import task, SequentialTaskSet, constant, HttpUser

class GtmRvScript(SequentialTaskSet):

    @task
    def xml_chahiye(self):
        result = self.client.get("/xml", name="XML")
        print(result)
    
    @task
    def ich_brauchen_json(self):
        expected_response = "Wake up to WonderWidgets!"

        with self.client.get("/json", catch_response=True, name="JSON") as response:
            result = True if expected_response in response.text else False
            print(self.ich_brauchen_json.__name__, result)
            response.success()
    
    @task
    def get_robots(self):
        expected_response = "*"
        result = "Fail"
        with self.client.get("/robots.txt", catch_response=True, name="Robots") as response:
            if expected_response in response.text:
                result = "Success"
                response.failure("Not a failure")  # Marking this success request intentional failure
        print(self.get_robots.__name__, result)

    @task
    def mein_failure_example(self):
        expected_response = 404
        with self.client.get("/status/404", catch_response=True, name="HTTP 404") as response:
            if response.status_code == expected_response:
                response.failure("Got 404!")
            else:
                response.success()

class MyLoadTest(HttpUser):
    host = "https://httpbin.org"
    wait_time = constant(1)
    tasks = [GtmRvScript]