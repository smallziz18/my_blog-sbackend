# wait_db.py
import sys, time, psycopg
import os

MAX_WAIT_TIME_SECONDS = 30
RETRY_INTERVAL = 5
start_time = time.time()

def check_database():
    try:
        conn = psycopg.connect(
            dbname=os.environ["POSTGRES_DB"],
            user=os.environ["POSTGRES_USER"],
            password=os.environ["POSTGRES_PASSWORD"],
            host=os.environ["POSTGRES_HOST"],
            port=os.environ["POSTGRES_PORT"],
        )
        conn.close()
        return True
    except psycopg.OperationalError as e:
        elapsed = int(time.time() - start_time)
        sys.stderr.write(f"Database connection failed after {elapsed}s: {e}\n")
        return False

while True:
    if check_database():
        break
    if time.time() - start_time > MAX_WAIT_TIME_SECONDS:
        sys.stderr.write("Error: Database connection could not be established after 30 seconds\n")
        sys.exit(1)
    sys.stderr.write(f"Waiting {RETRY_INTERVAL}s before retrying...\n")
    time.sleep(RETRY_INTERVAL)

print("PostgreSQL is ready to accept connections")
