import os

def load_dotenv(dotenv_path=".env"):
        if not os.path.exists(dotenv_path):
            return
        with open(dotenv_path) as f:
            for line in f:
                if line.strip() and not line.startswith("#"):
                    key, value = line.strip().split("=", 1)
                    os.environ[key] = value
