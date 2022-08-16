from django.urls import path

from . import views


urlpatterns = [
    path('blog/', views.BlogList.as_view()),
    path('blog/<int:pk>/', views.BlogDetail.as_view()),
]
