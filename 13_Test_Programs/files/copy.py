def copy_file(source_file, destination_file):
    try:
        with open(source_file, "r", encoding="utf-8") as src:
            content = src.read()  # read all content
        
        with open(destination_file, "w", encoding="utf-8") as dest:
            dest.write(content)   # write content to destination
        
        print(f"Contents copied from '{source_file}' to '{destination_file}' successfully!")
    
    except FileNotFoundError:
        print(f"Source file '{source_file}' not found!")

# Example usage
source = "source.txt"       # file to copy from
destination = "destination.txt"  # file to copy to

copy_file(source, destination)
