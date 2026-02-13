from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import datetime, timedelta
import random


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        self.stdout.write('Clearing existing data...')
        
        # Delete all existing data using Django ORM
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        
        self.stdout.write(self.style.SUCCESS('Existing data cleared.'))
        
        # Create Teams
        self.stdout.write('Creating teams...')
        team_marvel = Team.objects.create(
            name='Team Marvel',
            description='Assemble! The mightiest heroes of Earth united for fitness.',
            captain='Iron Man',
            total_points=0,
            member_count=0
        )
        
        team_dc = Team.objects.create(
            name='Team DC',
            description='Justice League - protecting fitness goals and breaking limits.',
            captain='Superman',
            total_points=0,
            member_count=0
        )
        
        self.stdout.write(self.style.SUCCESS(f'Created teams: {team_marvel.name}, {team_dc.name}'))
        
        # Create Users - Marvel Heroes
        marvel_heroes = [
            {'username': 'ironman', 'email': 'tony.stark@marvel.com', 'first_name': 'Tony', 'last_name': 'Stark'},
            {'username': 'captainamerica', 'email': 'steve.rogers@marvel.com', 'first_name': 'Steve', 'last_name': 'Rogers'},
            {'username': 'blackwidow', 'email': 'natasha.romanoff@marvel.com', 'first_name': 'Natasha', 'last_name': 'Romanoff'},
            {'username': 'thor', 'email': 'thor.odinson@marvel.com', 'first_name': 'Thor', 'last_name': 'Odinson'},
            {'username': 'hulk', 'email': 'bruce.banner@marvel.com', 'first_name': 'Bruce', 'last_name': 'Banner'},
            {'username': 'spiderman', 'email': 'peter.parker@marvel.com', 'first_name': 'Peter', 'last_name': 'Parker'},
        ]
        
        # Create Users - DC Heroes
        dc_heroes = [
            {'username': 'superman', 'email': 'clark.kent@dc.com', 'first_name': 'Clark', 'last_name': 'Kent'},
            {'username': 'batman', 'email': 'bruce.wayne@dc.com', 'first_name': 'Bruce', 'last_name': 'Wayne'},
            {'username': 'wonderwoman', 'email': 'diana.prince@dc.com', 'first_name': 'Diana', 'last_name': 'Prince'},
            {'username': 'flash', 'email': 'barry.allen@dc.com', 'first_name': 'Barry', 'last_name': 'Allen'},
            {'username': 'aquaman', 'email': 'arthur.curry@dc.com', 'first_name': 'Arthur', 'last_name': 'Curry'},
            {'username': 'greenlantern', 'email': 'hal.jordan@dc.com', 'first_name': 'Hal', 'last_name': 'Jordan'},
        ]
        
        self.stdout.write('Creating users...')
        marvel_users = []
        dc_users = []
        
        for hero in marvel_heroes:
            user = User.objects.create(
                username=hero['username'],
                email=hero['email'],
                password='pbkdf2_sha256$260000$hashed_password_here',  # Mock hashed password
                first_name=hero['first_name'],
                last_name=hero['last_name'],
                team='Team Marvel',
                points=random.randint(500, 2000)
            )
            marvel_users.append(user)
        
        for hero in dc_heroes:
            user = User.objects.create(
                username=hero['username'],
                email=hero['email'],
                password='pbkdf2_sha256$260000$hashed_password_here',  # Mock hashed password
                first_name=hero['first_name'],
                last_name=hero['last_name'],
                team='Team DC',
                points=random.randint(500, 2000)
            )
            dc_users.append(user)
        
        all_users = marvel_users + dc_users
        self.stdout.write(self.style.SUCCESS(f'Created {len(all_users)} users'))
        
        # Update team stats
        team_marvel.member_count = len(marvel_users)
        team_marvel.total_points = sum(u.points for u in marvel_users)
        team_marvel.save()
        
        team_dc.member_count = len(dc_users)
        team_dc.total_points = sum(u.points for u in dc_users)
        team_dc.save()
        
        # Create Activities
        self.stdout.write('Creating activities...')
        activity_types = [
            ('Running', 5, 10),
            ('Weight Training', 30, 60),
            ('Cycling', 10, 15),
            ('Swimming', 8, 12),
            ('Yoga', 3, 5),
            ('Boxing', 12, 18),
        ]
        
        activity_count = 0
        for user in all_users:
            # Create 3-7 activities per user
            num_activities = random.randint(3, 7)
            for i in range(num_activities):
                activity_type, min_cal, max_cal = random.choice(activity_types)
                duration = random.randint(20, 90)
                calories = random.randint(min_cal, max_cal) * duration
                points = calories // 10
                
                Activity.objects.create(
                    user=user.username,
                    activity_type=activity_type,
                    duration=duration,
                    distance=random.uniform(1.0, 15.0) if activity_type in ['Running', 'Cycling'] else None,
                    calories_burned=calories,
                    points_earned=points,
                    notes=f'Great {activity_type.lower()} session!'
                )
                activity_count += 1
        
        self.stdout.write(self.style.SUCCESS(f'Created {activity_count} activities'))
        
        # Create Leaderboard entries
        self.stdout.write('Creating leaderboard entries...')
        sorted_users = sorted(all_users, key=lambda u: u.points, reverse=True)
        
        for rank, user in enumerate(sorted_users, start=1):
            user_activities = Activity.objects.filter(user=user.username)
            Leaderboard.objects.create(
                user=user.username,
                team=user.team,
                total_points=user.points,
                rank=rank,
                activities_count=user_activities.count()
            )
        
        self.stdout.write(self.style.SUCCESS(f'Created {len(sorted_users)} leaderboard entries'))
        
        # Create Workouts
        self.stdout.write('Creating workout suggestions...')
        workouts = [
            {
                'name': 'Super Soldier Circuit',
                'category': 'Strength Training',
                'difficulty': 'Advanced',
                'duration': 45,
                'calories': 450,
                'description': 'Inspired by Captain America training regimen.',
                'instructions': '1. Push-ups (3 sets of 20)\n2. Pull-ups (3 sets of 15)\n3. Squats (3 sets of 20)\n4. Plank (3 sets of 60 seconds)\n5. Burpees (3 sets of 15)'
            },
            {
                'name': 'Speed Force Sprint',
                'category': 'Cardio',
                'difficulty': 'Intermediate',
                'duration': 30,
                'calories': 350,
                'description': 'Channel The Flash with high-intensity interval training.',
                'instructions': '1. Warm-up jog (5 min)\n2. Sprint intervals (30 sec sprint, 90 sec walk) x 8\n3. Cool-down walk (5 min)'
            },
            {
                'name': 'Amazonian Warrior Workout',
                'category': 'Full Body',
                'difficulty': 'Advanced',
                'duration': 60,
                'calories': 600,
                'description': 'Build strength like Wonder Woman with this comprehensive routine.',
                'instructions': '1. Battle rope waves (3 sets of 45 sec)\n2. Medicine ball slams (3 sets of 15)\n3. Box jumps (3 sets of 12)\n4. Kettlebell swings (3 sets of 20)\n5. Mountain climbers (3 sets of 30)'
            },
            {
                'name': 'Web-Slinger Agility',
                'category': 'Agility',
                'difficulty': 'Beginner',
                'duration': 25,
                'calories': 200,
                'description': 'Improve agility and reflexes like Spider-Man.',
                'instructions': '1. Ladder drills (5 min)\n2. Cone exercises (5 min)\n3. Jump rope (5 min)\n4. Shadow boxing (5 min)\n5. Stretching (5 min)'
            },
            {
                'name': 'Atlantean Swimming Session',
                'category': 'Swimming',
                'difficulty': 'Intermediate',
                'duration': 40,
                'calories': 400,
                'description': 'Rule the pool with Aquaman-inspired swimming workout.',
                'instructions': '1. Freestyle (400m)\n2. Backstroke (200m)\n3. Breaststroke (200m)\n4. Butterfly (100m)\n5. Cool-down swimming (200m)'
            },
            {
                'name': 'Zen Master Yoga',
                'category': 'Yoga',
                'difficulty': 'Beginner',
                'duration': 30,
                'calories': 150,
                'description': 'Find your inner peace with this restorative yoga session.',
                'instructions': '1. Sun Salutations (5 rounds)\n2. Warrior poses (hold each for 1 min)\n3. Tree pose (1 min each side)\n4. Downward dog (2 min)\n5. Savasana (5 min)'
            },
            {
                'name': 'Arc Reactor Cardio Blast',
                'category': 'Cardio',
                'difficulty': 'Advanced',
                'duration': 50,
                'calories': 550,
                'description': 'Power through this high-energy Iron Man workout.',
                'instructions': '1. Running (15 min)\n2. Rowing machine (10 min)\n3. Cycling (15 min)\n4. Stair climbing (10 min)'
            },
            {
                'name': 'Dark Knight Core Training',
                'category': 'Core',
                'difficulty': 'Intermediate',
                'duration': 35,
                'calories': 300,
                'description': 'Build a strong core like Batman with these exercises.',
                'instructions': '1. Plank variations (3 sets of 45 sec each)\n2. Russian twists (3 sets of 30)\n3. Leg raises (3 sets of 15)\n4. Bicycle crunches (3 sets of 30)\n5. Dead bugs (3 sets of 20)'
            },
        ]
        
        for workout_data in workouts:
            Workout.objects.create(**workout_data)
        
        self.stdout.write(self.style.SUCCESS(f'Created {len(workouts)} workout suggestions'))
        
        # Summary
        self.stdout.write(self.style.SUCCESS('\n' + '='*50))
        self.stdout.write(self.style.SUCCESS('Database population completed successfully!'))
        self.stdout.write(self.style.SUCCESS('='*50))
        self.stdout.write(f'Teams: {Team.objects.count()}')
        self.stdout.write(f'Users: {User.objects.count()}')
        self.stdout.write(f'Activities: {Activity.objects.count()}')
        self.stdout.write(f'Leaderboard entries: {Leaderboard.objects.count()}')
        self.stdout.write(f'Workouts: {Workout.objects.count()}')
        self.stdout.write(self.style.SUCCESS('='*50 + '\n'))
