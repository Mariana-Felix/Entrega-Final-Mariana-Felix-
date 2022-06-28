from django.urls import path

from app_coder import views

app_name='app_coder'
urlpatterns = [
    path('', views.index, name='Home'),
    # path('courses', views.courses, name='course-list'),
    path('comments', views.comments, name='Comments'),
    path('formHTML', views.form_hmtl),
    path('article-django-forms', views.articles_forms_django, name='ArticlesDjangoForms'),
    path('comment/add', views.comment_forms_django, name='comment-add'),
    path('search', views.search, name='Search'),


    
    path('articles', views.ArticlesListView.as_view(), name='articles-list'),
    path('article/add/', views.ArticlesCreateView.as_view(), name='articles-add'),
    path('article/<int:pk>/detail', views.ArticlesDetailView, name='articles-detail'),
    path('article/<int:pk>/update', views.ArticlesUpdateView.as_view(), name='articles-update'),
    path('article/<int:pk>/delete', views.ArticlesDeleteView.as_view(), name='articles-delete'),
    path('comment/<int:pk>/create', views.CommentsCreateView.as_view(), name='comments-create'),
    path('comment/<int:pk>/update', views.ArticlesUpdateView.as_view(), name='comments-update'),
    path('comment/<int:pk>/delete', views.ArticlesDeleteView.as_view(), name='comments-delete'),
    path('login', views.login_request, name='user-login'),
    path('logout', views.logout_request, name='user-logout'),
    path('register', views.register, name='user-register'),
    path('register/update', views.user_update, name='user-update'),
    path('avatar/load', views.avatar_load, name='avatar-load'),
    path ('about_me',views.about_me, name= 'about_me' )
]
