from django.contrib import admin
from .models import Project, Resume, Profile, CoverLetter, Skill, HeroImage

admin.site.register(Project)
admin.site.register(Resume)
admin.site.register(Profile)
admin.site.register(CoverLetter)
admin.site.register(Skill)
admin.site.register(HeroImage)