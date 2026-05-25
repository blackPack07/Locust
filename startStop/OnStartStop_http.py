from locust import task, HttpUser, constant, SequentialTaskSet

class GtmSequentialClass(SequentialTaskSet):

    def on_start(self):
        self.client.get("/", name=self.on_start.__name__)
    
    @task
    def browse_product(self):
        self.client.get("/product/OLJCESPC7Z", name=self.browse_product.__name__)
        print("Browse Product")

    @task
    def cart_page(self):
        self.client.get("/cart", name=self.browse_product.__name__)
        print("Cart Page")

    def on_stop(self):
        self.client.get("/", name=self.on_stop.__name__)
        print("Stop")

class LoadTest(HttpUser):
    host = "https://onlineboutique.dev"
    tasks = [GtmSequentialClass]
    wait_time = constant(1)

    