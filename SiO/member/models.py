from django.db import models
from django.conf import settings
from dedal.decorators import crud

# TODO: Her lages det database modeller Member, Association, member_asoc, Expense, member_expense


@crud
class Member(models.Model):
    # payment_id = models.AutoField(primary_key=True)
    # member_no = models.IntegerField(unique=True)
    member_no = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    student_status = models.BooleanField(default=False)
    reg_date = models.DateTimeField(null=True, blank=True)
    gender = models.CharField(max_length=50, null=True, blank=True)
    birthday = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'Member'


class Association(models.Model):
    asocnumber_id = models.AutoField(primary_key=True)
    # asocnumber_id = models.OneToOneField(Member, primary_key=True)
    asoc_name = models.CharField(max_length=50, null=True, blank=True)
    asoc_stardate = models.DateTimeField(null=True, blank=True)
    trans_id = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = 'Association'


class member_asoc(models.Model):
    asocnmember_id = models.AutoField(primary_key=True)
    asocnumber_id = models.OneToOneField(Association)
    member_no = models.OneToOneField(Member)
    join_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'member_asoc'


class Expense(models.Model):
    expensenumber_id = models.AutoField(primary_key=True)
    asocnumber_id = models.OneToOneField(Association)
    trans_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'Expense'


class member_expense(models.Model):
    # TODO: Er asocnumber_id strengt tatt nødvendig? Den blir litt annerledes fra den forrige modelen
    asocnumber_id = models.OneToOneField(Association)
    expensenumber_id = models.OneToOneField(Expense)
    payment_id = models.OneToOneField(Member)

    class Meta:
        db_table = 'member_expense'


