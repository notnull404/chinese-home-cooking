"""
Upload all 16 recipe images from CloudBase to Cloudinary
"""
import cloudinary
import cloudinary.uploader
import requests, json

cloudinary.config(
    cloud_name="dgivtfys2",
    api_key="768753898853767",
    api_secret="z_wVmpuvHjmt6IheecWp30nqHfI"
)

CDN = "https://636c-cloudbase-d9gyi8wgo2d578c78-1312126225.tcb.qcloud.la"

# Map: Chinese name → English slug used in Hugo
recipes = [
    ("红烧肉", "hong-shao-rou-red-braised-pork-belly"),
    ("鱼香肉丝", "yu-xiang-shredded-pork-fish-fragrant-pork"),
    ("青椒肉丝", "shredded-pork-with-green-peppers"),
    ("番茄炒蛋", "tomato-egg-stir-fry"),
    ("麻婆豆腐", "mapo-tofu"),
    ("家常豆腐", "home-style-tofu"),
    ("糖醋排骨", "sweet-and-sour-ribs"),
    ("可乐鸡翅", "cola-chicken-wings"),
    ("皮蛋瘦肉粥", "century-egg--pork-congee"),
    ("宫保鸡丁", "kung-pao-chicken"),
    ("蒜蓉粉丝蒸虾", "garlic-shrimp-with-glass-noodles"),
    ("蛋炒饭", "egg-fried-rice"),
    ("紫菜蛋花汤", "seaweed-egg-drop-soup"),
    ("蒜蓉西兰花", "garlic-broccoli"),
    ("酸辣土豆丝", "hot-and-sour-shredded-potatoes"),
    ("玉米排骨汤（电饭煲）", "corn-and-pork-rib-soup-rice-cooker"),
]

results = []
for ch_name, slug in recipes:
    url = f"{CDN}/foods/{ch_name}.png"
    print(f"Uploading {ch_name}...", end=" ")
    try:
        r = cloudinary.uploader.upload(url, public_id=f"recipes/{slug}")
        img_url = r["secure_url"]
        results.append({"slug": slug, "chinese": ch_name, "cloudinary_url": img_url})
        print(f"✅ {img_url}")
    except Exception as e:
        print(f"❌ {e}")

print(f"\n{'='*60}")
print(f"Uploaded {len(results)}/{len(recipes)} recipes")
print(json.dumps(results, indent=2))
