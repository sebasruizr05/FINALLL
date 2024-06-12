from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def submit_form(self):
        form_data = {
            "name": "John Doe",
            "email": "john@example.com",
            "message": "Hello, this is a test message!"
        }
        headers = {"Content-Type": "application/json"}
        response = self.client.post("/contact", json=form_data, headers=headers)
        assert response.status_code == 200, "Failed to submit form"
