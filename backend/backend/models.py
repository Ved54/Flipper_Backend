from django.db import models

class FileField(models.FileField):
    def value_to_string(self, obj):
        return obj.file.url

# ---------- User Model ----------
class User(models.Model):
    flipperUser = models.CharField(max_length=200, default='')
    username = models.CharField(max_length=255, default='')
    emailAddress = models.EmailField(max_length=100, default='')
    mobileNumber = models.CharField(max_length=20, default='')
    country = models.CharField(max_length=50, default='')
    userLocation = models.CharField(max_length=200, default='')
    userBio = models.CharField(max_length=1000, default='')

    def __str__(self) -> str:
        return f"{self.id} : {self.flipperUser} : {self.username}"
    
# ---------- Car Model ----------
class CarUpload(models.Model):
    flipperUser = models.CharField(max_length=200, default='')
    flipperType = models.CharField(max_length=50, default='Car')
    carBrand = models.CharField(max_length=100, default='')
    carModel = models.CharField(max_length=100, default='')
    carVariant = models.CharField(max_length=100, default='')
    carYear = models.CharField(max_length=100, default='')
    carFuelType = models.CharField(max_length=100, default='')
    carTransmission = models.CharField(max_length=100, default='')
    carKmDriven = models.CharField(max_length=50, default='')
    carOwnerNum = models.CharField(max_length=100, default='')
    carDescription = models.CharField(max_length=100000, default='')
    carLocation = models.CharField(max_length=200, default='')
    carPrice = models.CharField(max_length=20, default='')
    carImage = FileField(upload_to='CarImages/', blank=True, default='')
    
    def __str__(self) -> str:
        return f"{self.id} : {self.flipperUser} : {self.carBrand} {self.carModel} {self.carVariant}"
    
# ---------- Property Model ----------
class PropertyUpload(models.Model):
    flipperUser = models.CharField(max_length=200, default='')
    flipperType = models.CharField(max_length=50, default='Property')
    propertyType = models.CharField(max_length = 50, default='')
    propertyTitle = models.CharField(max_length=200, default='')
    propertyDescription = models.CharField(max_length = 100000, default='')
    propertyLocation = models.CharField(max_length=200, default='')
    propertyPrice = models.CharField(max_length=20, default='')
    propertyImage = FileField(upload_to='PropertyImages/', blank=True, default='')
    
    def __str__(self) -> str:
        return f"{self.id} : {self.flipperUser} : {self.propertyTitle}"
    
# ---------- Mobile Model ----------
class MobileUpload(models.Model):
    flipperUser = models.CharField(max_length=200, default='')
    flipperType = models.CharField(max_length=50, default='Mobile')
    accessoryType = models.CharField(max_length=50, default='')
    mobileBrand = models.CharField(max_length=200, default='')
    mobileTitle = models.CharField(max_length=200, default='')
    mobileDescription = models.CharField(max_length = 100000, default='')
    mobileLocation = models.CharField(max_length=200, default='')
    mobilePrice = models.CharField(max_length=20, default='')
    mobileImage = FileField(upload_to='MobileImages/', blank=True, default='')
    
    def __str__(self) -> str:
        return f"{self.id} : {self.flipperUser} : {self.mobileTitle}"
    
# ---------- Job Model ----------
class JobUpload(models.Model):
    flipperUser = models.CharField(max_length=200, default='')
    flipperType = models.CharField(max_length=50, default='Job')
    jobType = models.CharField(max_length=200, default='')
    jobTitle = models.CharField(max_length=200, default='')
    salaryPeriod = models.CharField(max_length=200, default='')
    positionType = models.CharField(max_length=200, default='')
    salaryRange = models.CharField(max_length=200, default='')
    jobDescription = models.CharField(max_length=200000, default='')
    jobLocation = models.CharField(max_length=200, default='')
    jobImage = FileField(upload_to='JobImages/', blank=True, default='')
    
    def __str__(self) -> str:
        return f"{self.id} : {self.flipperUser} : {self.jobType}"
    
