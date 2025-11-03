# Deploy to Railway

## Prerequisites
- GitHub account
- Railway account (sign up at https://railway.app)

## Steps to Deploy

### 1. Push Your Code to GitHub
```bash
cd C:\Users\srish\OneDrive\Desktop\Python\Wagtail\site\portfolio
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git push -u origin main
```

### 2. Deploy on Railway

1. Go to https://railway.app
2. Click "Start a New Project"
3. Select "Deploy from GitHub repo"
4. Connect your GitHub account if not already connected
5. Select your repository
6. Railway will auto-detect it's a Django project

### 3. Add PostgreSQL Database

1. In your Railway project dashboard, click "New"
2. Select "Database" → "Add PostgreSQL"
3. Railway will automatically create a `DATABASE_URL` environment variable

### 4. Set Environment Variables

In Railway project settings, add these variables:

```
DJANGO_SETTINGS_MODULE=portfolio.settings.production
SECRET_KEY=your-super-secret-key-here-generate-a-long-random-string
ALLOWED_HOSTS=*.railway.app,*.up.railway.app
PYTHON_VERSION=3.13
```

To generate a SECRET_KEY, run locally:
```python
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 5. Create Superuser (After First Deploy)

1. Go to your Railway project
2. Click on your service
3. Go to "Settings" → "Variables"
4. Run this command in Railway's CLI or using their run feature:

```bash
python manage.py createsuperuser
```

Or use Railway CLI locally:
```bash
railway run python manage.py createsuperuser
```

### 6. Access Your Site

1. Railway will provide a URL like: `https://your-app-name.up.railway.app`
2. Access admin at: `https://your-app-name.up.railway.app/admin`
3. Login with your superuser credentials
4. Create your HomePage and add content

## Important Notes

- **Media Files**: For production, consider using a service like AWS S3 or Cloudinary for media files (profile photos, project images)
- **Database Backups**: Railway automatically backs up PostgreSQL databases
- **Custom Domain**: You can add a custom domain in Railway project settings
- **Environment**: Railway automatically sets `DJANGO_SETTINGS_MODULE=portfolio.settings.production`

## Troubleshooting

### Check Logs
In Railway dashboard → Your Service → "Deployments" → Click latest deployment → "View Logs"

### Common Issues

1. **Static files not loading**: Check if `collectstatic` ran in build logs
2. **Database errors**: Ensure PostgreSQL is added and `DATABASE_URL` is set
3. **500 errors**: Check logs for detailed error messages

### Useful Railway CLI Commands

Install Railway CLI:
```bash
npm i -g @railway/cli
```

Login and link project:
```bash
railway login
railway link
```

Run commands:
```bash
railway run python manage.py migrate
railway run python manage.py createsuperuser
railway run python manage.py collectstatic
```

## What Gets Deployed

✅ Your Wagtail portfolio site
✅ PostgreSQL database
✅ All your custom models (HomePage, Skills, Projects, Contributions, etc.)
✅ Admin interface at `/admin`
✅ Static files (CSS, JS)
✅ Media uploads (if you add media storage)

## Cost

- **Free Tier**: $5 credit/month (enough for small portfolio)
- **Hobby Plan**: $5/month for unlimited usage
- Your portfolio should run fine on the free tier!
