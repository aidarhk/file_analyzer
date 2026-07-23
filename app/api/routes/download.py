from fastapi import APIRouter

from app.services.downloader import DownloaderService


router = APIRouter(
    prefix="/download",
    tags=["Download"]
)



@router.post("/start")
async def start_download():

    service = DownloaderService()


    count = await service.download_all()


    return {
        "downloaded": count
    }