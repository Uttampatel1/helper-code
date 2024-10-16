import subprocess

def convert_to_bytes(size_string):
    multipliers = {'K': 1024, 'M': 1024**2, 'G': 1024**3}
    size, unit = size_string[:-1], size_string[-1]
    return int(float(size) * multipliers.get(unit, 1))

def sort_disk_usage(base_path):
    # Get disk usage information for each directory within the base path and sort it based on memory usage
    sorted_output = subprocess.check_output(['du', '-h', '--max-depth=2', base_path]).decode('utf-8')
    sorted_output = sorted_output.split('\n')
    
    # Remove empty strings and handle lines with unexpected format
    sorted_output = [line for line in sorted_output if line.strip()]
    sorted_output.sort(reverse=True, key=lambda x: convert_to_bytes(x.split()[0]))  # Sort based on memory usage
    sorted_output = '\n'.join(sorted_output)
    return sorted_output

if __name__ == "__main__":
    base_path = "/home"
    sorted_disk_usage = sort_disk_usage(base_path)
    
    with open("disk_usage_info.txt", "w") as file:
        file.write(sorted_disk_usage)
    
    print(sorted_disk_usage)
    print("Disk usage information sorted successfully and written to disk_usage_info.txt")
