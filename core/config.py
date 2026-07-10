from dotenv import load_dotenv
import os


load_dotenv()

PORT = os.getenv("PORT")
PASSWORD = os.getenv("PASSWORD")
SECRET_KEY = os.getenv("SECRET_KEY")

DB_NAME = os.path.join("app_data", "apple_an_day_keep_the_doctor_away.db")