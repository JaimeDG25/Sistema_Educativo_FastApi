from supabase import create_client, Client

url: str ="https://wjfrsojqoyrtcctvtvln.supabase.co"
api: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6IndqZnJzb2pxb3lydGNjdHZ0dmxuIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODMyNTQwMTYsImV4cCI6MjA5ODgzMDAxNn0.M3ySySr7vaRAAE9NRNB6vHXveSWuUujQAHztuOr74ps"

supebase: Client = create_client(url,api)
print("Empezando ")
try: 
    nuevo = {
        "nombre_persona": "Carlos",
        "dni": 87654321
    }
    test = supebase.table("persona").select("*").execute()
    print("Conexion exitosa: ", test.data)
except Exception as e:
    print("Conecion erronea: ", e)
