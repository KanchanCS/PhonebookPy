from django.contrib.auth.models import User  # For user association
from django.db import models


class Contact(models.Model):
    # Basic contact information
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, verbose_name="Email Address")
    phone_number = models.CharField(max_length=20, blank=True)  # Allow for missing numbers

    # Optional address information (more extensible)
    address_line1 = models.CharField(max_length=255, blank=True)
    address_line2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=50, blank=True)
    postal_code = models.CharField(max_length=10, blank=True)
    country = models.CharField(max_length=50, blank=True)

    # Other relevant fields (based on requirements)
    birthday = models.DateField(blank=True, null=True)
    website = models.URLField(blank=True)
    notes = models.TextField(blank=True)

    # Many-to-many relationship with categories (for flexible grouping)
    categories = models.ManyToManyField('Category', blank=True)

    # Optional user association (for secure contact management)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def str(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        unique_together = ('user', 'phone_number',)
    

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def str(self):
        return self.name
    
    
