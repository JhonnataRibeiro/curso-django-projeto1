from django.urls import path
# from recipes.views import home
from recipes import views

urlpatterns = [
    # path('', home),
    path('', views.home, name="recipes-home"),
    path('recipes/<int:id>/', views.recipe, name="recipes-recipe"),
    path('recipes/category/<int:category_id>/', views.recipe, name="category"),
]