import requests
import json
user_message = "Schedule a meeting tomorrow"

request_message = {
    "message": user_message,
    "chatInput": user_message,  # Add this for AI Agent
    "sessionId": "test-session-123"  # Add this for memory
}

# ✅ CORRECTED URL - webhook-test appears TWICE
url = "http://localhost:5678/webhook-test/43d8c93b-77de-491c-b895-77c1d6f46f38"

try:
    print(f"Sending request to: {url}")
    print(f"Message: {user_message}")
    print("-" * 50)
    
    response = requests.post(url, json=request_message, timeout=30)
    
    print(f"✅ Status Code: {response.status_code}")
    print(f"Response Headers: {response.headers}")
    print(f"Response Body: {response.text}")
    
    if response.status_code == 200:
        try:
            json_response = response.json()
            print(f"\n✅ Parsed JSON Response:")
            print(json.dumps(json_response, indent=2))
        except ValueError as e:
            print(f"⚠️ Could not parse JSON: {e}")
    else:
        print(f"❌ Error: Webhook returned status {response.status_code}")
        
except requests.exceptions.ConnectionError:
    print("❌ Connection Error: Cannot connect to http://localhost:5678")
    print("Make sure n8n is running!")
    print("Try: docker ps | grep n8n")
except requests.exceptions.Timeout:
    print("⏱️ Timeout: The request took too long (>30 seconds)")
    print("The AI Agent might be processing...")
except Exception as e:
    print(f"❌ Error: {type(e).__name__}: {e}")