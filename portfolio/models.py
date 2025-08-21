from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    url = models.URLField(blank=True)  # Optional link to live project

    def __str__(self):
        return self.title

class Resume(models.Model):
    file = models.FileField(upload_to='resumes/')
    title = models.CharField(max_length=200, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or f"Resume {self.id}"

class CoverLetter(models.Model):
    file = models.FileField(upload_to='covers/')
    title = models.CharField(max_length=200, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or f"Cover Letter {self.id}"

class Profile(models.Model):
    full_name = models.CharField(max_length=200)
    tagline = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=50, blank=True)
    location = models.CharField(max_length=120, blank=True)
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    accent_color = models.CharField(max_length=7, default="#3fe3ff", help_text="Hex color like #3fe3ff")
    neon_color = models.CharField(max_length=7, default="#7aa2ff", help_text="Hex color like #7aa2ff")

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profile"

    def __str__(self):
        return self.full_name

class Skill(models.Model):
    name = models.CharField(max_length=120)
    proficiency = models.PositiveIntegerField(help_text="0-100")
    category = models.CharField(max_length=120, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "-proficiency", "name"]

    def __str__(self) -> str:
        return f"{self.name} ({self.proficiency}%)"

class HeroImage(models.Model):
    image = models.ImageField(upload_to='hero/')
    order = models.PositiveIntegerField(default=0)
    opacity = models.FloatField(default=0.25, help_text="0.0 - 1.0")

    class Meta:
        ordering = ["order", "id"]

    def __str__(self) -> str:
        return f"HeroImage {self.id}"

# For resume: We'll handle it as a static file or upload once via admin/media.