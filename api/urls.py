from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('api-token-auth/', views.AppToken.as_view()), #to obtain auth-token on login
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view()),
    path('comments/', views.CommentList.as_view()),
    path('comments/<int:pk>/', views.CommentDetail.as_view()),
    path('categories/', views.CategoryList.as_view()),
    path('categories/<int:pk>/', views.CategoryDetail.as_view()),
    path('postlike/<int:pk>/', views.LikeListCreate.as_view()),

    path('GetPostByCategory/<str:pk>/', views.GetPostByCategory.as_view()),
    path('GetPostByMonth/<str:pk>/', views.GetPostByMonth.as_view()),




] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)