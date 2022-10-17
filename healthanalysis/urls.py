from django.urls import path

from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('healthanalysis/', views.HealthAnalysisList.as_view()),
    path('healthanalysis/<int:pk>/', views.HealthAnalysisDetail.as_view()),
    path('yieldprediction/', views.YieldPredictionView.as_view()),
    path('weatherapi/', views.detail_view),
]
