#!/usr/bin/env python
"""Generate all Wagtail image renditions at deploy time."""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings.production')
django.setup()

from wagtail.images import get_image_model
from wagtail.images.models import Rendition

Image = get_image_model()

# Delete old renditions
Rendition.objects.all().delete()
print('Cleared old renditions')

# Generate all needed renditions
rendition_specs = [
    'fill-250x250',
    'fill-400x200',
    'max-165x165',
]

generated = 0
errors = 0

for img in Image.objects.all():
    print(f'Processing: {img.title} ({img.file.name})')
    for spec in rendition_specs:
        try:
            rendition = img.get_rendition(spec)
            print(f'  ✓ Generated {spec}: {rendition.file.name}')
            generated += 1
        except Exception as e:
            print(f'  ✗ Error generating {spec}: {e}')
            errors += 1

print(f'\n✅ Generated {generated} renditions')
if errors:
    print(f'⚠️  {errors} errors')
