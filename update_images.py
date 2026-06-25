import os, re

recipes_dir = r"C:\Users\kirito\Desktop\每日菜单\chineserecipes\content\recipes"

cloudinary_map = {
    "红烧肉": "https://res.cloudinary.com/dgivtfys2/image/upload/f_auto,q_auto/v1782207702/recipes/hong-shao-rou-red-braised-pork-belly.jpg",
    "鱼香肉丝": "https://res.cloudinary.com/dgivtfys2/image/upload/f_auto,q_auto/v1782207707/recipes/yu-xiang-shredded-pork-fish-fragrant-pork.jpg",
    "青椒肉丝": "https://res.cloudinary.com/dgivtfys2/image/upload/f_auto,q_auto/v1782207709/recipes/shredded-pork-with-green-peppers.jpg",
    "番茄炒蛋": "https://res.cloudinary.com/dgivtfys2/image/upload/f_auto,q_auto/v1782207712/recipes/tomato-egg-stir-fry.jpg",
    "麻婆豆腐": "https://res.cloudinary.com/dgivtfys2/image/upload/f_auto,q_auto/v1782207715/recipes/mapo-tofu.png",
    "家常豆腐": "https://res.cloudinary.com/dgivtfys2/image/upload/f_auto,q_auto/v1782207720/recipes/home-style-tofu.jpg",
    "糖醋排骨": "https://res.cloudinary.com/dgivtfys2/image/upload/f_auto,q_auto/v1782207724/recipes/sweet-and-sour-ribs.jpg",
    "可乐鸡翅": "https://res.cloudinary.com/dgivtfys2/image/upload/f_auto,q_auto/v1782207725/recipes/cola-chicken-wings.jpg",
    "皮蛋瘦肉粥": "https://res.cloudinary.com/dgivtfys2/image/upload/f_auto,q_auto/v1782207729/recipes/century-egg--pork-congee.jpg",
    "宫保鸡丁": "https://res.cloudinary.com/dgivtfys2/image/upload/f_auto,q_auto/v1782207733/recipes/kung-pao-chicken.jpg",
    "蒜蓉粉丝蒸虾": "https://res.cloudinary.com/dgivtfys2/image/upload/f_auto,q_auto/v1782207737/recipes/garlic-shrimp-with-glass-noodles.jpg",
    "蛋炒饭": "https://res.cloudinary.com/dgivtfys2/image/upload/f_auto,q_auto/v1782207739/recipes/egg-fried-rice.jpg",
    "紫菜蛋花汤": "https://res.cloudinary.com/dgivtfys2/image/upload/f_auto,q_auto/v1782207742/recipes/seaweed-egg-drop-soup.jpg",
    "蒜蓉西兰花": "https://res.cloudinary.com/dgivtfys2/image/upload/f_auto,q_auto/v1782207747/recipes/garlic-broccoli.jpg",
    "酸辣土豆丝": "https://res.cloudinary.com/dgivtfys2/image/upload/f_auto,q_auto/v1782207749/recipes/hot-and-sour-shredded-potatoes.jpg",
    "玉米排骨汤": "https://res.cloudinary.com/dgivtfys2/image/upload/f_auto,q_auto/v1782207754/recipes/corn-and-pork-rib-soup-rice-cooker.jpg",
    "玉米排骨汤（电饭煲）": "https://res.cloudinary.com/dgivtfys2/image/upload/f_auto,q_auto/v1782207754/recipes/corn-and-pork-rib-soup-rice-cooker.jpg",
}

updated = 0
for fname in sorted(os.listdir(recipes_dir)):
    if not fname.endswith(".md"):
        continue
    fpath = os.path.join(recipes_dir, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    m = re.search(r'^image:\s*"?([^"\n]+)"?\s*$', content, re.MULTILINE)
    if not m:
        print(f"  ⚠️  No image field in {fname}")
        continue
    
    old_path = m.group(1)
    ch_match = re.search(r"/([^/]+)\.\w+$", old_path)
    if not ch_match:
        print(f"  ⚠️  Can't parse image path in {fname}: {old_path}")
        continue
    
    ch_name = ch_match.group(1)
    
    if ch_name in cloudinary_map:
        new_url = cloudinary_map[ch_name]
        new_line = f'image: "{new_url}"'
        content = content.replace(m.group(0), new_line)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        updated += 1
        print(f"  ✅ {ch_name}")
    else:
        print(f"  ❌ No match for {ch_name}")

print(f"\nUpdated: {updated}/16")
