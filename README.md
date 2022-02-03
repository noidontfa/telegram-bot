### Development
- Config environment
```
.env.template
```
- Create virtual environment
```python
py -m venv venv
./venv/Scripts/activate
pip install -r requirements.txt
py manage.py migrate
py manage.py seed_languages
```
- Start server and bots
```python
py manage.py runserver
py manage.py run_bots
```
- Install pre-commit
```
pip install pre-commit
pre-commit install
pre-commit run --all-files
```
### Deployment
- Config production environment
```
.env_production.template
```
- Cd to deployment folder and build docker compose
```
docker-compose build
docker-compose up
```
- Utils
```
docker ps -a
docker exec -ti <app_name> sh
```
