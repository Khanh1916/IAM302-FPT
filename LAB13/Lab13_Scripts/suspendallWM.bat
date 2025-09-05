@echo off
setlocal
set Path=C:\Program Files (x86)\VMware\VMware Player
for /F "skip=1 delims=," %%i in ('vmrun list') do (
echo Suspending for %%i
vmrun -T ws suspend "%%i" )
endlocal
set/p any press any key ....