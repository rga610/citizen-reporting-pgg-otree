# PowerShell script to start the Otree development server
Set-Location $PSScriptRoot
.\venv\Scripts\Activate.ps1
Write-Host "Starting Otree development server..." -ForegroundColor Green
Write-Host "Server will be available at http://localhost:8000" -ForegroundColor Yellow
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Yellow
Write-Host ""
# Using uvicorn directly as it's more reliable than otree devserver
uvicorn otree.asgi:app --host 127.0.0.1 --port 8000 --reload

