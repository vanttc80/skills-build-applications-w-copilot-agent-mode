from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='pass')
        self.assertEqual(user.email, 'test@example.com')

    def test_create_team(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(team.name, 'Test Team')

    def test_create_activity(self):
        user = User.objects.create_user(username='testuser2', email='test2@example.com', password='pass')
        team = Team.objects.create(name='Test Team 2')
        activity = Activity.objects.create(name='Run', user=user, team=team)
        self.assertEqual(activity.name, 'Run')
        self.assertEqual(activity.user.username, 'testuser2')
        self.assertEqual(activity.team.name, 'Test Team 2')

    def test_create_leaderboard(self):
        team = Team.objects.create(name='Test Team 3')
        leaderboard = Leaderboard.objects.create(team=team, points=50)
        self.assertEqual(leaderboard.team.name, 'Test Team 3')
        self.assertEqual(leaderboard.points, 50)

    def test_create_workout(self):
        workout = Workout.objects.create(name='Pushups', description='Do 50 pushups')
        self.assertEqual(workout.name, 'Pushups')
        self.assertEqual(workout.description, 'Do 50 pushups')
