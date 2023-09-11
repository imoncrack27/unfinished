from django.urls import path

from . import views

urlpatterns = [
    path('', views.BrowseDocumentsView.as_view()),
    path('categories/', views.CategoriesView.as_view()),
    path('my/', views.MyDocuView.as_view()),
    path('request/', views.RequestDocumentView.as_view()),
    path('newest/', views.NewestDocumentsView.as_view()),
    path('<int:pk>/', views.DocumentsDetailView.as_view()),
    path('<int:pk>/delete/', views.RequestDocumentView.as_view()),
    path('<int:pk>/edit/', views.RequestDocumentView.as_view()),
]