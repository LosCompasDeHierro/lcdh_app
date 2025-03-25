import time
import sys
from django.db import connections
from django.db.utils import OperationalError

def wait_for_db():
    """Espera a que PostgreSQL esté disponible"""
    max_retries = 10
    retry_count = 0
    
    while retry_count < max_retries:
        try:
            conn = connections['default']
            conn.cursor()
            print("¡PostgreSQL está disponible!")
            return
        except OperationalError:
            print(f"Esperando PostgreSQL... (Intento {retry_count + 1}/{max_retries})")
            time.sleep(5)
            retry_count += 1
    
    sys.exit(1)

if __name__ == "__main__":
    wait_for_db()