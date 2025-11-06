# IMPORTANT: Restart Instructions

The changes have been made, but you need to:

## Step 1: Stop the old server
If you have a server running, stop it (Ctrl+C in the terminal where it's running)

## Step 2: Clear cache and restart
Run these commands in PowerShell from the `public_goods_project` directory:

```powershell
cd "C:\Users\rga61\Documents\Coding projects\wu\public_goods_project"
.\venv\Scripts\Activate.ps1

# Clear Python cache
Get-ChildItem -Recurse -Filter "*.pyc" | Remove-Item -Force
Get-ChildItem -Recurse -Filter "__pycache__" | Remove-Item -Recurse -Force

# Reset database (this clears old sessions)
otree resetdb --noinput

# Start server
uvicorn otree.asgi:app --host 127.0.0.1 --port 8000 --reload
```

## Step 3: Create a NEW session
After the server starts:
1. Go to http://localhost:8000
2. Click on "Demo" in the navigation
3. You should now see **4 different treatment options**:
   - Citizen Reporting PGG - Treatment 1
   - Citizen Reporting PGG - Treatment 2
   - Citizen Reporting PGG - Treatment 3
   - Citizen Reporting PGG - Treatment 4
4. Click on one of these to create a NEW session
5. The old sessions won't work - you need to create new ones

## What Changed:
- ✅ 4 treatment groups (instead of 1)
- ✅ 4 players per group (instead of 3)
- ✅ 10 rounds (instead of 1)
- ✅ Citizen reporting framing
- ✅ New introduction page

## If you still see old content:
- Make sure you're accessing http://localhost:8000 (not a cached page)
- Hard refresh your browser (Ctrl+F5)
- Create a completely NEW session (don't use old session links)
- Check that you're in the `public_goods_project` directory, not `public_goods`

