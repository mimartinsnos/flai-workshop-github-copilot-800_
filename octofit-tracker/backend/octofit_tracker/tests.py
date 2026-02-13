from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import User, Team, Activity, Leaderboard, Workout


class UserModelTest(TestCase):
    """Test cases for User model."""
    
    def setUp(self):
        self.user = User.objects.create(
            username='testuser',
            email='test@example.com',
            password='testpass123',
            first_name='Test',
            last_name='User',
            team='Test Team',
            points=100
        )
    
    def test_user_creation(self):
        """Test user is created correctly."""
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertEqual(self.user.points, 100)


class TeamModelTest(TestCase):
    """Test cases for Team model."""
    
    def setUp(self):
        self.team = Team.objects.create(
            name='Test Team',
            description='A test team',
            captain='Test Captain',
            total_points=500,
            member_count=5
        )
    
    def test_team_creation(self):
        """Test team is created correctly."""
        self.assertEqual(self.team.name, 'Test Team')
        self.assertEqual(self.team.total_points, 500)
        self.assertEqual(self.team.member_count, 5)


class ActivityModelTest(TestCase):
    """Test cases for Activity model."""
    
    def setUp(self):
        self.activity = Activity.objects.create(
            user='testuser',
            activity_type='Running',
            duration=30,
            distance=5.0,
            calories_burned=300,
            points_earned=30,
            notes='Test run'
        )
    
    def test_activity_creation(self):
        """Test activity is created correctly."""
        self.assertEqual(self.activity.user, 'testuser')
        self.assertEqual(self.activity.activity_type, 'Running')
        self.assertEqual(self.activity.duration, 30)


class LeaderboardModelTest(TestCase):
    """Test cases for Leaderboard model."""
    
    def setUp(self):
        self.leaderboard_entry = Leaderboard.objects.create(
            user='testuser',
            team='Test Team',
            total_points=1000,
            rank=1,
            activities_count=10
        )
    
    def test_leaderboard_creation(self):
        """Test leaderboard entry is created correctly."""
        self.assertEqual(self.leaderboard_entry.user, 'testuser')
        self.assertEqual(self.leaderboard_entry.rank, 1)
        self.assertEqual(self.leaderboard_entry.total_points, 1000)


class WorkoutModelTest(TestCase):
    """Test cases for Workout model."""
    
    def setUp(self):
        self.workout = Workout.objects.create(
            name='Test Workout',
            category='Strength Training',
            difficulty='Beginner',
            duration=30,
            calories=250,
            description='A test workout',
            instructions='Do the exercises'
        )
    
    def test_workout_creation(self):
        """Test workout is created correctly."""
        self.assertEqual(self.workout.name, 'Test Workout')
        self.assertEqual(self.workout.category, 'Strength Training')
        self.assertEqual(self.workout.difficulty, 'Beginner')


class UserAPITest(APITestCase):
    """Test cases for User API endpoints."""
    
    def test_api_root(self):
        """Test API root endpoint returns expected links."""
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('users', response.data)
        self.assertIn('teams', response.data)
        self.assertIn('activities', response.data)
        self.assertIn('leaderboard', response.data)
        self.assertIn('workouts', response.data)


class TeamAPITest(APITestCase):
    """Test cases for Team API endpoints."""
    
    def setUp(self):
        self.team = Team.objects.create(
            name='Test Team',
            description='A test team',
            captain='Test Captain',
            total_points=100
        )
    
    def test_get_teams_list(self):
        """Test GET request to teams list endpoint."""
        response = self.client.get('/api/teams/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ActivityAPITest(APITestCase):
    """Test cases for Activity API endpoints."""
    
    def setUp(self):
        self.activity = Activity.objects.create(
            user='testuser',
            activity_type='Running',
            duration=30,
            calories_burned=300,
            points_earned=30
        )
    
    def test_get_activities_list(self):
        """Test GET request to activities list endpoint."""
        response = self.client.get('/api/activities/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class LeaderboardAPITest(APITestCase):
    """Test cases for Leaderboard API endpoints."""
    
    def setUp(self):
        self.leaderboard = Leaderboard.objects.create(
            user='testuser',
            team='Test Team',
            total_points=1000,
            rank=1,
            activities_count=10
        )
    
    def test_get_leaderboard_list(self):
        """Test GET request to leaderboard list endpoint."""
        response = self.client.get('/api/leaderboard/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class WorkoutAPITest(APITestCase):
    """Test cases for Workout API endpoints."""
    
    def setUp(self):
        self.workout = Workout.objects.create(
            name='Test Workout',
            category='Strength Training',
            difficulty='Beginner',
            duration=30,
            calories=250,
            description='Test',
            instructions='Test instructions'
        )
    
    def test_get_workouts_list(self):
        """Test GET request to workouts list endpoint."""
        response = self.client.get('/api/workouts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
