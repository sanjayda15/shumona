from django.urls import path
from .views import (ProductListView,MenListView,
                    WomenListView,KidsListView,
                    ProductDetailSlugView)

app_name = 'products'
urlpatterns = [
    path('',ProductListView.as_view(),name='products'),
    path('menlist/',MenListView.as_view(),name='menlist'),
    path('womenlist/',WomenListView.as_view(),name='womenlist'),
    path('kidslist/',KidsListView.as_view(),name='kidslist'),
    path('<slug>/',ProductDetailSlugView.as_view(),name='detail')
             ]
