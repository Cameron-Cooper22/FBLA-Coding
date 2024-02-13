from django.urls import path
from .views import HomePageView, SearchResultsView, DetailsSearchView

urlpatterns = [
    path('search/<int:id>', DetailsSearchView.as_view(), name='details'),
    path("search/", SearchResultsView.as_view(), name="search_results"),
    path("", HomePageView.as_view(), name="home"),
]