import os
import zipfile
import subprocess

def check_and_create_local_bin():
    local_bin_path = os.path.expanduser("~/.local/bin")
    if not os.path.exists(local_bin_path):
        os.makedirs(local_bin_path)
        print(f"Directory created: {local_bin_path}")
    else:
        print(f"Directory already exists: {local_bin_path}")
    return local_bin_path

def unzip_files(destination):
    zip_files = ["websrv.zip", "ligolo.zip"]
    for zip_file in zip_files:
        if os.path.isfile(zip_file):
            with zipfile.ZipFile(zip_file, 'r') as zip_ref:
                zip_ref.extractall(destination)
                print(f"Extracted {zip_file} to {destination}")
        else:
            print(f"File not found: {zip_file}")

def install_dependencies():
    try:
        subprocess.run(["sudo", "apt", "install", "-y", "mono-complete"], check=True)
        subprocess.run(["sudo", "apt", "install", "-y", "xbuild"], check=True)
        print("Dependencies installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing dependencies: {e}")

def add_alias():
    shell = os.environ.get('SHELL')
    alias_command = "alias ligolo='python3 ~/.local/bin/ligolo/ligolo.py'"

    if 'bash' in shell:
        rc_file = os.path.expanduser("~/.bashrc")
        print("Alias added to ~/.bashrc")
    elif 'zsh' in shell:
        rc_file = os.path.expanduser("~/.zshrc")
        print("Alias added to ~/.zshrc")
    else:
        print("Unsupported shell")
        return

    with open(rc_file, 'a') as file:
        file.write(f"\n{alias_command}\n")

    print(f"To apply the alias, run the following command:")
    print(f"source {rc_file}")

def chmod_websrv_files():
    websrv_dir = os.path.expanduser("~/.local/bin/websrv")
    if os.path.exists(websrv_dir):
        for root, dirs, files in os.walk(websrv_dir):
            for file in files:
                file_path = os.path.join(root, file)
                subprocess.run(["chmod", "+x", file_path])
                print(f"Made executable: {file_path}")
    else:
        print(f"Directory not found: {websrv_dir}")

if __name__ == "__main__":
    local_bin_dir = check_and_create_local_bin()
    unzip_files(local_bin_dir)
    install_dependencies()
    add_alias()
    chmod_websrv_files()
