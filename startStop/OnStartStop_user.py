from locust import task, User, constant

class GtmTest(User):
    wait_time = constant(1)

    def on_start(self):
        # return super().on_start()
        print("starting")
    
    @task
    def task_hai_ji(self):
        print("This is Gautam 's task baby!")
    
    def on_stop(self):
        # return super().on_stop()
        print("on stop")