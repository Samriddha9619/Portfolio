from django.db import models
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.snippets.models import register_snippet
from colorfield.fields import ColorField


class HomePage(AbstractEmailForm):
    """Portfolio homepage with all sections"""
    
    # Personal Info
    first_name = models.CharField(max_length=100, default='Your')
    last_name = models.CharField(max_length=100, default='Name')
    professional_title = models.CharField(max_length=200, blank=True, default='')
    profile_photo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    about = RichTextField(blank=True)
    
    # Contact form
    thank_you_text = RichTextField(blank=True, default="Thank you for your message!")
    
    # Social Media Links
    linkedin_url = models.URLField(blank=True, help_text="Your LinkedIn profile URL")
    github_url = models.URLField(blank=True, help_text="Your GitHub profile URL")
    twitter_url = models.URLField(blank=True, help_text="Your Twitter/X profile URL")
    email = models.EmailField(blank=True, help_text="Your public email address")
    
    def get_merged_contributions_count(self):
        """Count merged contributions"""
        return self.contributions.filter(status='merged').count()
    
    def get_open_contributions_count(self):
        """Count open/active contributions"""
        return self.contributions.filter(status='open').count()
    
    content_panels = AbstractEmailForm.content_panels + [
        MultiFieldPanel([
            FieldPanel('first_name'),
            FieldPanel('last_name'),
            FieldPanel('professional_title'),
            FieldPanel('profile_photo'),
        ], heading="Personal Info"),
        FieldPanel('about'),
        InlinePanel('books', label="Learning Journey (Books)"),
        InlinePanel('skills', label="Skills"),
        InlinePanel('contributions', label="Open Source Contributions"),
        InlinePanel('experiences', label="Experience"),
        InlinePanel('projects', label="Projects"),
        InlinePanel('education_items', label="Education"),
        InlinePanel('publications', label="Publications"),
        MultiFieldPanel([
            FieldPanel('linkedin_url'),
            FieldPanel('github_url'),
            FieldPanel('twitter_url'),
            FieldPanel('email'),
        ], heading="Social Media & Contact"),
        MultiFieldPanel([
            InlinePanel('form_fields', label="Form fields"),
            FieldPanel('thank_you_text'),
            FieldPanel('to_address'),
            FieldPanel('from_address'),
            FieldPanel('subject'),
        ], heading="Contact Form"),
    ]
    
    max_count = 1
    
    class Meta:
        verbose_name = "Home Page"


class Skill(Orderable):
    """Skills section"""
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100, blank=True, help_text="Icon class or emoji")
    
    panels = [
        FieldPanel('name'),
        FieldPanel('icon'),
    ]
    
    def __str__(self):
        return self.name


class Experience(Orderable, ClusterableModel):
    """Work experience section"""
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='experiences')
    job_title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True, help_text="Leave blank for current position")
    description = RichTextField(blank=True)
    achievement_1 = models.TextField(blank=True)
    achievement_2 = models.TextField(blank=True)
    achievement_3 = models.TextField(blank=True)
    achievement_4 = models.TextField(blank=True)
    
    panels = [
        FieldPanel('job_title'),
        FieldPanel('company'),
        FieldPanel('location'),
        FieldPanel('start_date'),
        FieldPanel('end_date'),
        FieldPanel('description'),
        FieldPanel('achievement_1'),
        FieldPanel('achievement_2'),
        FieldPanel('achievement_3'),
        FieldPanel('achievement_4'),
        InlinePanel('technologies', label="Technologies used"),
    ]
    
    def __str__(self):
        return f"{self.job_title} at {self.company}"


@register_snippet
class Technology(models.Model):
    """Reusable technology tags"""
    name = models.CharField(max_length=100, unique=True)
    color = ColorField(default='#4A90E2')
    
    panels = [
        FieldPanel('name'),
        FieldPanel('color'),
    ]
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Technologies"
        ordering = ['name']


class ExperienceTechnology(Orderable):
    """Technologies used in experience"""
    experience = ParentalKey(Experience, on_delete=models.CASCADE, related_name='technologies')
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE)
    
    panels = [
        FieldPanel('technology'),
    ]


