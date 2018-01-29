# Standard Library Imports
from datetime import datetime
# 3rd Party Imports
# Local Imports
from PokeAlarm import Unknown
from . import BaseEvent
from PokeAlarm.Utils import get_gmaps_link, get_applemaps_link, \
    get_time_as_str, get_move_damage, get_move_dps, \
    get_move_duration, get_move_energy, get_seconds_remaining, \
    get_dist_as_str, get_pokemon_cp_range, is_weather_boosted, \
    get_base_types, get_weather_emoji, get_type_emoji


class RaidEvent(BaseEvent):
    """ Event representing the discovery of a Raid. """

    def __init__(self, data):
        """ Creates a new Stop Event based on the given dict. """
        super(RaidEvent, self).__init__('raid')
        check_for_none = BaseEvent.check_for_none

        # Identification
        self.gym_id = data.get('gym_id')

        # Time Remaining
        self.raid_end = datetime.utcfromtimestamp(
            data.get('end') or data.get('raid_end'))  # RM or Monocle
        self.time_left = get_seconds_remaining(self.raid_end)

        # Location
        self.lat = float(data['latitude'])
        self.lng = float(data['longitude'])
        self.distance = Unknown.SMALL  # Completed by Manager
        self.direction = Unknown.TINY  # Completed by Manager
        self.weather_id = check_for_none(
            int, data.get('weather'), Unknown.TINY)

        # Monster Info
        self.raid_lvl = int(data['level'])
        self.mon_id = int(data['pokemon_id'])
        self.cp = int(data['cp'])
        self.types = get_base_types(self.mon_id)

        # Quick Move
        self.quick_id = check_for_none(int, data.get('move_1'), Unknown.TINY)
        self.quick_damage = get_move_damage(self.quick_id)
        self.quick_dps = get_move_dps(self.quick_id)
        self.quick_duration = get_move_duration(self.quick_id)
        self.quick_energy = get_move_energy(self.quick_id)

        # Charge Move
        self.charge_id = check_for_none(int, data.get('move_2'), Unknown.TINY)
        self.charge_damage = get_move_damage(self.charge_id)
        self.charge_dps = get_move_dps(self.charge_id)
        self.charge_duration = get_move_duration(self.quick_id)
        self.charge_energy = get_move_energy(self.charge_id)

        # Gym Details (currently only sent from Monocle)
        self.gym_name = check_for_none(
            str, data.get('name'), Unknown.REGULAR).strip()
        self.gym_description = check_for_none(
            str, data.get('description'), Unknown.REGULAR).strip()
        self.gym_image = check_for_none(
            str, data.get('url'), Unknown.REGULAR)

        # Gym Team (this is only available from cache)
        self.current_team_id = check_for_none(
            int, data.get('team'), Unknown.TINY)

        self.name = self.gym_id
        self.geofence = Unknown.REGULAR
        self.custom_dts = {}

    def generate_dts(self, locale, timezone, units):
        """ Return a dict with all the DTS for this event. """
        raid_end_time = get_time_as_str(self.raid_end, timezone)
        dts = self.custom_dts.copy()

        boss_level = 20
        boosted_weather_id = \
            0 if Unknown.is_not(self.weather_id) else Unknown.TINY,
        if is_weather_boosted(self.mon_id, self.weather_id):
            boss_level = 25
            boosted_weather_id = self.weather_id
        boosted_weather_name = locale.get_weather_name(boosted_weather_id)
        weather_name = locale.get_weather_name(self.weather_id)

        type1 = locale.get_type_name(self.types[0])
        type2 = locale.get_type_name(self.types[1])

        cp_range = get_pokemon_cp_range(self.mon_id, boss_level)
        dts.update({
            # Identification
            'gym_id': self.gym_id,

            # Time Remaining
            'raid_time_left': raid_end_time[0],
            '12h_raid_end': raid_end_time[1],
            '24h_raid_end': raid_end_time[2],

            # Type
            'type1': type1,
            'type1_or_empty': Unknown.or_empty(type1),
            'type1_emoji': Unknown.or_empty(get_type_emoji(self.types[0])),
            'type2': type2,
            'type2_or_empty': Unknown.or_empty(type2),
            'type2_emoji': Unknown.or_empty(get_type_emoji(self.types[1])),
            'types': (
                "{}/{}".format(type1, type2)
                if Unknown.is_not(type2) else type1),
            'types_emoji': (
                "{}{}".format(
                    get_type_emoji(self.types[0]),
                    get_type_emoji(self.types[1]))
                if Unknown.is_not(type2) else get_type_emoji(self.types[0])),

            # Location
            'lat': self.lat,
            'lng': self.lng,
            'lat_5': "{:.5f}".format(self.lat),
            'lng_5': "{:.5f}".format(self.lng),
            'distance': (
                get_dist_as_str(self.distance, units)
                if Unknown.is_not(self.distance) else Unknown.SMALL),
            'direction': self.direction,
            'gmaps': get_gmaps_link(self.lat, self.lng),
            'applemaps': get_applemaps_link(self.lat, self.lng),
            'geofence': self.geofence,
            'weather_id': self.weather_id,
            'weather': weather_name,
            'weather_or_empty': Unknown.or_empty(weather_name),
            'weather_emoji': get_weather_emoji(self.weather_id),
            'boosted_weather_id': boosted_weather_id,
            'boosted_weather': boosted_weather_name,
            'boosted_weather_or_empty': (
                '' if boosted_weather_id == 0
                else Unknown.or_empty(boosted_weather_name)),
            'boosted_weather_emoji': get_weather_emoji(boosted_weather_id),
            'boosted_or_empty':
                locale.get_boosted_text() if boss_level == 25 else '',

            # Raid Info
            'raid_lvl': self.raid_lvl,
            'mon_name': locale.get_pokemon_name(self.mon_id),
            'mon_id': self.mon_id,
            'mon_id_3': "{:03}".format(self.mon_id),
            # TODO: Form?

            # Quick Move
            'quick_move': locale.get_move_name(self.quick_id),
            'quick_id': self.quick_id,
            'quick_damage': self.quick_damage,
            'quick_dps': self.quick_dps,
            'quick_duration': self.quick_duration,
            'quick_energy': self.quick_energy,

            # Charge Move
            'charge_move': locale.get_move_name(self.charge_id),
            'charge_id': self.charge_id,
            'charge_damage': self.charge_damage,
            'charge_dps': self.charge_dps,
            'charge_duration': self.charge_duration,
            'charge_energy': self.charge_energy,

            # CP info
            'cp': self.cp,
            'min_cp': cp_range[0],
            'max_cp': cp_range[1],

            # Gym Details
            'gym_name': self.gym_name,
            'gym_description': self.gym_description,
            'gym_image': self.gym_image,
            'team_id': self.current_team_id,
            'team_name': locale.get_team_name(self.current_team_id),
            'team_leader': locale.get_leader_name(self.current_team_id)
        })
        return dts
