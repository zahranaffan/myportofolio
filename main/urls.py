from django.urls import path

from main.views import (
    show_main,
    show_experience,
    create_experience,
    get_experience_json,
    delete_experience,
    update_experience,
    show_achievement,
    create_achievement,
    update_achievement,
)

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("experience/add/", create_experience, name="create_experience"),
    path("api/experience/", get_experience_json, name="get_experience_json"),
    path("experience/<uuid:experience_id>/delete/", delete_experience, name="delete_experience"),
    path("experience/<uuid:experience_id>/edit/", update_experience, name="update_experience"),
    path('achievement/', show_achievement, name='show_achievement'),
    path("achievement/add/", create_achievement, name="create_achievement"),
    path("achievement/<uuid:achievement_id>/edit/", update_achievement, name="update_achievement"),
]