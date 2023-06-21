@echo off

mkdir employee_burnout_prevention
cd employee_burnout_prevention

echo.>config.py
echo.>wsgi.py
echo.>.env

mkdir app
cd app

echo.>__init__.py

mkdir main
cd main
echo.>__init__.py
echo.>routes.py
echo.>forms.py
echo.>utils.py
cd ..

mkdir auth
cd auth
echo.>__init__.py
echo.>routes.py
echo.>forms.py
cd ..

mkdir models
cd models
echo.>__init__.py
echo.>user.py
echo.>survey.py
cd ..

mkdir static
cd static
mkdir css
mkdir js
cd ..

mkdir templates
cd templates
echo.>index.html
echo.>login.html
echo.>register.html
echo.>dashboard.html
echo.>profile.html
echo.>survey.html
echo.>resources.html
echo.>notifications.html
echo.>help_center.html
echo.>admin.html
echo.>base.html
cd ../..

echo.
echo Project structure created successfully!
pause