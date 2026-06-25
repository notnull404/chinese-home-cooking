import os, re, json, requests

recipes_dir = r"C:\Users\kirito\Desktop\每日菜单\chineserecipes\content\recipes"

def parse_recipe(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    parts = content.split('---', 2)
    if len(parts) < 3:
        return None
    
    fm_text = parts[1]
    body = parts[2].strip()
    
    # Parse frontmatter manually
    fm = {}
    for line in fm_text.strip().split('\n'):
        m = re.match(r'^(\w+):\s*(.+)$', line)
        if m:
            key = m.group(1).strip()
            val = m.group(2).strip().strip('"').strip("'")
            fm[key] = val
    
    # Parse body sections
    sections = re.split(r'^##\s+', body, flags=re.MULTILINE)
    
    description = ""
    ingredients = []
    seasonings = []
    steps = []
    tips = ""
    
    for sec in sections:
        sec = sec.strip()
        if not sec:
            continue
        lines = sec.split('\n')
        heading = lines[0].strip()
        rest = '\n'.join(lines[1:]).strip() if len(lines) > 1 else ""
        
        if heading == "Ingredients":
            for line in rest.split('\n'):
                if '|' in line and line.strip().startswith('|'):
                    cells = [c.strip() for c in line.split('|') if c.strip()]
                    if cells and not cells[0].startswith('Ingredient') and not cells[0].startswith('---'):
                        name = cells[0] if len(cells) > 0 else ""
                        amount = cells[1] if len(cells) > 1 else ""
                        if name:
                            ingredients.append({"name": name, "amount": amount})
        
        elif heading == "Seasonings":
            for line in rest.split('\n'):
                line = line.strip()
                if line.startswith('- '):
                    s = line[2:].strip()
                    if s and not s.startswith('-'):
                        seasonings.append({"name": s})
        
        elif heading == "Instructions":
            for line in rest.split('\n'):
                line = line.strip()
                m = re.match(r'^\d+\.\s*(.*)', line)
                if m:
                    text = m.group(1).strip()
                    if text:
                        steps.append({"step": len(steps)+1, "text": text})
        
        elif heading == "Tips":
            tips = rest.strip()
            tips = re.sub(r'</?[^>]+>', '', tips)
        else:
            if not description and not heading.startswith('#'):
                desc_lines = [l for l in sec.split('\n') if l.strip() and not l.strip().startswith('|-') and not l.strip().startswith('|')]
                description = ' '.join(desc_lines)
    
    cats = fm.get('categories', '')
    if cats.startswith('['):
        cats = cats.strip('[]').strip('"').strip("'")
    
    title = fm.get('title', '')
    
    recipe = {
        "title": title,
        "slug": fm.get('slug', title.lower().replace(' ', '-')),
        "category": cats,
        "difficulty": fm.get('difficulty', ''),
        "cook_time": fm.get('cooktime', fm.get('cookTime', '')),
        "servings": fm.get('servings', ''),
        "description": description,
        "ingredients": json.dumps(ingredients),
        "seasonings": json.dumps(seasonings),
        "steps": json.dumps(steps),
        "tips": tips,
    }
    return recipe

# Parse all recipes
parsed = []
for fname in sorted(os.listdir(recipes_dir)):
    if fname.endswith('.md'):
        fp = os.path.join(recipes_dir, fname)
        recipe = parse_recipe(fp)
        if recipe:
            parsed.append(recipe)
            print(f"  {recipe['title']}")

print(f"\nTotal: {len(parsed)}")

# Insert into Supabase
api_url = "https://glpvakbewmdlmohmytiz.supabase.co/rest/v1/recipes"
api_headers = {
    "apikey": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImdscHZha2Jld21kbG1vaG15dGl6Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc4MjE4NzkzNSwiZXhwIjoyMDk3NzYzOTM1fQ.q2W4QGU7WuxGtiA9s1FVDt7f9eJOCipQKCyhGRs38Yc",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImdscHZha2Jld21kbG1vaG15dGl6Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc4MjE4NzkzNSwiZXhwIjoyMDk3NzYzOTM1fQ.q2W4QGU7WuxGtiA9s1FVDt7f9eJOCipQKCyhGRs38Yc",
    "Content-Type": "application/json",
    "Prefer": "return=minimal"
}

success = 0
for rcp in parsed:
    r = requests.post(api_url, json=rcp, headers=api_headers)
    if r.status_code in [201, 200]:
        success += 1
        print(f"  ✅ {rcp['title']}")
    else:
        print(f"  ❌ {rcp['title']}: {r.status_code} {r.text[:100]}")

print(f"\nImported: {success}/{len(parsed)}")
