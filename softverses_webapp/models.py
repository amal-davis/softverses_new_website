from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify


from django.utils.text import slugify


class ContactMessage(models.Model):
    first_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.first_name} {self.last_name}"

class CenterSection(models.Model):
    heading = models.CharField(max_length=100)
    subheading = models.CharField(max_length=100)
    paragraph = models.TextField()
    button_text = models.CharField(max_length=255, blank=True, default='Default Button Text')
    button_url = models.URLField(blank=True, default='https://example.com')
    def __str__(self):
        return self.heading


class ClientLogo(models.Model):
    image = models.ImageField(upload_to='client_logos/', help_text="Upload the client logo image")
    alt_text = models.CharField(max_length=100, help_text="Alt text for the image")

    def __str__(self):
        return self.name
    

class MissionVision(models.Model):
    title = models.CharField(max_length=100, help_text="Title (e.g., 'Our Mission', 'Our Vision')")
    description = models.TextField(help_text="Description for the mission or vision")
    link_url = models.URLField(blank=True, null=True, help_text="Optional link for the arrow link")

    def __str__(self):
        return self.title

class WebDesign(models.Model):
    image = models.ImageField(upload_to='web_designs/', help_text="Upload the design image")
    alt_text = models.CharField(max_length=100, help_text="Alt text for the image")

    def __str__(self):
        return self.title


class FAQ(models.Model):
    question = models.CharField(max_length=255, help_text="Enter the FAQ question")
    answer = models.TextField(help_text="Enter the FAQ answer")

    def __str__(self):
        return self.question


class Aboutus_intro(models.Model):
    image = models.ImageField(upload_to='digital_transformation/', help_text="Upload the image for the section")
    heading = models.CharField(max_length=200, help_text="Enter the main heading")
    paragraph = models.TextField(help_text="Enter the main paragraph")
    highlight_text = models.CharField(max_length=100, help_text="Highlight text for emphasis")
   
    def __str__(self):
        return self.heading
    
class About_Testimonial(models.Model):
    question = models.CharField(max_length=255, help_text="Enter the question text")
    content = models.TextField(help_text="Enter the testimonial content")

    def __str__(self):
        return self.question


class WhyChooseUs(models.Model):
    title = models.CharField(max_length=200, help_text="Enter the main title")
    sub_title = models.CharField(max_length=200, help_text="Enter the subtitle")
    left_heading = models.CharField(max_length=200, help_text="Heading for the left text block")
    left_description = models.TextField(help_text="Description for the left text block")
    right_heading = models.CharField(max_length=200, help_text="Heading for the right text block")
    right_description = models.TextField(help_text="Description for the right text block")

    def __str__(self):
        return self.title


class Portfolio(models.Model):
    heading = models.CharField(max_length=100, help_text="heading of the portfolio item")
    paragraph = models.TextField(help_text="Paragraph of the portfolio item")
    image = models.ImageField(upload_to='portfolio/', help_text="Upload an image for the portfolio item")
    link = models.URLField(max_length=500, blank=True, help_text="Link to redirect when clicked")
   
    def __str__(self):
        return self.title


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/')
    author = models.CharField(max_length=100, default='none')  # Allow blank author for default
    created_at = models.DateTimeField(default=timezone.now)  # Use timezone.now for default date
    slug = models.SlugField(max_length=200, unique=True, help_text="Enter the blog slug", blank=True)
   
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(BlogPost, self).save(*args, **kwargs)

    def __str__(self):
        return self.title