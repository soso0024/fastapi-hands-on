from typing import Optional

from pydantic import BaseModel, Field


class Task(BaseModel):
    id: int
    title: Optional[str] = Field(None, title="クリーニングを取りに行く")
    done: bool = Field(False, title="完了フラグ")
