

from django.db import models
from apps.master_data.currency.models.currency_models import Currency

class Country(models.Model):
    country_id = models.AutoField(primary_key=True)

    currency = models.ForeignKey(
        Currency,
        on_delete=models.CASCADE,
        related_name="countries",
        null=True,
        blank=True
    )

    country_code = models.CharField(max_length=3)
    country_name = models.CharField(max_length=100)

    iso = models.CharField(max_length=3, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)

    default_time_zone = models.CharField(max_length=50, null=True, blank=True)
    default_language = models.CharField(max_length=20, null=True, blank=True)
    date_format = models.CharField(max_length=20, null=True, blank=True)

    allow_asset_location = models.BooleanField(default=True)
    default_country = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



from  django.db import models




class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    

    currency = models.ForeignKey(
        Currency, 
         on_delete=models.CASCADE, 
         null=True, 
         blank=True,
         related_name='countries' 
    )
    
    country_code = models.CharField(max_length=3)
    country_name = models.CharField(max_length=100)
    iso = models.CharField(max_length=3, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    default_time_zone = models.CharField(max_length=50, null=True, blank=True)
    default_language = models.CharField(max_length=20, null=True, blank=True)
    date_format = models.CharField(max_length=20, null=True, blank=True)
    
    allow_asset_location = models.BooleanField(default=True)
    default_country = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.CharField(max_length=100, null=True, blank=True)
    updated_by = models.CharField(max_length=100, null=True, blank=True)

    class Meta:

        db_table = 'country'
    def __str__(self):
        return self.country_name

