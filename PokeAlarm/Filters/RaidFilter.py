# Standard Library Imports
import operator
# 3rd Party Imports
# Local Imports
from . import BaseFilter
from PokeAlarm.Utilities import MonUtils as MonUtils
from PokeAlarm.Utilities import GymUtils as GymUtils
from PokeAlarm.Utils import get_weather_id


class RaidFilter(BaseFilter):
    """ Filter class for limiting which egg trigger a notification. """

    def __init__(self, name, data):
        """ Initializes base parameters for a filter. """
        super(RaidFilter, self).__init__(name)

        # Monster ID - f.mon_ids in r.mon_id
        self.mon_ids = self.evaluate_attribute(  #
            event_attribute='mon_id', eval_func=operator.contains,
            limit=BaseFilter.parse_as_set(
                MonUtils.get_monster_id, 'monsters', data))

        # Distance
        self.min_dist = self.evaluate_attribute(  # f.min_dist <= r.distance
            event_attribute='distance', eval_func=operator.le,
            limit=BaseFilter.parse_as_type(float, 'min_dist', data))
        self.max_dist = self.evaluate_attribute(  # f.max_dist <= r.distance
            event_attribute='distance', eval_func=operator.ge,
            limit=BaseFilter.parse_as_type(float, 'max_dist', data))

        # Time Left
        self.min_time_left = self.evaluate_attribute(
            # f.min_time_left <= r.time_left
            event_attribute='time_left', eval_func=operator.le,
            limit=BaseFilter.parse_as_type(int, 'min_time_left', data))
        self.max_time_left = self.evaluate_attribute(
            # f.max_time_left >= r.time_left
            event_attribute='time_left', eval_func=operator.ge,
            limit=BaseFilter.parse_as_type(int, 'max_time_left', data))

        # Monster Info
        self.min_lvl = self.evaluate_attribute(  # f.min_lvl <= r.mon_lvl
            event_attribute='raid_lvl', eval_func=operator.le,
            limit=BaseFilter.parse_as_type(int, 'min_raid_lvl', data))
        self.max_lvl = self.evaluate_attribute(  # f.max_lvl >= r.mon_lvl
            event_attribute='raid_lvl', eval_func=operator.ge,
            limit=BaseFilter.parse_as_type(int, 'max_raid_lvl', data))

        # CP
        self.min_cp = self.evaluate_attribute(  # f.min_cp <= r.cp
            event_attribute='cp', eval_func=operator.le,
            limit=BaseFilter.parse_as_type(int, 'min_cp', data))
        self.max_cp = self.evaluate_attribute(  # f.max_cp >= r.cp
            event_attribute='cp', eval_func=operator.ge,
            limit=BaseFilter.parse_as_type(int, 'max_cp', data))

        # Quick Move
        self.quick_moves = self.evaluate_attribute(  # f.q_ms contains r.q_m
            event_attribute='quick_id', eval_func=operator.contains,
            limit=BaseFilter.parse_as_set(
                MonUtils.get_move_id, 'quick_moves', data))
        # Charge Move
        self.charge_moves = self.evaluate_attribute(  # f.c_ms contains r.c_m
            event_attribute='charge_id', eval_func=operator.contains,
            limit=BaseFilter.parse_as_set(
                MonUtils.get_move_id, 'charge_moves', data))

        # Gym name
        self.gym_name_contains = self.evaluate_attribute(  # f.gn matches e.gn
            event_attribute='gym_name', eval_func=GymUtils.match_regex_dict,
            limit=BaseFilter.parse_as_set(
                GymUtils.create_regex, 'gym_name_contains', data))

        # Team Info
        self.old_team = self.evaluate_attribute(  # f.ctis contains m.cti
            event_attribute='current_team_id', eval_func=operator.contains,
            limit=BaseFilter.parse_as_set(
                GymUtils.get_team_id, 'current_teams', data))

        # Weather
        self.weather_ids = self.evaluate_attribute(  # f.w_ids contains m.w_id
            event_attribute='weather_id', eval_func=operator.contains,
            limit=BaseFilter.parse_as_set(get_weather_id, 'weather', data))

        # Geofences
        self.geofences = BaseFilter.parse_as_set(str, 'geofences', data)

        # Custom DTS
        self.custom_dts = BaseFilter.parse_as_dict(
            str, str, 'custom_dts', data)

        # Missing Info
        self.is_missing_info = BaseFilter.parse_as_type(
            bool, 'is_missing_info', data)

        # Reject leftover parameters
        for key in data:
            raise ValueError("'{}' is not a recognized parameter for"
                             " Raid filters".format(key))

    def to_dict(self):
        """ Create a dict representation of this Filter. """
        settings = {}
        # Monster ID
        if self.mon_ids is not None:
            settings['monster_ids'] = self.mon_ids

        # Distance
        if self.min_dist is not None:
            settings['min_dist'] = self.min_dist
        if self.max_dist is not None:
            settings['max_dist'] = self.max_dist

        # Level
        if self.min_lvl is not None:
            settings['min_lvl'] = self.min_lvl
        if self.max_lvl is not None:
            settings['max_lvl'] = self.max_lvl

        # Weather
        if self.weather_ids is not None:
            settings['weather_ids'] = self.weather_ids

        # Gym Name
        if self.gym_name_contains is not None:
            settings['gym_name_matches'] = self.gym_name_contains

        # Geofences
        if self.geofences is not None:
            settings['geofences'] = self.geofences

        # Missing Info
        if self.is_missing_info is not None:
            settings['missing_info'] = self.is_missing_info

        return settings
