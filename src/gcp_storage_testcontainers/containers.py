from testcontainers.core.container import DockerContainer
from testcontainers.core.waiting_utils import wait_for_logs


class OittaaStorageEmulatorContainer(DockerContainer):
    def __init__(
        self,
        image: str = "oittaa/gcp-storage-emulator",
        port: int = 9023,
        **kwargs,
    ) -> None:
        super().__init__(image, **kwargs)
        self.port = port

        # The emulator server expects that the attacked port is the same as the exposed port
        # So, port docker port internal-external mappings are problematic
        self.with_bind_ports(self.port, self.port)
        self.with_env("PORT", self.port)

    def start(self, timeout: float = 60) -> "OittaaStorageEmulatorContainer":
        super().start()
        wait_for_logs(self, "All services started", timeout)
        return self
