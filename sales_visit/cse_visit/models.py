from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db.models.signals import post_save
from django.dispatch import receiver


class Active(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    is_logged_in = models.BooleanField(default=False)
    name = models.CharField(max_length=20,null=True,blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Active.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.active.save()


class Branch(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        db_table = 'branch'
        verbose_name_plural = 'branch'

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        db_table = 'status'
        verbose_name_plural = 'status'

    def __str__(self):
        return self.name


class CustomerVisitDetails(models.Model):
    customer_name = models.CharField(max_length=20, null=True, blank=True)
    customer_address = models.TextField(max_length=2000, null=True, blank=True)
    branch = models.ForeignKey(Branch, on_delete=models.DO_NOTHING)
    assigned_cse = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    visit_date = models.DateField(null=True, blank=True)
    status = models.ForeignKey(Status, on_delete=models.DO_NOTHING)
    attachment = models.FileField(upload_to='documents/', validators=[FileExtensionValidator(allowed_extensions=['pdf'])], null=True, blank=True)
    is_submitted = models.BooleanField(default=False)

    class Meta:
        db_table = 'customer_detail'
        verbose_name_plural = 'customer_detail'

    def __str__(self):
        return self.customer_name


class CustomerAssignment(models.Model):
    sales_person = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    branch = models.ForeignKey(Branch, on_delete=models.DO_NOTHING)
    customer = models.ForeignKey(CustomerVisitDetails, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'customer_assignment'
        verbose_name_plural = 'customer_assignment'

    def __str__(self):
        return f"{self.sales_person.username}_{self.customer.customer_name}"
