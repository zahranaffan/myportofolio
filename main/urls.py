from django.urls import path

from main import views

app_name = "main"

urlpatterns = [
    path("", views.show_main, name="show_main"),
    path("experience/", views.show_experience, name="show_experience"),
    path("experience/add/", views.create_experience, name="create_experience"),
    path("api/experience/", views.get_experience_json, name="get_experience_json"),
    path("experience/<uuid:experience_id>/delete/", views.delete_experience, name="delete_experience"),
    path("experience/<uuid:experience_id>/edit/", views.update_experience, name="update_experience"),
    path("experience/<uuid:experience_id>/star/", views.toggle_star, name="toggle_star"),
    path("experience/add-ajax/", views.create_experience_ajax, name="create_experience_ajax"),
    path('achievement/', views.show_achievement, name='show_achievement'),
    path("achievement/add/", views.create_achievement, name="create_achievement"),
    path("achievement/<uuid:achievement_id>/edit/", views.update_achievement, name="update_achievement"),
    path("achievement/<uuid:achievement_id>/delete/", views.delete_achievement, name="delete_achievement"),
    path("api/achievement/", views.get_achievement_json, name="get_achievement_json"),
    path("achievement/<uuid:achievement_id>/star/", views.toggle_star_achievement, name="toggle_star_achievement"),
    path("register/", views.register, name="register"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),

]