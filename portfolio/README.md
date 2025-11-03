# Modern Portfolio Website with Wagtail

A clean, minimal, dark-themed portfolio website built with Django and Wagtail CMS.

## Features

- **Hero Section**: Name, photo, professional title
- **About**: Rich text introduction
- **Experience**: Work history with achievements and technologies
- **Projects**: Showcase projects with images, descriptions, and links
- **Skills**: List your skills with icons
- **Education**: Academic background
- **Publications**: Research papers and articles
- **Contact Form**: Built-in contact form with email notifications

## Setup Instructions

### 1. Make sure your virtual environment is activated
```powershell
.\.Sam\Scripts\Activate.ps1
```

### 2. Run migrations
```powershell
cd C:\Users\srish\OneDrive\Desktop\Python\Wagtail\site\portfolio
python manage.py makemigrations
python manage.py migrate
```

### 3. Create a superuser
```powershell
python manage.py createsuperuser
```
Follow the prompts to create your admin account.

### 4. Run the development server
```powershell
python manage.py runserver
```

### 5. Access the admin panel
Open your browser and go to: `http://127.0.0.1:8000/admin`

Login with the superuser credentials you just created.

### 6. Set up your HomePage
1. In the admin panel, go to **Pages**
2. Delete the existing "Welcome to your new Wagtail site!" page
3. Click **Add child page** under **Root**
4. Select **Home Page**
5. Fill in your personal information:
   - First Name
   - Last Name
   - Professional Title
   - Profile Photo (upload an image)
   - About section
6. Add your content sections:
   - **Skills**: Add skills with names and icon emojis (e.g., 🐍, ⚛️, 🔧)
   - **Experience**: Add your work history
     - For each experience, you can add technologies used
   - **Projects**: Add your projects with images
   - **Education**: Add your academic background
   - **Publications**: Add any research papers or articles
7. Set up the contact form:
   - Add form fields (Name, Email, Message, etc.)
   - Configure email settings
8. Click **Publish**

### 7. Create Technology Tags (for Projects & Experience)
1. In the admin sidebar, go to **Snippets** → **Technologies**
2. Add technologies (e.g., Python, Django, React, etc.)
3. Assign colors to each technology (they'll appear as colored tags)

### 8. View your portfolio
Go to: `http://127.0.0.1:8000/`

## Customization

### Changing Colors
Edit the `home_page.html` template and modify the CSS variables:
- Main accent color: `#4A90E2` (blue)
- Background: `#2b2b2b` (dark gray)
- Cards: `#1f1f1f` (darker gray)
- Text: `#e0e0e0` (light gray)

### Adding More Sections
Edit `home/models.py` to add new models and fields, then create migrations.

## Project Structure

```
portfolio/
├── home/
│   ├── models.py           # Database models
│   ├── templates/
│   │   └── home/
│   │       └── home_page.html  # Main template
│   └── migrations/
├── portfolio/
│   ├── settings/           # Django settings
│   └── urls.py            # URL configuration
└── manage.py
```

## Tech Stack

- **Django 5.2**: Web framework
- **Wagtail 7.1**: CMS
- **SQLite**: Database (default)
- **Pure CSS**: No frontend frameworks - keeping it simple!

## Deployment

To deploy to production:
1. Update `portfolio/settings/production.py` with your production settings
2. Set environment variables for `SECRET_KEY`, `DATABASE_URL`, etc.
3. Configure your web server (Gunicorn, etc.)
4. Use the included `Dockerfile` for containerized deployment

## Tips

- Use high-quality images for your profile photo and projects
- Keep descriptions concise and impactful
- Use emojis for icons (they work great and require no icon fonts!)
- The site is fully responsive and mobile-friendly
- All content is managed through the Wagtail admin - no code changes needed

## Support

For Wagtail documentation: https://docs.wagtail.org/

Enjoy your new portfolio! 🚀
