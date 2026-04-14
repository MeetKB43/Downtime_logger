import os
from supabase import create_client, Client
from dotenv import load_dotenv
import json

load_dotenv()
url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")
print(url)
supabase: Client = create_client(url,key)

def record_DT (s_time, e_time, duration):
	s_time = json.dumps(s_time, default=str)
	e_time = json.dumps(e_time, default=str)
	response = (
		supabase.table("downtime")
		.insert({"Start_Time": s_time, "End_Time": e_time, "Duration_Minutes": duration})
		.execute()
	)

