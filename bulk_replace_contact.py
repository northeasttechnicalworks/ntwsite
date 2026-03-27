import os

base_dir = "e:/websites/NTW"

replacements = {
    "deploy@ne-technical.com": "solutions@northeasttechworks.com",
    "+1 (800) 555-0199": "(203) 418-1608",
    "+18005550199": "2034181608",
    "18005550199": "2034181608",
    "8005550199": "2034181608"
}

def process_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
    except UnicodeDecodeError:
        return

    original_content = content
    for old, new in replacements.items():
        content = content.replace(old, new)
        
    if content != original_content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {file_path}")

for root, _, files in os.walk(base_dir):
    for file in files:
        if file.endswith((".html", ".js", ".py", ".css")):
            # Don't modify our own script
            if file == "bulk_replace_contact.py":
                continue
            process_file(os.path.join(root, file))

print("Replacement complete.")
