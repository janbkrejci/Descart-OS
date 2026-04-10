#!/usr/bin/env -S uv run --script
#
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///

import os

folders = [
    "agent",
    "user",
    "memory",
    "knowledge",
    "workspace"
]

headings = {
    "memory": "## My memories",
    "knowledge": "## My knowledge base"
}

def get_frontmatter(file_path):
    frontmatter_lines = []
    in_frontmatter = False
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip() == "---":
                    if not in_frontmatter:
                        in_frontmatter = True
                        frontmatter_lines.append("\n")
                    else:
                        # frontmatter_lines.append("")
                        break
                elif in_frontmatter:
                    frontmatter_lines.append("- " + line)
    except Exception:
        pass
    
    if len(frontmatter_lines) > 2:  # Ensure we have at least the opening and closing '---'
        return "".join(frontmatter_lines)
    return ""

def process_subdirectories(base_folder, filename="README.md"):
    results = []
    for root, dirs, files in os.walk(base_folder):
        if root == base_folder:
            continue
        
        if filename in files:
            readme_path = os.path.join(root, filename)
            fm = get_frontmatter(readme_path)
            if fm:
                results.append((readme_path, fm))
                
    results.sort(key=lambda x: x[0])
    return results

def main():
    print("SESSION INITIALIZATION CONTEXT - IMPORTANT\n")

    for folder in folders:
        file_path = os.path.join(folder, "README.md")
        # print(f"## Content of {file_path}")
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                print(f.read().strip())
        else:
            print(f"WARNING: {file_path} not found.")
        
        # print("\n" + "-" * 40 + "\n")
        print()
        
        if folder in headings:
            print(headings[folder])
            print()
            if os.path.exists(folder):
                filename = "SKILL.md" if folder == "skills" else "README.md"
                sub_results = process_subdirectories(folder, filename)
                if not sub_results:
                    print("None.\n")
                else:
                    for path, fm in sub_results:
                        print(f"### {path}")
                        print(fm)
                # print()
            else:
                print(f"WARNING: Folder {folder}/ not found.")
            # print("-" * 40 + "\n")
            # print()

    print("END OF SESSION INITIALIZATION CONTEXT\n")

if __name__ == "__main__":
    main()
