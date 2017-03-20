from django.contrib.auth.admin import UserAdmin, admin
from SiO.member.models import Member, Association


# class MemberAdmin(UserAdmin):
#     pass


admin.site.register(Member)
