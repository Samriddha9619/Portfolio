#!/usr/bin/env python
"""
Load portfolio data fixture on first deployment
"""
import os
import sys
import django

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio.settings.production")
    django.setup()
    
    from django.core.management import call_command
    from wagtail.models import Site
    
    # Check if data already exists
    if Site.objects.count() == 0:
        print("Loading portfolio data...")
        call_command('loaddata', 'portfolio_data.json')
        print("Portfolio data loaded successfully!")
    else:
        print("Data already exists, skipping fixture load.")
