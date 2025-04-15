import json
import os
import requests

# Initialize APIs (set these as environment variables in Lambda)
DEEPSEEK_API_KEY = os.environ.get('DEEPSEEK_API_KEY')
GOOGLE_MAPS_API_KEY = os.environ.get('GOOGLE_MAPS_API_KEY')

def get_ai_response(event):
    name = json.loads(event['body'])['name'].strip().capitalize()[:100]
    body = json.loads(event.get('body', '{}'))
    user_lat = body.get('lat', 55.915)  # Default to Bearsden
    user_lng = body.get('lng', -4.335)
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "deepseek-chat",  # Required field
        "messages": [
            {
                "role": "user",
                "content": f"""
Find ONE real, existing location matching or resembling the name "{name}". Follow these rules STRICTLY:

1. SEARCH ORDER:
- First: Town near area ({user_lat}, {user_lng})
- Then: The area/province nearby
- Then: The country of the coordinates
- Finally: Worldwide

2. REQUIREMENTS:
- Must be a verified real place (check maps)
- Prioritize closest name matches
- Include exact coordinates (verify on Google Maps)

3. RESPONSE FORMAT (JSON ONLY):
{{
"location": "[Full official name]",
"distance": "[X km/miles from nearest town]",
"description": "[1-2 sentence quirky description]",
"funFact": "[Verified historical/geographical fact]",
"coordinates": "[latitude,longitude]"
}}

4. VERIFICATION:
- Double-check all facts exist
- Confirm coordinates on maps
- Never invent information
"""
            }
        ],
        "temperature": 0.7
    }
    print("Sending to deepseek", payload)
    response = requests.post("https://api.deepseek.com/chat/completions", headers=headers, json=payload)
    response.raise_for_status()  # Raises exception for 4XX/5XX responses
    print("AI Response", response.text)
    # Extract the AI's text response
    ai_response = response.json()['choices'][0]['message']['content']
    
    # Parse the JSON from the AI's text response
    print("AI Response 2", ai_response)
    if ai_response.startswith('```json') and ai_response.endswith('```'):
        ai_response = ai_response[7:-3].strip() 
    return json.loads(ai_response)

def get_coordinates(location_name):
    """Fetch coordinates via Google Maps Geocoding API"""
    response = requests.get(
        f"https://maps.googleapis.com/maps/api/geocode/json?address={location_name}&key={GOOGLE_MAPS_API_KEY}"
    )
    data = response.json()
    if data['results']:
        lat = data['results'][0]['geometry']['location']['lat']
        lng = data['results'][0]['geometry']['location']['lng']
        return f'[{lat},{lng}]'
    return None

def lambda_handler(event, context):
    print("Received event", event)
    print("Received event body", event['body'])
    name = json.loads(event['body'])['name'].strip().capitalize()
    

    # Get AI-generated response
    ai_data = get_ai_response(event)
    
    # Fallback if coordinates missing
    if not ai_data.get("coordinates"):
        ai_data["coordinates"] = get_coordinates(ai_data["location"]) or '[55.9,-4.3]' # Default: Bearsden
    print('returning', json.dumps(ai_data))
    return {
        'statusCode': 200,
        'body': json.dumps(ai_data)
    }
