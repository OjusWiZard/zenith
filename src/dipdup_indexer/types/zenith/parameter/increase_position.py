# generated by datamodel-codegen:
#   filename:  increasePosition.json

from __future__ import annotations

from pydantic import BaseModel
from pydantic import Extra


class IncreasePositionParameter(BaseModel):
    class Config:
        extra = Extra.forbid

    direction: str
    leverage_multiple: str
    vUSD_amount: str