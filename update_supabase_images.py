import requests, json

key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImdscHZha2Jld21kbG1vaG15dGl6Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc4MjE4NzkzNSwiZXhwIjoyMDk3NzYzOTM1fQ.q2W4QGU7WuxGtiA9s1FVDt7f9eJOCipQKCyhGRs38Yc"

supabase_url = "https://glpvakbewmdlmohmytiz.supabase.co"
headers = {
    "apikey": key,
    "Authorization": f"Bearer {key}",
    "Content-Type": "application/json",
    "Prefer": "return=minimal"
}

image_urls = {
    "hong-shao-rou-red-braised-pork-belly": "https://res.cloudinary.com/dgivtfys2/image/upload/v1782207702/recipes/hong-shao-rou-red-braised-pork-belly.jpg",
    "yu-xiang-shredded-pork-fish-fragrant-pork": "https://res.cloudinary.com/dgivtfys2/image/upload/v1782207707/recipes/yu-xiang-shredded-pork-fish-fragrant-pork.jpg",
    "shredded-pork-with-green-peppers": "https://res.cloudinary.com/dgivtfys2/image/upload/v1782207709/recipes/shredded-pork-with-green-peppers.jpg",
    "tomato-egg-stir-fry": "https://res.cloudinary.com/dgivtfys2/image/upload/v1782207712/recipes/tomato-egg-stir-fry.jpg",
    "mapo-tofu": "https://res.cloudinary.com/dgivtfys2/image/upload/v1782207715/recipes/mapo-tofu.png",
    "home-style-tofu": "https://res.cloudinary.com/dgivtfys2/image/upload/v1782207720/recipes/home-style-tofu.jpg",
    "sweet-and-sour-ribs": "https://res.cloudinary.com/dgivtfys2/image/upload/v1782207724/recipes/sweet-and-sour-ribs.jpg",
    "cola-chicken-wings": "https://res.cloudinary.com/dgivtfys2/image/upload/v1782207725/recipes/cola-chicken-wings.jpg",
    "century-egg--pork-congee": "https://res.cloudinary.com/dgivtfys2/image/upload/v1782207729/recipes/century-egg--pork-congee.jpg",
    "kung-pao-chicken": "https://res.cloudinary.com/dgivtfys2/image/upload/v1782207733/recipes/kung-pao-chicken.jpg",
    "garlic-shrimp-with-glass-noodles": "https://res.cloudinary.com/dgivtfys2/image/upload/v1782207737/recipes/garlic-shrimp-with-glass-noodles.jpg",
    "egg-fried-rice": "https://res.cloudinary.com/dgivtfys2/image/upload/v1782207739/recipes/egg-fried-rice.jpg",
    "seaweed-egg-drop-soup": "https://res.cloudinary.com/dgivtfys2/image/upload/v1782207742/recipes/seaweed-egg-drop-soup.jpg",
    "garlic-broccoli": "https://res.cloudinary.com/dgivtfys2/image/upload/v1782207747/recipes/garlic-broccoli.jpg",
    "hot-and-sour-shredded-potatoes": "https://res.cloudinary.com/dgivtfys2/image/upload/v1782207749/recipes/hot-and-sour-shredded-potatoes.jpg",
    "corn-and-pork-rib-soup-rice-cooker": "https://res.cloudinary.com/dgivtfys2/image/upload/v1782207754/recipes/corn-and-pork-rib-soup-rice-cooker.jpg",
}

for slug, img_url in image_urls.items():
    r = requests.patch(
        f"{supabase_url}/rest/v1/recipes?slug=eq.{slug}",
        json={"image_url": img_url},
        headers=headers
    )
    status = "✅" if r.status_code in [200, 204] else f"❌ ({r.status_code})"
    print(f"  {status} {slug}")

print("\nDone!")
