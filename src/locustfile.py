from __future__ import annotations

import logging
from typing import Any

from locust import HttpUser, events
from locustfiles.tasklist import APITasks
from locustfiles.healthcek import HealthCek

class PrimaryUser(HttpUser):
    tasks =  (APITasks, HealthCek)


@events.quitting.add_listener
def _(environment, **_: Any) -> None:
    print(type(environment))
    if environment.stats.total.fail_ratio > 0:
        logging.error("Test failed due to failure ratio > 1%")
        environment.process_exit_code = 1
