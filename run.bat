@echo off

rem Set the path to your Python executable
set PYTHON_EXECUTABLE=path\to\python\executable

rem Set the path to your Python script
set SCRIPT_PATH=C:\path\to\your\dashboard\directory\dashboard_panel.py

rem Activate the virtual environment (if applicable)
call %PYTHON_EXECUTABLE% -m venv path\to\venv
call path\to\venv\Scripts\activate

rem Install necessary packages (ensure pip is up-to-date)
call %PYTHON_EXECUTABLE% -m pip install --upgrade pip
call %PYTHON_EXECUTABLE% -m pip install panel pandas hvplot

rem Run the dashboard script using panel serve
call %PYTHON_EXECUTABLE% -m panel serve %SCRIPT_PATH%

rem Deactivate the virtual environment
call path\to\venv\Scripts\deactivate


rem to create Windows Service:: 
rem sc create PanelDashboard binPath= "C:\path\to\run_dashboard.bat"
rem sc config PanelDashboardService start= auto

rem sc start PanelDashboard
rem sc stop PanelDashboard



