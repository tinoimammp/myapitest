from __future__ import annotations

from http import HTTPStatus

import setup
from locust import TaskSet, between, task


class APITasks(TaskSet):
    # Time period between firing consecutive tasks is 1-3 seconds
    wait_time = between(1, 3)

    def on_start(self) -> None:
        """Logins or setup before starting a user session."""
        setup.start()

    #Homepage get all this api
    #Test case is when people access homepage
    @task
    def task_1(self) -> None:
        urls = [
            "/topik",
            "/menus",
            "/categories?type=Konten",
            "/topik?is_populer=1&perPage=8",
            "/contents?perPage=5&featured=1",
            "/contents?perPage=4&is_populer=1",
            "/card_items/list_by_parent/layanan-masa-depan-digital",
            "/general_config",
            "/card_items/list_by_parent/transformasi-digital",
            "/card_items/list_by_parent/pencapaian-infrastruktur-digital",
            "/contents?perPage=8&is_tematik=1",
            "/contents?perPage=12&topik_ids=",
            "/magazines?perPage=3",
            "/contents/category/berita-hoaks?perPage=4&page=1",
            "/contents?is_gpr=1&perPage=20",
            "/statistik_aduan?year=2024",
            "/banner",
            "/contacts",
            "/card_items/list_by_parent/sosial-media",
            "/card_items/list_by_parent/footer",
            "/card_items/list_by_parent/pencapaian-pemerintahan-digital",
            "/statistik_aduan?year=2024&month=7",
            "/card_items/list_by_parent/layanan-sertifikasi",
            "/card_items/list_by_parent/beasiswa",
            "/program_kerja?perPage=6",
            "/card_items/list_by_parent/layanan-perizinan",
            "/tags?is_populer=1&perPage=8"
        ]

        for url in urls:
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
        """Logout and cleanup after ending a user session."""
        setup.stop()