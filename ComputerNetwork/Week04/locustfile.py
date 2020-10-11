import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(3, 5)

    @task
    def index_page(self):
        response = self.client.get("/")
        #print(response)
#    def on_start(self):
#        self.client.post("/", "ack".encode())
