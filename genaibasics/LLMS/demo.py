from google import genai
from dotenv import load_dotenv
import os   # ✅ missing import

load_dotenv()
api_key = os.getenv("API_KEY")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-2.5-flash",   # safer model (avoid deprecated issues)
    contents="Explain data engineering in simple terms"
)

print(response.text)