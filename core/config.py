from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv()

PORT = os.getenv("PORT")
PASSWORD = os.getenv("PASSWORD")
SECRET_KEY = os.getenv("SECRET_KEY")

# AppData folder
APPDATA = Path(os.getenv("APPDATA"))

# App directory
APP_DIR = APPDATA / ".api-vault"
APP_DIR.mkdir(parents=True, exist_ok=True)

# Database file
DB_NAME = APP_DIR / "apple_an_day_keep_the_doctor_away.db"

