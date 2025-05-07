# start_servers.ps1 - Minimal version

# Start Backend Server in a new window
# Run from project root, specify app as backend.main:app
Start-Process pwsh -ArgumentList '-NoExit', '-Command', 'Write-Host "Attempting to activate backend venv and start uvicorn (from project root)..."; .\.venv\Scripts\Activate.ps1; python -m uvicorn backend.main:app --reload; Write-Host "Uvicorn process ended or failed to start. Press Enter to close."; Read-Host'

# Start Frontend Server in a new window
Start-Process pwsh -ArgumentList '-NoExit', '-Command', 'Push-Location ./frontend; Write-Host "Attempting to start frontend npm dev server..."; npm run dev -- --open; Write-Host "NPM dev process ended or failed to start. Press Enter to close."; Read-Host'

Write-Host "Commands to start backend and frontend servers have been issued in new windows." 