# Railway Deployment Guide

## Setup Steps

1. **Create a PostgreSQL database on Railway:**
   - In your Railway project, add a PostgreSQL service
   - Railway will automatically set the `DATABASE_URL` environment variable

2. **Set Environment Variables:**
   - `OTREE_ADMIN_PASSWORD` - Set a secure password for admin access
   - `SECRET_KEY` - Set a secure secret key (generate a random string)

3. **Deploy:**
   - Railway will automatically detect the `Procfile` and deploy
   - The app will be available at your Railway domain

## First Deployment

After the first successful deployment, you may need to initialize the database:

1. Go to Railway dashboard → Your service → Deployments
2. Click on the latest deployment
3. Open the "Shell" or "Logs" tab
4. Run: `otree resetdb --noinput`

## Important Notes

- The `_static` directory is required and is now included in the repository
- Railway uses PostgreSQL (configured automatically via `DATABASE_URL`)
- Local development still uses SQLite
- Make sure `OTREE_ADMIN_PASSWORD` and `SECRET_KEY` are set in Railway environment variables