# ---------- Bike Model ----------
class BikeUpload(models.Model):
    flipperUser = models.CharField(max_length=200, default='')
    flipperType = models.CharField(max_length=50, default='Bike')
    bikeType = models.CharField(max_length=50, default='')
    spareTitle = models.CharField(max_length=200, default='')
    cycleTitle = models.CharField(max_length=200, default='')
    bikeBrand = models.CharField(max_length=100, default='')
    bikeModel = models.CharField(max_length=100, default='')
    bikeYear = models.CharField(max_length=100, default='')
    bikeKmDriven = models.CharField(max_length=50, default='')
    bikeOwnerNum = models.CharField(max_length=100, default='')
    bikeDescription = models.CharField(max_length=100000, default='')
    bikeLocation = models.CharField(max_length=200, default='')
    bikePrice = models.CharField(max_length=20, default='')
    bikeImage = FileField(upload_to='BikeImages/', blank=True, default='')
    
    def __str__(self) -> str:
        return f"{self.id} : {self.flipperUser} : {self.bikeType}"
    
# ---------- Furniture Model ----------
class FurnitureUpload(models.Model):
    flipperUser = models.CharField(max_length=200, default='')
    flipperType = models.CharField(max_length=50, default='Furniture')
    furnitureType = models.CharField(max_length=50, default='')
    furnitureTitle = models.CharField(max_length=200, default='')
    furnitureDescription = models.CharField(max_length=100000, default='')
    furnitureLocation = models.CharField(max_length=200, default='')
    furniturePrice = models.CharField(max_length=20, default='')
    furnitureImage = FileField(upload_to='FurnitureImages/', blank=True, default='')
    
    def __str__(self) -> str:
        return f"{self.id} : {self.flipperUser} : {self.furnitureTitle}" 
    
# ---------- Fashion Model ---------- 
class FashionUpload(models.Model):
    flipperUser = models.CharField(max_length=200, default='')
    flipperType = models.CharField(max_length=50, default='Fashion')
    fashionType = models.CharField(max_length=50, default='')
    fashionTitle = models.CharField(max_length=200, default='')
    fashionDescription = models.CharField(max_length=100000, default='')
    fashionLocation = models.CharField(max_length=200, default='')
    fashionPrice = models.CharField(max_length=20, default='')
    fashionImage = FileField(upload_to='FashionImages/', blank=True, default='')
    
    def __str__(self) -> str:
        return f"{self.id} : {self.flipperUser} : {self.fashionTitle}" 
    
# ---------- Electronics & Appliances Model ----------  
class ElectronicAppliancesUpload(models.Model):
    flipperUser = models.CharField(max_length=200, default='')
    flipperType = models.CharField(max_length=50, default='Electronics Appliances')
    elecType = models.CharField(max_length=50, default='')
    elecTitle = models.CharField(max_length=200, default='')
    elecDescription = models.CharField(max_length=100000, default='')
    elecLocation = models.CharField(max_length=200, default='')
    elecPrice = models.CharField(max_length=20, default='')
    elecImage = FileField(upload_to='ElecAppImages/', blank=True, default='')
    
    def __str__(self) -> str:
        return f"{self.id} : {self.flipperUser} : {self.elecType}" 
    
# ---------- Commercial Model ----------
class CommUpload(models.Model):
    flipperUser = models.CharField(max_length=200, default='')
    flipperType = models.CharField(max_length=50, default='Commercial Vehicle')
    commType = models.CharField(max_length=50, default='')
    spareTitle = models.CharField(max_length=200, default='')
    commTitle = models.CharField(max_length=200, default='')
    commBrand = models.CharField(max_length=100, default='')
    commYear = models.CharField(max_length=100, default='')
    commKmDriven = models.CharField(max_length=50, default='')
    commDescription = models.CharField(max_length=100000, default='')
    commLocation = models.CharField(max_length=200, default='')
    commPrice = models.CharField(max_length=20, default='')
    commImage = FileField(upload_to='CommImages/', blank=True, default='')
    
    def __str__(self) -> str:
        return f"{self.id} : {self.flipperUser} : {self.commType}" 

# ---------- Books, Sports $ Hobbies Model ----------
class BooksSportsHobbiesUpload(models.Model):
    flipperUser = models.CharField(max_length=200, default='')
    flipperType = models.CharField(max_length=50, default='BookSportsHobbies')
    bshType = models.CharField(max_length=50, default='')
    bshTitle = models.CharField(max_length=200, default='')
    bshDescription = models.CharField(max_length=2000000, default='')
    bshLocation = models.CharField(max_length=200, default='')
    bshPrice = models.CharField(max_length=20, default='')
    bshImage = FileField(upload_to='BSHImages/', blank=True, default='')
    
    def __str__(self) -> str:
        return f"{self.id} : {self.flipperUser} : {self.bshType}"
    
