@echo off
SET OSGEO4W_ROOT=C:\Program Files\QGIS 3.10
call "%OSGEO4W_ROOT%"\bin\o4w_env.bat

@echo off
SET QGISNAME=qgis-ltr
path %PATH%;%OSGEO4W_ROOT%\apps\%QGISNAME%\bin
path %PATH%;%OSGEO4W_ROOT%\apps\Qt5\bin
path %PATH%;%OSGEO4W_ROOT%\apps\Python37\Scripts

SET PYTHONPATH=%PYTHONPATH%;%OSGEO4W_ROOT%\apps\%QGISNAME%\python
SET PYTHONHOME=%OSGEO4W_ROOT%\apps\Python37

cmd.exe