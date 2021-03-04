import time
from locust import HttpUser, task, between


class QuickstartUser(HttpUser):
    wait_time = between(1, 2.5)

    @task
    def hello_world(self):
        self.client.get("rus/news/top-8-samykh-ozhidaemykh-novinok-fevralya")

    def on_start(self):
        pass
        # self.client.post("/login", json={"login": "Scorpeg", "pass": "ivan91"})
