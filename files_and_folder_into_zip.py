import os
import zipfile

def collect_and_zip_files(root_dir, zip_file_name):
    # Create a ZipFile object in write mode
    with zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Walk through the directory structure
        for dirpath, dirnames, filenames in os.walk(root_dir):
            for filename in filenames:
                # Check for specified file types
                if (filename.endswith('.py') or 
                    filename.endswith('.ipynb') or 
                    filename.endswith('.txt') or 
                    filename.endswith('.html') or 
                    filename.endswith('.js') or 
                    filename.endswith('.css') or 
                    filename.endswith('.md') or 
                    filename == '.gitignore' or 
                    filename.endswith('.json') or 
                    filename.endswith('.pdf')):
                    
                    # Create a relative path for the file to maintain folder structure
                    file_path = os.path.join(dirpath, filename)
                    # Write the file to the zip file with the relative path
                    zipf.write(file_path, os.path.relpath(file_path, root_dir))

# Example usage
root_directory = '/home/uttam/App'  # Change this to the root directory you want to scan
zip_file_name = 'App.zip'       # The name of the output ZIP file

collect_and_zip_files(root_directory, zip_file_name)

print(f"ZIP file created: {zip_file_name}")
