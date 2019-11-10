from dataclasses import dataclass


@dataclass
class Flight:
    duration: str
    carrier_code: str
    carrier_number: int
    aircraft: str
    gate: int
    departure: dict
    arrival: dict


@dataclass
class Airport:
    code: str
    name: str
    city: str
    country: str
    continent: str
    latitude: float
    longitude: float


@dataclass
class Weather:
    temperature: float
    description: str
