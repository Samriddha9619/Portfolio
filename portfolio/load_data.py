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
    from home.models import HomePage
    
    # Check if HomePage exists
    if HomePage.objects.count() == 0:
        print("=" * 50)
        print("Loading portfolio data from portfolio_data.json...")
        print("=" * 50)
        try:
            call_command('loaddata', 'portfolio_data.json', verbosity=2)
            print("=" * 50)
            print("Portfolio data loaded successfully!")
            print("=" * 50)
        except Exception as e:
            print("=" * 50)
            print(f"Error loading data: {e}")
            print("=" * 50)
            sys.exit(1)
    else:
        print("HomePage already exists, skipping fixture load.")
