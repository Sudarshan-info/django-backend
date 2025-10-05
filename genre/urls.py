from django.urls import path,include
from.import views
from rest_framework.routers import DefaultRouter
from .views import CollectionViewSet, PieceViewSet

# --- API Router Setup ---
router = DefaultRouter()
router.register(r'collections', CollectionViewSet)
router.register(r'pieces', PieceViewSet)

urlpatterns = [
    #For overall /genre/
    path('',views.index.as_view(),name="index"),

    #For 1st genre description i.e /genre/1
    path('<int:pk>/',views.details.as_view(),name="details"),

    #For creating registration userform
    path('register/',views.UserFormView.as_view(),name="userform"),

    # --- New API Endpoints ---
    path('api/', include(router.urls)),
]


from django.urls import path
from . import views

urlpatterns = [
    path('collections/', views.CollectionList.as_view(), name='collection-list'),
    path('run-migrations/', views.run_migrations, name='run-migrations'),  # temporary
]

