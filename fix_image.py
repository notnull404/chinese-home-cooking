import requests

key = "eyJhbG...38Yc"

r = requests.patch(
    "https://glpvakbewmdlmohmytiz.supabase.co/rest/v1/recipes?slug=eq.century-egg-&-pork-congee",
    json={"image_url": "https://res.cloudinary.com/dgivtfys2/image/upload/f_auto,q_auto/v1782207729/recipes/century-egg--pork-congee.jpg"},
    headers={"apikey": key, "Authorization": f"Bearer {key}", "Content-Type": "application/json"}
)
print(f"Status: {r.status_code}")
if r.status_code in [200, 204]:
    print("✅ Fixed!")
else:
    print(r.text[:200])
