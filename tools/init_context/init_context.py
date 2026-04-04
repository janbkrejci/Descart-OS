import os

files = [
    "agent/README.md",
    "user/README.md",
    "knowledge/README.md",
    "memory/README.md",
    "skills/README.md",
    "tools/README.md",
    "workspace/README.md"
]

folders_with_frontmatter = ["knowledge", "memory", "skills", "tools"]

print("# SESSION INITIALIZATION CONTEXT\n")

for file_path in files:
    print(f"## Content of {file_path}")
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            print(f.read())
    else:
        print(f"WARNING: {file_path} not found.")
    print("-" * 40 + "\n")

for folder in folders_with_frontmatter:
    print(f"## Frontmatters for {folder}/")
    if os.path.exists(folder):
        subdirs = [os.path.join(folder, d) for d in os.listdir(folder) if os.path.isdir(os.path.join(folder, d))]
        for subdir in sorted(subdirs):
            readme_path = os.path.join(subdir, "README.md")
            if os.path.exists(readme_path):
                with open(readme_path, "r", encoding="utf-8") as f:
                    lines = f.readlines()
                
                in_frontmatter = False
                frontmatter_lines = []
                for line in lines:
                    if line.strip() == "---":
                        if not in_frontmatter:
                            in_frontmatter = True
                            frontmatter_lines.append(line)
                        else:
                            frontmatter_lines.append(line)
                            break
                    elif in_frontmatter:
                        frontmatter_lines.append(line)
                
                if frontmatter_lines:
                    print(f"### {readme_path}")
                    print("".join(frontmatter_lines))
    else:
        print(f"WARNING: Folder {folder}/ not found.")
    print("-" * 40 + "\n")
