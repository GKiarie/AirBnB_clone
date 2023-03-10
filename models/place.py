#!/usr/bin/env python3
"""class Place inheriting from BaseModel
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """class Place which inherits from BaseModel
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    max_guests = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
