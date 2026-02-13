from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User model."""
    id = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', 'team', 'points', 'created_at']
        extra_kwargs = {'password': {'write_only': True}}
    
    def get_id(self, obj):
        """Convert ObjectId to string."""
        return str(obj._id)


class TeamSerializer(serializers.ModelSerializer):
    """Serializer for Team model."""
    id = serializers.SerializerMethodField()
    
    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'captain', 'total_points', 'member_count', 'created_at']
    
    def get_id(self, obj):
        """Convert ObjectId to string."""
        return str(obj._id)


class ActivitySerializer(serializers.ModelSerializer):
    """Serializer for Activity model."""
    id = serializers.SerializerMethodField()
    
    class Meta:
        model = Activity
        fields = ['id', 'user', 'activity_type', 'duration', 'distance', 'calories_burned', 'points_earned', 'date', 'notes']
    
    def get_id(self, obj):
        """Convert ObjectId to string."""
        return str(obj._id)


class LeaderboardSerializer(serializers.ModelSerializer):
    """Serializer for Leaderboard model."""
    id = serializers.SerializerMethodField()
    
    class Meta:
        model = Leaderboard
        fields = ['id', 'user', 'team', 'total_points', 'rank', 'activities_count', 'updated_at']
    
    def get_id(self, obj):
        """Convert ObjectId to string."""
        return str(obj._id)


class WorkoutSerializer(serializers.ModelSerializer):
    """Serializer for Workout model."""
    id = serializers.SerializerMethodField()
    
    class Meta:
        model = Workout
        fields = ['id', 'name', 'category', 'difficulty', 'duration', 'calories', 'description', 'instructions', 'created_at']
    
    def get_id(self, obj):
        """Convert ObjectId to string."""
        return str(obj._id)
