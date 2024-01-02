# api/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BillViewSet, LegislatorViewSet, VoteViewSet, VoteResultViewSet

router = DefaultRouter()
router.register(r'bills', BillViewSet, basename='bill')
router.register(r'legislators', LegislatorViewSet, basename='legislator')
router.register(r'votes', VoteViewSet, basename='vote')
router.register(r'vote-results', VoteResultViewSet, basename='vote-result')

urlpatterns = [
    path('', include(router.urls)),
]
