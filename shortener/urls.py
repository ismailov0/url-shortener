from django.urls import path
from shortener.views import ShortenedURLListCreateView, ShortenedURLRetrieveView

urlpatterns = [
    path('short-url/', ShortenedURLListCreateView.as_view(),
         name='shortenedurl-list-create'),
    path('short-url/<str:short_code>/',
         ShortenedURLRetrieveView.as_view(), name='shortenedurl-retrieve'),
]
