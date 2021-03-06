from nba_py import _api_scrape, _get_json
from nba_py.constants import *


class Leaders:
    _endpoint = 'leagueleaders'

    def __init__(self,
                 league_id=League.Default,
                 per_mode=PerMode.Default,
                 stat_category=StatCategory.Default,
                 season=CURRENT_SEASON,
                 season_type=SeasonType.Default,
                 scope=Scope.Default,):
        self.json = _get_json(endpoint=self._endpoint,
                              params={'LeagueID': league_id,
                                      'PerMode': per_mode,
                                      'StatCategory': stat_category,
                                      'Season': season,
                                      'SeasonType': season_type,
                                      'Scope': scope})

    def results(self):
        return _api_scrape(self.json, 0)


class LeadersTiles:
    _endpoint = 'leaderstiles'

    def __init__(self,
                 league_id=League.Default,
                 season=CURRENT_SEASON,
                 season_type=SeasonType.Default,
                 game_scope=GameScope.Default,
                 player_scope=PlayerScope.Default,
                 player_or_team=PlayerOrTeam.Default,
                 stat_category=StatCategory.Default):
        self.json = _get_json(endpoint=self._endpoint,
                              params={'LeagueID': league_id,
                                      'Stat': stat_category,
                                      'Season': season,
                                      'SeasonType': season_type,
                                      'GameScope': game_scope,
                                      'PlayerScope': player_scope,
                                      'PlayerOrTeam': player_or_team})

    def current_season_high(self):
        return _api_scrape(self.json, 0)

    def alltime_season_high(self):
        return _api_scrape(self.json, 1)

    def last_season_high(self):
        return _api_scrape(self.json, 2)

    def low_season_high(self):
        return _api_scrape(self.json, 3)


class Lineups:
    _endpoint = 'leaguedashlineups'

    def __init__(self,
                 group_quantity=GroupQuantity.Default,
                 season_type=SeasonType.Default,
                 measure_type=MeasureType.Default,
                 per_mode=PerMode.Default,
                 plus_minus=PlusMinus.Default,
                 pace_adjust=PaceAdjust.Default,
                 rank=Rank.Default,
                 season=CURRENT_SEASON,
                 outcome=Outcome.Default,
                 location=Location.Default,
                 month=Month.Default,
                 season_segment=SeasonSegment.Default,
                 date_from=DateFrom.Default,
                 date_to=DateTo.Default,
                 opponent_team_id=OpponentTeamID.Default,
                 vs_conference=VsConference.Default,
                 vs_division=VsDivision.Default,
                 game_segment=GameSegment.Default,
                 period=Period.Default,
                 last_n_games=LastNGames.Default):
        self.json = _get_json(endpoint=self._endpoint,
                              params={'GroupQuantity': group_quantity,
                                      'SeasonType': season_type,
                                      'MeasureType': measure_type,
                                      'PerMode': per_mode,
                                      'PlusMinus': plus_minus,
                                      'PaceAdjust': pace_adjust,
                                      'Rank': rank,
                                      'Season': season,
                                      'Outcome': outcome,
                                      'Location': location,
                                      'Month': month,
                                      'SeasonSegment': season_segment,
                                      'DateFrom': date_from,
                                      'DateTo': date_to,
                                      'OpponentTeamID': opponent_team_id,
                                      'VsConference': vs_conference,
                                      'VsDivision': vs_division,
                                      'GameSegment': game_segment,
                                      'Period': period,
                                      'LastNGames': last_n_games})

    def overall(self):
        return _api_scrape(self.json, 0)
