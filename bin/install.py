import os
import shutil

if __name__ == "__main__":
    # vault_path = input("Enter the Obsidian vault path: ")
    vault_path = "/Users/jplatta/Library/Mobile Documents/iCloud~md~obsidian/Documents/development_vault"
    print("Vault path: " + vault_path)

    if not os.path.exists(vault_path):
        print("Vault path does not exist.")
        exit(1)

    plugins_path = os.path.join(vault_path, ".obsidian", "plugins")
    if not os.path.exists(plugins_path):
        print("Plugins path does not exist.")
        exit(1)

    plugin_path = os.path.join(plugins_path, "note_secretary")
    if os.path.exists(plugin_path):
        answer = input("Plugin already installed. Reinstall? (y/n): ")
        if answer != "y":
            print("Exiting.")
            exit(1)
    else:
        os.mkdir(plugin_path)

    print("Installing plugin...")

    os.system("npm install")
    os.system("npm run build")

    install_files = [
        "main.js",
        "manifest.json",
        "styles.css",
        "LICENSE",
        "README.md",
    ]

    for file_name in install_files:
        filepath = os.path.join(os.getcwd(), file_name)
        if os.path.isfile(filepath):
            shutil.copy(filepath, plugin_path)

    print("Plugin installed.")