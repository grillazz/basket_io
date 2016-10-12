from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    position = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    place_of_birth = models.CharField(max_length=255, blank=True, null=True)
    height = models.SmallIntegerField(blank=True, null=True)
    weight = models.SmallIntegerField(blank=True, null=True)
    teams = models.ManyToManyField(Team, related_name='players', through='Membership')
    image = models.ImageField(upload_to='players', blank=True, null=True)

    class Meta:
        db_table = 'player'


class Membership(models.Model):
    team = models.ForeignKey(Team, related_name="memberships")
    player = models.ForeignKey(Player, related_name='memberships')
    number = models.IntegerField(blank=True, null=True)
    active = models.NullBooleanField()
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'membership'
        unique_together = [('person', 'team', 'active')]


class Team(models.Model):
    club_name = models.CharField(max_length=255, blank=True, null=True)
    founded = models.CharField(max_length=255, blank=True, null=True)
    club_colors = models.CharField(max_length=255, blank=True, null=True)
    clothing = models.CharField(max_length=255, blank=True, null=True)
    sponsor = models.CharField(max_length=255, blank=True, null=True)
    details = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='teams', blank=True, null=True)

    class Meta:
        db_table = 'team'


class Match(models.Model):
    date = models.DateTimeField(blank=True, null=True, db_index=True)
    #season = models.ForeignKey(Season, blank=True, null=True)
    #venue = models.ForeignKey(Venue, blank=True, null=True, related_name='matches')
    team_a = models.ForeignKey(Team, db_column='team_A_id', blank=True, null=True, related_name='match_team_a', db_index=True)
    team_b = models.ForeignKey(Team, db_column='team_B_id', blank=True, null=True, related_name='match_team_b', db_index=True)
    #referees = models.ManyToManyField(Referee, related_name='matches', through=MatchReferee)
    memberships = models.ManyToManyField(Membership, related_name='matches', through='MatchMembership')
    #broadcasters = models.ManyToManyField(Broadcaster, related_name='matches')
    points_a = models.SmallIntegerField(db_column='goals_A', blank=True, null=True)
    points_b = models.SmallIntegerField(db_column='goals_B', blank=True, null=True)

    class Meta:
        db_table = 'match'


class MatchMembership(models.Model):
    membership = models.ForeignKey(Membership, related_name='match_memberships')
    match = models.ForeignKey(Match, related_name='match_memberships')
    position = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'matchmembership'
