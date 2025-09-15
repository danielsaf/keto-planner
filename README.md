# keto-planner
Keto planner for create medical meal.


run:
  - source .venv/bin/activate
  - pip install -r requirements.txt
  - uvicorn app.main:app --reloa

# run db
     - docker-compose -f deployments/maria-db-docker-compose.yml up -d