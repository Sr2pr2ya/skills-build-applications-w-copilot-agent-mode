from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet, ActivityViewSet, TeamViewSet, LeaderboardEntryViewSet, WorkoutSuggestionViewSet

router = DefaultRouter()
router.register(r'userprofiles', UserProfileViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'leaderboard', LeaderboardEntryViewSet)
router.register(r'workoutsuggestions', WorkoutSuggestionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]