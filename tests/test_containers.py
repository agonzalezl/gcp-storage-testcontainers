import os
from google.cloud import storage
from gcp_storage_testcontainers.containers import OittaaStorageEmulatorContainer
from google.auth.credentials import AnonymousCredentials


def test_basic():
    with OittaaStorageEmulatorContainer() as emulator:
        host_ip = emulator.get_container_host_ip()
        url = f"http://{host_ip}:{emulator.get_exposed_port(emulator.port)}"
        os.environ["STORAGE_EMULATOR_HOST"] = url
        client = storage.Client(
            credentials=AnonymousCredentials(),
            project="test",
        )

        bucket = client.bucket("hello")
        bucket = client.create_bucket(bucket)
        blob = bucket.blob("blob1")
        blob.upload_from_string("test1")
        blob = bucket.blob("blob2")
        blob.upload_from_string("test2")

        contents = []
        for blob in bucket.list_blobs():
            content = blob.download_as_bytes()
            contents.append(content)

        assert contents == [b"test1", b"test2"]
