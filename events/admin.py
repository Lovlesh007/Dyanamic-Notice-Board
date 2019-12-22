from django.contrib import admin
from . models import Mymodel
from . models import Mymodel2
from . models import Mymodel3
from . models import Email
#from . models import Question

# Register your models here.
admin.site.register(Mymodel)
admin.site.register(Mymodel2)
admin.site.register(Mymodel3)
admin.site.register(Email)
#admin.site.register(Question)