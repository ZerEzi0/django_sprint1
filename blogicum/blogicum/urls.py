from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',
         include(('blog.urls', 'blog'),
                 namespace='blog_main')
         ),
    path('posts/',
         include(('blog.urls', 'blog'),
                 namespace='blog_posts')
         ),
    path('category/',
         include(('blog.urls', 'blog'),
                 namespace='blog_category')
         ),
    path('pages/', include('pages.urls')),
]

'''Я пытался все объединить в include,
но, исходя из ошибок,
требуется что-то исправить blog и pages.
Как результат - я все поломал и запутался, aахахааха.
Мог ты мне поподробнее объяснить, пожалуйста?
Очень благодарен! Спасибо тебе!'''
