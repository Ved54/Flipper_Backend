from backend import views
from django.conf import settings
from django.contrib import admin
from django.urls import path
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path('user/', views.UserList),
    path('carupload/', views.CarList),
    path('propertyupload/', views.PropertyList), 
    path('mobileupload/', views.MobileList),
    path('jobupload/', views.JobList),
    path('bikeupload/', views.BikeList),
    path('furnitureupload/', views.FurnitureList),
    path('fashionupload/', views.FashionList),
    path('electronicappliancesupload/', views.ElectronicAppliancesList),
    path('commupload/', views.CommList),
    path('bookssportshobbiesupload/', views.BSHList),
    path('petupload/', views.PetList),
    path('serviceupload/', views.ServiceList),
    path('favorite/', views.FavoriteList),
    path('rating/', views.RatingList),
    path('barter/', views.BarterList),
    path('favoritebarter/', views.FavBarterList)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)