# run_fsm.ps1

# Establece el PYTHONPATH para que Python encuentre el paquete backend/fsm_control
$env:PYTHONPATH = "$PSScriptRoot\backend"

# Nombre del módulo a ejecutar
$module = "fsm_control.fsm_tests.fsm_manual_test"

Write-Host "Ejecutando módulo FSM: $module`n"

# Ejecuta el módulo como parte del paquete
python -m $module
