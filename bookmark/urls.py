from django.urls import path
from .views import BookmarkList, BookmarkDetail, BookmarkCreate, BookmarkUpdate, BookmarkDelete


app_name = 'bookmark'

urlpatterns = [
    path('', BookmarkList.as_view(), name='index'),
    path('detail/<pk>/', BookmarkDetail.as_view(), name='detail'),
    path('create/', BookmarkCreate.as_view(), name='create'),
    path('update/<pk>/', BookmarkUpdate.as_view(), name='update'),
    path('delete/<pk>/', BookmarkDelete.as_view(), name='delete'),
]