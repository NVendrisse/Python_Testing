from locust import HttpUser, task


class serverPerformanceTest(HttpUser):

    @task
    def home(self):
        self.client.get("/")

    @task
    def login(self):
        self.client.post("/showSummary", {"email": "admin@irontemple.com"})

    @task
    def book(self):
        self.client.get("/book/Spring%20Festival/Simply%20Lift")

    @task
    def purchase(self):
        form_data = {
            "club": "Simply Lift",
            "competition": "Spring Festival",
            "places": "10",
        }
        self.client.post("/purchasePlaces", form_data)

    @task
    def logout(self):
        self.client.get("/logout")

    @task
    def point_display(self):
        self.client.get("/points-display")
