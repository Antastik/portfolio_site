from django.shortcuts import render
from .models import Project, Resume, CoverLetter, Profile, Skill, HeroImage

def home(request):
    projects = Project.objects.all()
    resume = Resume.objects.filter(is_active=True).order_by('-created_at').first()
    cover = CoverLetter.objects.filter(is_active=True).order_by('-created_at').first()
    profile = Profile.objects.first()
    skills = Skill.objects.all()
    hero_images = HeroImage.objects.all()
    context = {
        'projects': projects,
        'resume': resume,
        'cover': cover,
        'profile': profile,
        'skills': skills,
        'hero_images': hero_images,
    }
    return render(request, 'portfolio/home.html', context)