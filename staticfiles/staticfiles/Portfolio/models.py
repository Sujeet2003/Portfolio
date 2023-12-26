from django.db import models

class ContactUs(models.Model):
    name = models.CharField(max_length=30)
    phone = models.IntegerField()
    email = models.EmailField()
    description = models.TextField()
    # created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email