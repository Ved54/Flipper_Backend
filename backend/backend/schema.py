import graphene
from graphene_django import DjangoObjectType
from graphql import GraphQLError
from .models import *

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = "__all__"
        
class CarType(DjangoObjectType):
    class Meta:
        model = CarUpload
        fields = "__all__"
        
class PropertyType(DjangoObjectType):
    class Meta:
        model = PropertyUpload
        fields = "__all__"
        
class MobileType(DjangoObjectType):
    class Meta:
        model = MobileUpload
        fields = "__all__"
        
class JobType(DjangoObjectType):
    class Meta:
        model = JobUpload
        fields = "__all__"
        
class BikeType(DjangoObjectType):
    class Meta:
        model = BikeUpload
        fields = "__all__"
        
class FurnitureType(DjangoObjectType):
    class Meta:
        model = FurnitureUpload
        fields = "__all__"
        
class FashionType(DjangoObjectType):
    class Meta:
        model = FashionUpload
        fields = "__all__"
        
class ElectronicAppliancesType(DjangoObjectType):
    class Meta:
        model = ElectronicAppliancesUpload
        fields = "__all__"
        
class CommType(DjangoObjectType):
    class Meta:
        model = CommUpload
        fields = "__all__"

class BSHType(DjangoObjectType):
    class Meta:
        model = BooksSportsHobbiesUpload
        fields = "__all__"
        
class PetType(DjangoObjectType):
    class Meta:
        model = PetUpload
        fields = "__all__"

class ServiceType(DjangoObjectType):
    class Meta:
        model = ServiceUpload
        fields = "__all__"
        
class FavoriteType(DjangoObjectType):
    class Meta:
        model = Favorite
        fields = "__all__"

class RatingType(DjangoObjectType):
    class Meta:
        model = Rating
        fields = "__all__"

class BarterType(DjangoObjectType):
    class Meta:
        model = Barter
        fields = "__all__"
        
