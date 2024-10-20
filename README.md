# Testcontainers for GCP Storage

Powered by [oittaa/gcp-storage-emulator](https://github.com/oittaa/gcp-storage-emulator)

## How to

```python

with OittaaStorageEmulatorContainer() as emulator:
    host_ip = emulator.get_container_host_ip()
    url = f"http://{host_ip}:{emulator.get_exposed_port(emulator.port)}"
    os.environ["STORAGE_EMULATOR_HOST"] = url
    client = storage.Client(
        credentials=AnonymousCredentials(),
        project="test",
    )

```