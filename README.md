# Drone Assessment: Setup Instructions

## For Windows Users

1. **Clone the Repository** :
   - git clone https://github.com/vinscentN/drone_assessment.git
   - Clone the repository using the provided URL.

2. **Navigate to Project Directory**: 
   - Using Command Prompt or PowerShell, navigate to the directory where the repository has been cloned.
   - `cd drone_assessment`

3. **Create and Activate Virtual Environment**:
   - Create a virtual environment by running `python -m venv venv_name` in the project directory.
   - Activate the virtual environment by navigating to the venv directory and running `Scripts\activate`.

4. **Install Dependencies**: 
   - Install the project dependencies by running `pip install -r requirements.txt`. Ensure Python and pip are already installed on your system.

5. **Run Migrations**:
   - Apply database migrations by executing `python manage.py makemigrations`.
   - Execute `python manage.py migrate`.

6. **Load Initial Data** (optional):
   - Load initial data (Sample Medications) into the database using `python manage.py loaddata medication`.

7. **Start the Server**:
   - Start the development server with `python manage.py runserver`.

8. **Start Celery Beat Scheduler and Worker with Redis**:
   - Install Redis if not already installed and ensure it's running.
   - On a new terminal window navigate to where Redis is on your local machine and run `redis-server`
   - Open a new terminal window.
   - Navigate to your project directory.
   - Start Celery beat scheduler with `celery -A drone_assessment_project beat -l info`.
   - Open another terminal window.
   - Navigate to your project directory.
   - Start Celery worker with `celery -A drone_assessment_project worker -l info`.


## API Endpoints

- `POST api/v1/drones/register`: Register a new drone.
- `POST api/v1/add/medication`: Add medications.
- `POST api/v1/drones/load/:drone_id`: Load medications onto a drone.
- `GET api/v1/drones/loaded/:drone_id`: Check loaded medications for a given drone.
- `GET api/v1/drones/available`: Get available drones for loading.
- `GET api/v1/drones/battery/:drone_id`: Check battery level for a given drone.

## Sample Payload

### Register a New Drone 
`Method: POST`
` http://localhost:8000/api/v1/drones/register`
```json
{
  "serial_number": "DRN1234",
  "model": "Lightweight",
  "weight_limit": 500,
  "battery_capacity": 90,
  "state": "IDLE"
}
```

### Add Medication
`Method:POST`
` http://localhost:8000/api/v1/add/medication`
````json
{
  "name": "Medication AZF",
  "weight": 100,
  "code": "MED001",
  "image": "medication_a.jpg"
}
````

### Load Medications onto a Drone
`Method: POST`
`http://localhost:8000/api/v1/drones/load`
````json
{
   "serial_number": "DRN1234",
   "medications": [1,2,3,4]
}
````

### Checking loaded medication items for a given drone
`Method: GET`
````http://localhost:8000/api/v1/drones/loaded/DRN1234````

### Checking available drones for loading
`Method: GET`
````http://localhost:8000/api/v1/drones/available````


### Check drone battery level for a given drone
`Method: GET`
````http://localhost:8000/api/v1/drones/battery/DRN1234````

