import requests

# Backend API URL
BACKEND_URL = "http://localhost:8000/recommend"

# Function to send user input to backend and get outfit recommendation
def get_outfit_recommendation(user_input):
    try:
        response = requests.post(BACKEND_URL, json={"user_input": user_input})
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Backend Error: {response.status_code}"}
    except Exception as e:
        return {"error": str(e)}

# Example usage
if __name__ == "__main__":
    user_input = "casual summer outfit"
    result = get_outfit_recommendation(user_input)
    print(result)



