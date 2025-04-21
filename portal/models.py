from django.contrib.auth.models import AbstractUser
from django.conf import settings  # ✅ needed for AUTH_USER_MODEL
from django.db import models

# --------------------------
# Custom User Model
# --------------------------
class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('staff', 'Staff'),
        ('admin', 'Admin'),
    ]

    DEPARTMENT_CHOICES = [
        ('Admin', 'Admin'),
        ('IT', 'IT'),
        ('Infrastructure', 'Infrastructure'),
        ('Electrical', 'Electrical'),
        ('House keeping', 'House keeping'),
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')
    department = models.CharField(max_length=100, choices=DEPARTMENT_CHOICES, blank=True, null=True)

    REQUIRED_FIELDS = ['email']
# --------------------------
# Complaint Model
# --------------------------
class Complaint(models.Model):
    complaint_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True) 
    user_email = models.EmailField(null=True, blank=True)
    title = models.CharField(max_length=200)
    discription = models.CharField(max_length=200)
    status = models.CharField(max_length=100, null=True, blank=True)
    faculty = models.CharField(max_length=200)
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to='complaint_images/', blank=True, null=True)
    pub_date = models.DateTimeField('Date Published')

    def __str__(self):
        return f"{self.title} - {self.faculty}"


    



    
