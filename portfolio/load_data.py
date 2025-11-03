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
    from wagtail.models import Page
    
    # Check if only root page exists (id=1) and welcome page (id=2)
    page_count = Page.objects.count()
    
    if page_count <= 2:
        print("=" * 50)
        print("Loading portfolio data from portfolio_data.json...")
        print("=" * 50)
        try:
            call_command('loaddata', 'portfolio_data.json', verbosity=2)
            print("=" * 50)
            print("Portfolio data loaded successfully!")
            print(f"Total pages now: {Page.objects.count()}")
            print("=" * 50)
        except Exception as e:
            print("=" * 50)
            print(f"Error loading data: {e}")
            print("=" * 50)
            import traceback
            traceback.print_exc()
            sys.exit(1)
    else:
        print(f"Pages already exist ({page_count} pages), skipping fixture load.")
        print("To reload data, delete the database and redeploy.")
