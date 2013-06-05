from django.contrib import admin

from .models import LocationType
from .models import Phone
from .models import Address
from .models import Email
from .models import Person
from .models import Company
from .models import WebSite
from .models import Group
from .models import CustomData
from .models import IdentityData

admin.site.register(LocationType)
admin.site.register(Phone)
admin.site.register(Address)
admin.site.register(Email)
admin.site.register(WebSite)
admin.site.register(Group)
admin.site.register(CustomData)
admin.site.register(IdentityData)

admin.site.register(Person)
admin.site.register(Company)
