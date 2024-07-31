from __future__ import annotations

from http import HTTPStatus

import settings
import setup
from locust import TaskSet, between, task


class HealthCek(TaskSet):
    # Time period between firing consecutive tasks is 1-3 seconds
    wait_time = between(1, 3)

    def on_start(self) -> None:
        """Logins or start stuff before starting a user session."""
        setup.start()

    @task
    def cek_1(self) -> None:
        url = "/"
        with self.client.get(
            url,
            catch_response=True,
        ) as response:
            if response.status_code == HTTPStatus.OK:
                response.success()
            else:
                response.failure(f"Failed! Http Code `{response.status_code}`")

                
    @task
    def stop(self) -> None:
        """TaskSet objects don't know when to hand over control
        to the parent class. This method does exactly that."""
        self.interrupt()

    def on_stop(self) -> None:
        """Logout or stop stuff after ending a user session."""
        setup.stop()