# ---------- Pet Model ----------
class PetUpload(models.Model):
    flipperUser = models.CharField(max_length=200, default='')
    flipperType = models.CharField(max_length=50, default='Pet')
    petType = models.CharField(max_length=50, default='')
    petTitle = models.CharField(max_length=200, default='')
    petDescription = models.CharField(max_length=2000000, default='')
    petLocation = models.CharField(max_length=200, default='')
    petPrice = models.CharField(max_length=20, default='')
    petImage = FileField(upload_to='PetImages/', blank=True, default='')
    
    def __str__(self) -> str:
        return f"{self.id} : {self.flipperUser} : {self.petTitle}"
    
# ---------- Service Model ----------
class ServiceUpload(models.Model):
    flipperUser = models.CharField(max_length=200, default='')
    flipperType = models.CharField(max_length=50, default='Service')
    serviceType = models.CharField(max_length=200, default='')
    serviceTitle = models.CharField(max_length=200, default='')
    serviceDescription = models.CharField(max_length=2000000, default='')
    serviceLocation = models.CharField(max_length=200, default='')
    serviceImage = FileField(upload_to='ServiceImages/', blank=True, default='')
    
    def __str__(self) -> str:
        return f"{self.id} : {self.flipperUser} : {self.serviceType}"
    
# ---------- Favorites Model (Products) ----------
class Favorite(models.Model):
    flipperUser = models.CharField(max_length=200, default='')
    flipperType = models.CharField(max_length=50, default='')
    carId = models.ForeignKey(CarUpload, on_delete=models.CASCADE, null=True)
    propertyId = models.ForeignKey(PropertyUpload, on_delete=models.CASCADE, null=True)
    mobileId = models.ForeignKey(MobileUpload, on_delete=models.CASCADE, null=True)
    jobId = models.ForeignKey(JobUpload, on_delete=models.CASCADE, null=True)
    bikeId = models.ForeignKey(BikeUpload, on_delete=models.CASCADE, null=True)
    furnitureId = models.ForeignKey(FurnitureUpload, on_delete=models.CASCADE, null=True)
    fashionId = models.ForeignKey(FashionUpload, on_delete=models.CASCADE, null=True)
    elecId = models.ForeignKey(ElectronicAppliancesUpload, on_delete=models.CASCADE, null=True)
    commId = models.ForeignKey(CommUpload, on_delete=models.CASCADE, null=True)
    bshId = models.ForeignKey(BooksSportsHobbiesUpload, on_delete=models.CASCADE, null=True)
    petId = models.ForeignKey(PetUpload, on_delete=models.CASCADE, null=True)
    serviceId = models.ForeignKey(ServiceUpload, on_delete=models.CASCADE, null=True)
    
    def __str__(self) -> str:
        return f"{self.id} : {self.flipperUser} : {self.flipperType}"
        
# ---------- Ratings Model ----------
class Rating(models.Model):
    flipperUser = models.CharField(max_length=200, default='')
    rating = models.FloatField(default=0.00)
    rates = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return f"{self.id} : {self.flipperUser} : {self.rating}"
    
# ---------- Barter Model ----------
class Barter(models.Model):
    flipperUser = models.CharField(max_length=200, default='')
    barterTitle = models.CharField(max_length=200, default='')
    barterDescription = models.CharField(max_length=2000000, default='')
    barterRequirement = models.CharField(max_length=2000000, default='')
    barterLocation = models.CharField(max_length=200, default='')
    barterImage = FileField(upload_to='BarterImages/', blank=True, default='')
    
    def __str__(self) -> str:
        return f"{self.id} : {self.flipperUser} : {self.barterTitle}"
    
# ---------- Favorites Model (Barter) ----------
class FavoriteBarter(models.Model):
    flipperUser = models.CharField(max_length=200, default='')
    barterId = models.ForeignKey(Barter, on_delete=models.CASCADE, null=True)
    
    def __str__(self) -> str:
        return f"{self.id} : {self.flipperUser}"