#my homework poetry 

#creating new virtual environment 
```bash
python3 -m venv venv
source venv/bin/activate
pip list
deactivate
#using system-site-packages
python3 -m venv --system-site-packages venv_with_system_packages
pip list
deactivate  
#installing packages and freeze
pip install soap requests numpy
pip list
pip freeze > requirements.txt
deactivate

mkdir new_project
cd new_project
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
deactivate