class Project(Orderable, ClusterableModel):
    """Projects section"""
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=200)
    description = RichTextField()
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    demo_url = models.URLField(blank=True)
    source_url = models.URLField(blank=True)
    date = models.DateField(null=True, blank=True)
    
    panels = [
        FieldPanel('title'),
        FieldPanel('description'),
        FieldPanel('image'),
        FieldPanel('demo_url'),
        FieldPanel('source_url'),
        FieldPanel('date'),
        InlinePanel('technologies', label="Technologies used"),
    ]
    
    def __str__(self):
        return self.title


class ProjectTechnology(Orderable):
    """Technologies used in project"""
    project = ParentalKey(Project, on_delete=models.CASCADE, related_name='technologies')
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE)
    
    panels = [
        FieldPanel('technology'),
    ]


class Education(Orderable):
    """Education section"""
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='education_items')
    degree = models.CharField(max_length=200)
    field_of_study = models.CharField(max_length=200, blank=True)
    institution = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    gpa = models.CharField(max_length=50, blank=True, help_text="e.g., 3.8/4.0")
    description = RichTextField(blank=True)
    
    panels = [
        FieldPanel('degree'),
        FieldPanel('field_of_study'),
        FieldPanel('institution'),
        FieldPanel('location'),
        FieldPanel('start_date'),
        FieldPanel('end_date'),
        FieldPanel('gpa'),
        FieldPanel('description'),
    ]
    
    def __str__(self):
        return f"{self.degree} - {self.institution}"


class Book(Orderable):
    """Books/Learning Journey section"""
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='books')
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=200)
    status = models.CharField(
        max_length=20,
        choices=[
            ('reading', '📖 Currently Reading'),
            ('completed', '✅ Completed'),
            ('planned', '📚 Want to Read'),
        ],
        default='reading'
    )
    start_date = models.DateField(null=True, blank=True)
    finish_date = models.DateField(null=True, blank=True)
    rating = models.IntegerField(
        null=True, 
        blank=True,
        choices=[(i, f'{i} ⭐') for i in range(1, 6)],
        help_text="Rate out of 5 stars"
    )
    key_takeaways = RichTextField(blank=True, help_text="What you learned from this book")
    book_url = models.URLField(blank=True, help_text="Link to Goodreads, Amazon, etc.")
    
    panels = [
        FieldPanel('title'),
        FieldPanel('author'),
        FieldPanel('status'),
        FieldPanel('start_date'),
        FieldPanel('finish_date'),
        FieldPanel('rating'),
        FieldPanel('key_takeaways'),
        FieldPanel('book_url'),
    ]
    
    class Meta:
        ordering = ['-start_date']
    
    def __str__(self):
        return f"{self.title} by {self.author}"


class Contribution(Orderable):
    """Open Source Contributions section"""
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='contributions')
    project_name = models.CharField(max_length=200, help_text="e.g., Django, React, etc.")
    title = models.CharField(max_length=300, help_text="Brief description of your contribution")
    description = RichTextField(blank=True, help_text="Detailed explanation of what you contributed")
    pr_url = models.URLField(verbose_name="Pull Request URL")
    status = models.CharField(
        max_length=20,
        choices=[
            ('merged', 'Merged ✅'),
            ('open', 'Open'),
            ('closed', 'Closed'),
        ],
        default='merged'
    )
    date = models.DateField(null=True, blank=True, help_text="Date merged/submitted")
    lines_changed = models.CharField(max_length=50, blank=True, help_text="e.g., +100 -50")
    
    panels = [
        FieldPanel('project_name'),
        FieldPanel('title'),
        FieldPanel('description'),
        FieldPanel('pr_url'),
        FieldPanel('status'),
        FieldPanel('date'),
        FieldPanel('lines_changed'),
    ]
    
    def __str__(self):
        return f"{self.project_name} - {self.title}"


class Publication(Orderable):
    """Publications section"""
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='publications')
    title = RichTextField()
    authors = models.TextField()
    journal = models.CharField(max_length=300, blank=True)
    date = models.DateField(null=True, blank=True)
    doi = models.CharField(max_length=200, blank=True, verbose_name="DOI")
    url = models.URLField(blank=True)
    abstract = RichTextField(blank=True)
    
    panels = [
        FieldPanel('title'),
        FieldPanel('authors'),
        FieldPanel('journal'),
        FieldPanel('date'),
        FieldPanel('doi'),
        FieldPanel('url'),
        FieldPanel('abstract'),
    ]
    
    def __str__(self):
        return self.title


class FormField(AbstractFormField):
    """Contact form fields"""
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='form_fields')

