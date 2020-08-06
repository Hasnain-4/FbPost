from django.contrib import admin
from fb1.models import Contact,Imagepost,Videopost, Userprofile,Postcomment

# Register your models here.
admin.site.register(Contact)
admin.site.register(Imagepost)
admin.site.register(Videopost)
admin.site.register(Userprofile)
admin.site.register(Postcomment)
