# generated by datamodel-codegen:
#   filename:  storage.json

from __future__ import annotations

from typing import Dict

from pydantic import BaseModel
from pydantic import Extra


class LongFundingRate(BaseModel):
    class Config:
        extra = Extra.forbid

    direction: str
    value: str


class Positions(BaseModel):
    class Config:
        extra = Extra.forbid

    collateral_amount: str
    entry_price: str
    funding_amount: str
    position: str
    position_value: str
    vUSD_amount: str


class ShortFundingRate(BaseModel):
    class Config:
        extra = Extra.forbid

    direction: str
    value: str


class Vmm(BaseModel):
    class Config:
        extra = Extra.forbid

    invariant: str
    token_amount: str
    vUSD_amount: str


class ZenithStorage(BaseModel):
    class Config:
        extra = Extra.forbid

    administrator: str
    current_index_price: str
    current_mark_price: str
    decimal: str
    fees_collected: str
    funding_period: str
    long_funding_rate: LongFundingRate
    metadata: Dict[str, str]
    oracle_address: str
    paused: bool
    positions: Dict[str, Positions]
    previous_funding_time: str
    short_funding_rate: ShortFundingRate
    total_long: str
    total_short: str
    transaction_fees: str
    upcoming_funding_time: str
    vUSD_contract_address: str
    vmm: Vmm