class Query(graphene.ObjectType):
    # ---------- User ----------
    displayUsers = graphene.List(UserType)
    usersbyid = graphene.Field(UserType, flipperUser=graphene.String())
    def resolve_displayUsers(self, info):
        return User.objects.all()
    
    def resolve_usersbyid(self, info, flipperUser):
        try:
            return User.objects.get(flipperUser=flipperUser)
        except User.DoesNotExist:
            raise GraphQLError(f"User with ID {flipperUser} does not exist.")
        
    # ---------- Car ----------
    displayCars = graphene.List(CarType, flipperUser=graphene.String())
    carsbyid = graphene.Field(CarType, flipperUser=graphene.String())
    def resolve_displayCars(self, info, flipperUser):
        if flipperUser:
            return CarUpload.objects.exclude(flipperUser=flipperUser)
        else:
            return CarUpload.objects.all()
        
    def resolve_carsbyid(self, info, flipperUser):
        try:
            return CarUpload.objects.get(flipperUser=flipperUser)
        except CarUpload.DoesNotExist:
            raise GraphQLError(f"Uploads with ID {flipperUser} does not exist.")
        
    # ---------- Property ----------
    displayProperties = graphene.List(PropertyType, flipperUser=graphene.String())
    propertiesbyid = graphene.Field(PropertyType, flipperUser=graphene.String())
    def resolve_displayProperties(self, info, flipperUser):
        if flipperUser:
            return PropertyUpload.objects.exclude(flipperUser=flipperUser)
        else:
            return PropertyUpload.objects.all()
            
    def resolve_propertiesbyid(self, info, flipperUser):
        try:
            return PropertyUpload.objects.get(flipperUser=flipperUser)
        except PropertyUpload.DoesNotExist:
            raise GraphQLError(f"Uploads with ID {flipperUser} does not exist.")
    
    # ---------- Mobile ----------
    displayMobiles = graphene.List(MobileType, flipperUser=graphene.String())
    mobilesbyid = graphene.Field(MobileType, flipperUser=graphene.String())
    def resolve_displayMobiles(self, info, flipperUser):
        if flipperUser:
            return MobileUpload.objects.exclude(flipperUser=flipperUser)
        else:
            return MobileUpload.objects.all()
    
    def resolve_mobilesbyid(self, info, flipperUser):
        try:
            return MobileUpload.objects.get(flipperUser=flipperUser)
        except MobileUpload.DoesNotExist:
            raise GraphQLError(f"Uploads with ID {flipperUser} does not exist.")
    
    # ---------- Job ----------
    displayJobs = graphene.List(JobType, flipperUser=graphene.String())
    jobsbyid = graphene.Field(JobType, flipperUser=graphene.String())
    def resolve_displayJobs(self, info, flipperUser):
        if flipperUser:
            return JobUpload.objects.exclude(flipperUser=flipperUser)
        else:
            return JobUpload.objects.all()
     
    def resolve_jobsbyid(self, info, flipperUser):
        try:
            return JobUpload.objects.get(flipperUser=flipperUser)
        except JobUpload.DoesNotExist:
            raise GraphQLError(f"Uploads with ID {flipperUser} does not exist.")

    # ---------- Bike ----------
    displayBikes = graphene.List(BikeType, flipperUser=graphene.String())
    bikesbyid = graphene.Field(BikeType, flipperUser=graphene.String())
    def resolve_displayBikes(self, info, flipperUser):
        if flipperUser:
            return BikeUpload.objects.exclude(flipperUser=flipperUser)
        else:
            return BikeUpload.objects.all()
        
    def resolve_bikesbyid(self, info, flipperUser):
        try:
            return BikeUpload.objects.get(flipperUser=flipperUser)
        except BikeUpload.DoesNotExist:
            raise GraphQLError(f"Uploads with ID {flipperUser} does not exist.")

    # ---------- Furniture ----------
    displayFurnitures = graphene.List(FurnitureType, flipperUser=graphene.String())
    furnituresbyid = graphene.Field(FurnitureType, flipperUser=graphene.String())
    def resolve_displayFurnitures(self, info, flipperUser):
        if flipperUser:
            return FurnitureUpload.objects.exclude(flipperUser=flipperUser)
        else:
            return FurnitureUpload.objects.all()
        
    def resolve_furnituresbyid(self, info, flipperUser):
        try:
            return FurnitureUpload.objects.get(flipperUser=flipperUser)
        except FurnitureUpload.DoesNotExist:
            raise GraphQLError(f"Uploads with ID {flipperUser} does not exist.")

    # ---------- Fashion ----------
    displayFashions = graphene.List(FashionType, flipperUser=graphene.String())
    fashionsbyid = graphene.Field(FashionType, flipperUser=graphene.String())
    def resolve_displayFashions(self, info, flipperUser):
        if flipperUser:
            return FashionUpload.objects.exclude(flipperUser=flipperUser)
        else:
            return FashionUpload.objects.all()
        
    def resolve_fashionsbyid(self, info, flipperUser):
        try:
            return FashionUpload.objects.get(flipperUser=flipperUser)
        except FashionUpload.DoesNotExist:
            raise GraphQLError(f"Uploads with ID {flipperUser} does not exist.")

    # ---------- Electronic & Appliances ----------
    displayElectronicAppliances = graphene.List(ElectronicAppliancesType, flipperUser=graphene.String())
    electronicappliancesbyid = graphene.Field(ElectronicAppliancesType, flipperUser=graphene.String())
    def resolve_displayElectronicAppliances(self, info, flipperUser):
        if flipperUser:
            return ElectronicAppliancesUpload.objects.exclude(flipperUser=flipperUser)
        else:
            return ElectronicAppliancesUpload.objects.all()
        
    def resolve_electronicappliancesbyid(self, info, flipperUser):
        try:
            return ElectronicAppliancesUpload.objects.get(flipperUser=flipperUser)
        except ElectronicAppliancesUpload.DoesNotExist:
            raise GraphQLError(f"Uploads with ID {flipperUser} does not exist.")
    
    # ---------- Commercial Vehicles ----------
    displayComms = graphene.List(CommType, flipperUser=graphene.String())
    commsbyid = graphene.Field(CommType, flipperUser=graphene.String())
    def resolve_displayComms(self, info, flipperUser):
        if flipperUser:
            return CommUpload.objects.exclude(flipperUser=flipperUser)
        else:
            return CommUpload.objects.all()
        
    def resolve_commsbyid(self, info, flipperUser):
        try:
            return CommUpload.objects.get(flipperUser=flipperUser)
        except CommUpload.DoesNotExist:
            raise GraphQLError(f"Uploads with ID {flipperUser} does not exist.")
    
    # ---------- Books, Sports & Hobbies ----------
    displayBSHs = graphene.List(BSHType, flipperUser=graphene.String())
    BSHsbyid = graphene.Field(BSHType, flipperUser=graphene.String())
    def resolve_displayBSHs(self, info, flipperUser):
        if flipperUser:
            return BooksSportsHobbiesUpload.objects.exclude(flipperUser=flipperUser)
        else:
            return BooksSportsHobbiesUpload.objects.all()
        
    def resolve_BSHsbyid(self, info, flipperUser):
        try:
            return BooksSportsHobbiesUpload.objects.get(flipperUser=flipperUser)
        except BooksSportsHobbiesUpload.DoesNotExist:
            raise GraphQLError(f"Uploads with ID {flipperUser} does not exist.")

    # ---------- Pet ----------
    displayPets = graphene.List(PetType, flipperUser=graphene.String())
    petsbyid = graphene.Field(PetType, flipperUser=graphene.String())
    def resolve_displayPets(self, info, flipperUser):
        if flipperUser:
            return PetUpload.objects.exclude(flipperUser=flipperUser)
        else:
            return PetUpload.objects.all()
     
    def resolve_petsbyid(self, info, flipperUser):
        try:
            return PetUpload.objects.get(flipperUser=flipperUser)
        except PetUpload.DoesNotExist:
            raise GraphQLError(f"Uploads with ID {flipperUser} does not exist.")

    # ---------- Service ----------
    displayServices = graphene.List(ServiceType, flipperUser=graphene.String())
    servicesbyid = graphene.Field(ServiceType, flipperUser=graphene.String())
    def resolve_displayServices(self, info, flipperUser):
        if flipperUser:
            return ServiceUpload.objects.exclude(flipperUser=flipperUser)
        else:
            return ServiceUpload.objects.all()
     
    def resolve_servicesbyid(self, info, flipperUser):
        try:
            return ServiceUpload.objects.get(flipperUser=flipperUser)
        except ServiceUpload.DoesNotExist:
            raise GraphQLError(f"Uploads with ID {flipperUser} does not exist.")

    # ---------- Favorite ----------
    displayFavbyId = graphene.List(FavoriteType, flipperUser=graphene.String())
    def resolve_displayFavbyId(self, info, flipperUser):
        try:
            return Favorite.objects.filter(flipperUser=flipperUser)
        except Favorite.DoesNotExist:
            raise GraphQLError(f"Favorites with ID {flipperUser} does not exist.")

    # ---------- Rating ----------
    ratingbyid = graphene.Field(RatingType, flipperUser=graphene.String())
    def resolve_ratingbyid(self, info):
        try:
            return Rating.objects.get(flipperUser=flipperUser)
        except Rating.DoesNotExist:
            raise GraphQLError(f"User with ID {flipperUser} does not exist.")
    
    # ---------- Barter ----------
    displayBarters = graphene.List(BarterType, flipperUser=graphene.String())
    bartersbyid = graphene.List(BarterType, flipperUser=graphene.String())
    def resolve_displayBarters(self, info, flipperUser):
        if flipperUser:
            return Barter.objects.exclude(flipperUser=flipperUser)
        else:
            return Barter.objects.all()
    
    def resolve_bartersbyid(self, info, flipperUser):
        try:
            return Barter.objects.filter(flipperUser=flipperUser)
        except Barter.DoesNotExist:
            raise GraphQLError(f"Uploads with ID {flipperUser} does not exist.")
        
class UserUpdate(graphene.Mutation):
    
    user = graphene.Field(UserType)
    
    class Arguments:
        flipperUser = graphene.String(required=True)
        username = graphene.String()
        emailAddress = graphene.String()
        mobileNumber = graphene.String()
        country = graphene.String()
        userLocation = graphene.String()
        userBio = graphene.String()
        
    def mutate(self, info, flipperUser, **kwargs):
        user = User.objects.get(flipperUser=flipperUser)
        for field, value in kwargs.items():
            if value is not None:
                setattr(user, field, value)
        user.save()
        return UserUpdate(user=user)

class DeleteFav(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        flipperUser = graphene.String(required=True)
        id = graphene.ID(required=True)

    def mutate(self, info, flipperUser, id):
        try:
            fav = Favorite.objects.get(flipperUser=flipperUser, id=id)
            fav.delete()
            return DeleteFav(success=True)
        except Favorite.DoesNotExist:
            return DeleteFav(success=False)
    
class Mutation(graphene.ObjectType):
    update_user = UserUpdate.Field()
    delete_fav = DeleteFav.Field()
    
schema = graphene.Schema(query=Query, mutation=Mutation)
    