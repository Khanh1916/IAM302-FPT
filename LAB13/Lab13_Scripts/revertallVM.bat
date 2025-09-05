@echo off
setlocal
set Path=C:\Program Files (x86)\VMware\VMware Player
set snapname=
set/p snapname=Enter the name for the snapshot:
for /F "skip=1 delims=," %%i in ('vmrun list') do (
echo Reverting snapshot for %%i
vmrun start "%%i"
vmrun -T ws revertToSnapshot "%%i" %snapname% msg.autoAnswer = TRUE )
endlocal
set/p any=press any key ...