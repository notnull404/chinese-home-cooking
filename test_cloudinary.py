"""
Cloudinary Onboarding Test
Uploads a demo image, fetches metadata, generates optimized URL.
"""
import cloudinary
import cloudinary.uploader
import cloudinary.api

# ── Credentials (inline) ──
cloudinary.config(
    cloud_name="dgivtfys2",
    api_key="768753898853767",
    api_secret="z_wVmpuvHjmt6IheecWp30nqHfI"
)

# ── 1. Upload a sample image ──
print("Uploading sample image...")
result = cloudinary.uploader.upload(
    "https://res.cloudinary.com/demo/image/upload/sample.jpg",
    public_id="hermes_test_sample"
)
secure_url = result["secure_url"]
public_id = result["public_id"]
print(f"✅ Uploaded!")
print(f"   Public ID: {public_id}")
print(f"   Secure URL: {secure_url}")

# ── 2. Get image details ──
print("\nFetching image details...")
info = cloudinary.api.resource(public_id)
width = info["width"]
height = info["height"]
fmt = info["format"]
bytes_size = info["bytes"]
print(f"   Width: {width}px")
print(f"   Height: {height}px")
print(f"   Format: {fmt}")
print(f"   Size: {bytes_size} bytes ({bytes_size/1024:.1f} KB)")

# ── 3. Generate transformed URL ──
# f_auto  → let Cloudinary choose the best format (WebP, AVIF, etc.)
# q_auto  → let Cloudinary choose optimal quality (balances size & visual quality)
transformed_url = cloudinary.CloudinaryImage(public_id).build_url(
    transformation=[{"fetch_format": "auto", "quality": "auto"}]
)
print(f"\n🎯 Done! Click the link below to see the optimized version.")
print(f"   Check the size and format difference vs the original.")
print(f"\n   Transformed URL: {transformed_url}")
