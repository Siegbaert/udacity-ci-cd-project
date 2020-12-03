from locust import HttpUser, TaskSet, task
import json


class MlPredictUser(HttpUser):
    @task
    def get_home(self):
        self.client.get("/")

    @task
    def post_predictions(self):
        self.client.post(
            "/predict",
            data=json.dumps(
                {
                    "CHAS": {"0": 0},
                    "RM": {"0": 6.575},
                    "TAX": {"0": 296.0},
                    "PTRATIO": {"0": 15.3},
                    "B": {"0": 396.9},
                    "LSTAT": {"0": 4.98},
                }
            ),
            headers={"Content-Type": "application/json"},
        )