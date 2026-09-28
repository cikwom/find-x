from sqlalchemy import String, Text, Date
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Item(Base):
    __tablename__ = "items"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(Text)

    category: Mapped[str] = mapped_column(String(50))
    location: Mapped[str] = mapped_column(String(100))

    date_reported: Mapped[Date] = mapped_column(Date)

    item_type: Mapped[str] = mapped_column(String(10))
    status: Mapped[str] = mapped_column(String(20), default="active")