from django.urls import path
from expense_tracker import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('create/', views.create_expense, name='create'),
    path('edit/<int:exp_id>', views.edit_expense, name='edit'),
    path('delete/<int:exp_id>', views.delete_expense, name='delete'),
    path('profile/', views.profile_page, name='profile'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('profile/delete/', views.profile_delete, name='profile_delete')
]
