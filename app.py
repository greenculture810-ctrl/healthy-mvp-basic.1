from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
async def index():
    return FileResponse("index.html")

@app.post("/plan")
async def plan(data: dict):
    budget = data.get("budget")
    calories = data.get("calories")
    region = data.get("region")
    meals = [
        f"Breakfast: Oatmeal with fruit ({region})",
        f"Lunch: Grilled chicken salad ({region})",
        f"Dinner: Rice and beans with veggies ({region})"
    ]
    return {"budget": budget, "calories": calories, "region": region, "meals": meals}
