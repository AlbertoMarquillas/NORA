# run_frontend.ps1

# Navega a la carpeta del frontend
Set-Location "$PSScriptRoot\frontend"

# Lanza el servidor de desarrollo de Vite o React
npm run dev  # <- si usas Vite

# Regresa al directorio original cuando termine
Set-Location $PSScriptRoot
