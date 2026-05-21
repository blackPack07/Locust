from locust import HttpUser, SequentialTaskSet, task, constant
import logging
import re
import random


class PetStore(SequentialTaskSet):

    def __init__(self, parent):
        super().__init__(parent)
        self.jsession = ""
        self.random_product = ""

    @task
    def home_page(self):
        with self.client.get("/", catch_response=True, name="T00_HomePage") as response:
            if "Welcome to JPetStore 6" in response.text and response.elapsed.total_seconds() < 2.0:
                response.success()
                logging.info("Home Page load success")
            else:
                response.failure("Home page took too long to load and/or text check has failed.")
                logging.error("Home page didn't load successfully.")

    @task
    def enter_store(self):
        products = ['Fish', 'Dogs', 'Cats', 'Reptiles', 'Birds']
        with self.client.get("/actions/Catalog.action", catch_response=True, name="T10_EnterStore") as response:
            for product in products:
                if product in response.text:
                    response.success()
                else:
                    response.failure("Products check failed.")
                    break
            try:
                self.jsession = re.search(r"jsessionid=(.+?)\?", response.text)
                self.jsession = self.jsession.group(1)
            except AttributeError:
                self.jsession = ""

    @task
    def signin_page(self):
        self.client.cookies.clear()
        url = "/actions/Account.actionjsessionid=" + self.jsession + "?signonForm="
        with self.client.get(url, catch_response=True, name="T10_SignInPage") as response:
            if "Please enter your username and password" in response.text:
                response.success()
            else:
                response.failure("Signin page check failed.")

    @task
    def login(self):
        self.client.cookies.clear()
        url = "/actions/Account.action"
        data = {
            "username" : "j2ee",
            "password" : "j2ee",
            "signon"   : "Login"
        }
        with self.client.post(url, name="T30_SignInPage", data=data, catch_response=True) as response:
            if "Welcome ABC!" in response.text:
                response.success()
                try:
                    self.random_product = re.findall(r"Catalog.action\?viewCategory=&categoryId=(.+?)\"", response.text)
                    self.random_product = random.choice(self.random_product)
                except AttributeError:
                    self.random_product = ""
            else:
                response.failure("Signin failed.")

class LoadTest(HttpUser):
    host = "https://petstore.octoperf.com"
    wait_time = constant(1)
    tasks = [PetStore]