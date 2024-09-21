
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from .manager import StaffAuthManager, StaffAdminManager

# Create your models here.

# model for admin
class StaffAdmin(AbstractBaseUser, PermissionsMixin):
    groups = None
    user_permissions = None
    email = models.EmailField(unique=True, blank=False)
    date_created = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    
    objects = StaffAdminManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.email
    


#Model for normal Staff

class StaffAuth(AbstractBaseUser, PermissionsMixin):
    groups = None
    user_permissions = None
    last_login = None
    full_name = models.CharField( max_length=150, blank=False)
    email = models.EmailField( blank=False, unique=True)
    data_created = models.DateTimeField( default= timezone.now)

    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_supervisor = models.BooleanField(default=False)
    
    objects = StaffAuthManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["full_name", "is_supervisor"]
    
    def __str__(self):
        return self.email 
    
class SupervisorRelationship(models.Model):
    supervisor_id = models.ForeignKey(StaffAuth, on_delete=models.CASCADE, blank=False, related_name='supervised_relationships_as_supervisor')
    staff_id = models.ForeignKey(StaffAuth, on_delete=models.CASCADE, blank=False, related_name='supervised_relationships_as_staff')

    def __str__(self):
        return f"Supervisor Relationship ID: {self.supervisor_id}"
    

# class StaffProfile:
#     staff_id = models.OneToOneField(StaffAuth, on_delete=models.CASCADE, blank=False, related_name='Staff_profile')

#     def __str__(self):
#         return f"Supervisor Relationship ID: {self.staff_id}"

