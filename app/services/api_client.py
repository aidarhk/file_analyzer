import os

import httpx
from dotenv import load_dotenv


load_dotenv()


class FilesApiClient:
    def __init__(self):
        self.base_url = os.getenv("EXTERNAL_API_URL")

        self.headers = {
            "X-Candidate-Id": os.getenv("CANDIDATE_ID")
        }


    async def get_names(self):
        async with httpx.AsyncClient() as client:

            response = await client.get(
                f"{self.base_url}/api/files/names",
                headers=self.headers
            )

            response.raise_for_status()

            data = response.json()

            print(data)

            return data["file_names"]


    async def download_files(self, filenames):
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/api/files/download",
                headers=self.headers,
                json={
                    "file_names": filenames
                }
            )

            print(response.status_code)

            response.raise_for_status()

            return response.content


    async def mark_downloaded(self, filenames):
        async with httpx.AsyncClient() as client:

            response = await client.post(
                f"{self.base_url}/api/files/downloaded",
                headers=self.headers,
                json={
                    "file_names": filenames
                }
            )

            print("STATUS:", response.status_code)
            print("RESPONSE:", response.text)

            response.raise_for_status()

            return response.json()