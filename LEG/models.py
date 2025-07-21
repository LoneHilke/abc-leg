from django.db import models

# Create your models here.
class A(models.Model):
    image = models.ImageField(upload_to='images/')
    ord = models.CharField(max_length=50)
    beskrivelse = models.TextField(blank=True)

    def __str__(self):
        return self.ord
    
class B(models.Model):
    image = models.ImageField(upload_to='images/')
    ord = models.CharField(max_length=50)
    beskrivelse = models.TextField(blank=True)

    def __str__(self):
        return self.ord
    
class C(models.Model):
    image = models.ImageField(upload_to='images/')
    ord = models.CharField(max_length=50)
    beskrivelse = models.TextField(blank=True)

    def __str__(self):
        return self.ord
    
class D(models.Model):
    image = models.ImageField(upload_to='images/')
    ord = models.CharField(max_length=50)
    beskrivelse = models.TextField(blank=True)

    def __str__(self):
        return self.ord
    
class E(models.Model):
    image = models.ImageField(upload_to='images/')
    ord = models.CharField(max_length=50)
    beskrivelse = models.TextField(blank=True)

    def __str__(self):
        return self.ord