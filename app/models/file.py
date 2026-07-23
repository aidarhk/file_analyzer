from datetime import datetime

from sqlalchemy import DateTime, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base

class File(Base):

    __tablename__ = "files"


    id: Mapped[int] = mapped_column(
        primary_key=True
    )


    filename: Mapped[str] = mapped_column(
        String(255),
        unique=True
    )


    path: Mapped[str] = mapped_column(
        String(500)
    )


    downloaded_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )