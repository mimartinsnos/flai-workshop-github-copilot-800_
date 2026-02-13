from djongo import models
from django.contrib.auth.models import AbstractUser


class User(models.Model):
    """User model for OctoFit Tracker."""
    _id = models.ObjectIdField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    team = models.CharField(max_length=100, blank=True, null=True)
    points = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'users'
    
    def __str__(self):
        return self.username


class Team(models.Model):
    """Team model for OctoFit Tracker."""
    _id = models.ObjectIdField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    captain = models.CharField(max_length=100)
    total_points = models.IntegerField(default=0)
    member_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'teams'
    
    def __str__(self):
        return self.name


class Activity(models.Model):
    """Activity model for logging fitness activities."""
    _id = models.ObjectIdField(primary_key=True)
    user = models.CharField(max_length=100)
    activity_type = models.CharField(max_length=50)
    duration = models.IntegerField()  # in minutes
    distance = models.FloatField(blank=True, null=True)  # in kilometers
    calories_burned = models.IntegerField(default=0)
    points_earned = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)
    
    class Meta:
        db_table = 'activities'
    
    def __str__(self):
        return f"{self.user} - {self.activity_type}"


class Leaderboard(models.Model):
    """Leaderboard model for tracking rankings."""
    _id = models.ObjectIdField(primary_key=True)
    user = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    total_points = models.IntegerField(default=0)
    rank = models.IntegerField(default=0)
    activities_count = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'leaderboard'
    
    def __str__(self):
        return f"{self.rank}. {self.user} - {self.total_points} points"


class Workout(models.Model):
    """Workout model for personalized workout suggestions."""
    _id = models.ObjectIdField(primary_key=True)
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=50)
    difficulty = models.CharField(max_length=20)
    duration = models.IntegerField()  # in minutes
    calories = models.IntegerField()  # estimated calories burned
    description = models.TextField()
    instructions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'workouts'
    
    def __str__(self):
        return f"{self.name} ({self.difficulty})"
