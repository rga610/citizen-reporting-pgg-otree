# Complete server restart script
Write-Host "Stopping any running servers..." -ForegroundColor Yellow
Get-Process | Where-Object {$_.ProcessName -eq "python" -or $_.ProcessName -eq "uvicorn"} | Stop-Process -Force -ErrorAction SilentlyContinue

Write-Host "Clearing Python cache..." -ForegroundColor Yellow
Get-ChildItem -Recurse -Filter "*.pyc" | Remove-Item -Force -ErrorAction SilentlyContinue
Get-ChildItem -Recurse -Filter "__pycache__" | Remove-Item -Recurse -Force -ErrorAction SilentlyContinue

Write-Host "Resetting database..." -ForegroundColor Yellow
.\venv\Scripts\Activate.ps1
otree resetdb --noinput

Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "Server is ready to start!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "IMPORTANT: You must create a NEW session!" -ForegroundColor Red
Write-Host "Old sessions will not show the new changes." -ForegroundColor Red
Write-Host ""
Write-Host "To start the server, run:" -ForegroundColor Yellow
Write-Host "  uvicorn otree.asgi:app --host 127.0.0.1 --port 8000 --reload" -ForegroundColor Cyan
Write-Host ""
Write-Host "Then go to http://localhost:8000 and create a NEW session" -ForegroundColor Yellow
Write-Host "You should see 4 treatment options!" -ForegroundColor Yellow
Write-Host ""

