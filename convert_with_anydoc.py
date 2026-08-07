import os
import glob
import anydoc

source_dir = "/media/romi/data/carpeta nueva donde van a estar los proyectos "
dest_dir = "/media/romi/data/portfolio_qa"

def sanitize_filename(name):
    name = name.replace("Copia de ", "")
    name = name.replace("Copia-", "")
    name = name.replace(" ", "_")
    name = name.replace(".xlsx", "")
    name = name.replace(".docx", "")
    return name

def convert_file(filepath):
    try:
        filename = os.path.basename(filepath)
        clean_name = sanitize_filename(filename)
        dest_path = os.path.join(dest_dir, f"{clean_name}.md")
        
        md_content = anydoc.to_markdown(filepath)
        
        with open(dest_path, "w", encoding="utf-8") as f:
            f.write(f"# {filename}\n\n")
            f.write(md_content)
            
        print(f"✅ Converted with anydoc: {filename} -> {clean_name}.md")
    except Exception as e:
        print(f"❌ Error converting {filepath}: {e}")

def main():
    print("🚀 Starting conversion using firecrawl-anydoc...")
    
    excel_files = glob.glob(os.path.join(source_dir, "**", "*.xlsx"), recursive=True)
    word_files = glob.glob(os.path.join(source_dir, "**", "*.docx"), recursive=True)
    
    all_files = excel_files + word_files
    print(f"Found {len(all_files)} files to convert.")
    
    for f in all_files:
        convert_file(f)
        
    print("✨ Conversion finished!")

if __name__ == "__main__":
    main()
