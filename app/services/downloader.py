import zipfile
import io
from pathlib import Path

from app.services.api_client import FilesApiClient


STORAGE_PATH = Path("storage/files")


class DownloaderService:


    def __init__(self):

        self.client = FilesApiClient()

        STORAGE_PATH.mkdir(
            parents=True,
            exist_ok=True
        )


    async def download_all(self):

        total = 0


        while True:

            names = await self.client.get_names()

            print("Получено файлов:", len(names))


            if not names:
                break


            # API разрешает максимум 3 файла

            for i in range(0, len(names), 3):

                batch = names[i:i+3]


                archive = await self.client.download_files(
                    batch
                )


                self.extract_archive(
                    archive
                )


                await self.client.mark_downloaded(
                    batch
                )


                total += len(batch)



        return total



    def extract_archive(self, content):

        archive = zipfile.ZipFile(
            io.BytesIO(content)
        )


        archive.extractall(
            STORAGE_PATH
        )