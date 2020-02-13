from shapely.geometry import Point, shape

from domain.observation import Observation

polygon_norway = {
    "type": "Polygon",
    "coordinates": [
        [
            [
                0.87890625,
                56.65622649350222
            ],
            [
                31.46484375,
                56.65622649350222
            ],
            [
                31.46484375,
                73.52839948765174
            ],
            [
                0.87890625,
                73.52839948765174
            ],
            [
                0.87890625,
                56.65622649350222
            ]
        ]
    ]
}


def validate_observation(obs: Observation):
    valid_region = shape(polygon_norway)
    point = Point(obs.location.long, obs.location.lat)
    return {
        "location_valid": valid_region.contains(point)
    }
