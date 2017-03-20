from django.db import models
from django import forms
from django.conf import settings
from dedal.decorators import crud
# from SiO.CoAdmin.models import Administrator
from django.db.models.signals import post_save


# TODO: Her lages det database modeller Member, Association, member_asoc, Expense, member_expense


# @crud
class Member(models.Model):
    # payment_id = models.AutoField(primary_key=True)
    # member_no = models.IntegerField(unique=True)
    member_no = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)

    # asoc_name = models.CharField(max_length=50)
    association = models.ForeignKey('Association')

    student_status = models.CharField(max_length=50, default=False)
    reg_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=50, null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    # asocnumber = models.ForeignKey('Association')
    # user = models.OneToOneField(Administrator)

    class Meta:
        db_table = 'Member'
# TODO: dette vises i admin istedenfor "Member object"

    def __str__(self):
        return self.first_name + ' ' + self.last_name


# def create_user_member(sender, instance, created, **kwargs):
#         if created:
#             Association.objects.create(asocnumber=instance)


# def save_user_member(sender, instance, **kwargs):
#         instance.profile.save()

# post_save.connect(create_user_member)
# post_save.connect(save_user_member)


class Association(models.Model):
    # asocnumber = models.AutoField(primary_key=True)
    # asocnumber_id = models.OneToOneField(Member, primary_key=True)
    asoc_name = models.CharField(max_length=50, null=True, blank=True)
    # asoc_stardate = models.DateTimeField(null=True, blank=True)
    # trans_id = models.CharField(max_length=50, null=True, blank=True)
    # user = models.ForeignKey(Administrator, related_name='user')

    # user = models.ForeignKey(Administrator)

    # member_no = models.ForeignKey(Member)

    class Meta:
        db_table = 'Association'

    def __str__(self):
        return self.asoc_name


# def create_asoc_id(sender, instance, created, **kwargs):
#         if created:
#             Association.objects.create(user=instance)
#             # Association.objects.create(asoc_name=instance)
#             # Administrator.objects.create(asoc_name='asoc_name')
#             Administrator.objects.created(asocnumber=instance)
#
#
# def create_asoc_name(sender, instance, created, **kwargs):
#     if created:
#         Administrator.objects.create(asoc_name=instance)
#
#
# def save_asoc_id(sender, instance, **kwargs):
#         instance.profile.save()
#
# post_save.connect(create_asoc_id, sender=Administrator)
# post_save.connect(save_asoc_id, sender=Administrator)
# post_save.connect(create_asoc_name, sender=Administrator)


# class member_asoc(models.Model):
#     # asocnmember_id = models.AutoField(primary_key=True)
#     asocnumber = models.OneToOneField(Association)
#     member_no = models.OneToOneField(Member)
#     # user = models.OneToOneField(Administrator)
#     join_date = models.DateTimeField(null=True, blank=True)
#     end_date = models.DateTimeField(null=True, blank=True)
#
#     class Meta:
#         db_table = 'member_asoc'


# class Expense(models.Model):
#     expensenumber_id = models.AutoField(primary_key=True)
#     asocnumber_id = models.OneToOneField(Association)
#     trans_date = models.DateTimeField(null=True, blank=True)
#
#     class Meta:
#         db_table = 'Expense'
#
#
# class member_expense(models.Model):
#     # TODO: Er asocnumber_id strengt tatt nødvendig? Den blir litt annerledes fra den forrige modelen
#     asocnumber_id = models.OneToOneField(Association)
#     expensenumber_id = models.OneToOneField(Expense)
#     # payment_id = models.OneToOneField(Member)
#
#     class Meta:
#         db_table = 'member_expense'


