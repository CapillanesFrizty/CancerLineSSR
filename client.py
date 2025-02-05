import psycopg2

_SUPABASE_PASSWORD="Zv4RpGQhERuqnVgf"
_SUPABASE_URL=f"postgresql://postgres.rjqurvqazyrxpiqjshxm:{_SUPABASE_PASSWORD}@aws-0-ap-southeast-1.pooler.supabase.com:6543/postgres"

try:
    conn = psycopg2.connect(_SUPABASE_URL)
    cursor = conn.cursor()
    print("Connected to PostgreSQL via Supabase")
except Exception as e:
        print("Database error:", e)




