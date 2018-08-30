from django.db import models

class Post(models.Model):
    post_title = models.CharField(max_length=300) 
    post_text = models.TextField()
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.post_title

class Unit(models.Model):
    name = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=13)
    longitude = models.DecimalField(max_digits=9, decimal_places=7)
    latitude = models.DecimalField(max_digits=9, decimal_places=7)
    def __str__(self):
        return self.name

class Doctor(models.Model):
    name = models.CharField(max_length=300)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    education = models.CharField(max_length=500)
    end_year = models.PositiveSmallIntegerField()
    specialization = models.CharField(default='терапевт', max_length=50)
    qualification = models.CharField(max_length=20)
    start_experience = models.PositiveSmallIntegerField()
    photo = models.ImageField()
    def __str__(self):
        return self.name

class Drug(models.Model):
    drug_name = models.CharField(max_length=300)
    drug_form = models.CharField(max_length=300)
    drug_quantity_type = models.CharField(max_length=300)
    drug_quantity = models.IntegerField()
    drug_date_updated = models.DateField(auto_now=True)
    drug_place = models.ForeignKey(Unit, on_delete=models.CASCADE)
    def __str__(self):
        return self.drug_name


