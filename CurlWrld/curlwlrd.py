import json
import os

# ---------- File Names ----------
# Data is stored in JSON files so it persists between runs
DATA_FILE = "hairstyles.json"
FAV_FILE = "favorites.json"

# ---------- Helpers ----------
def load_data(file):
    """
    Load data from a JSON file.
    If the file doesn't exist, return an empty list.
    """
    if not os.path.exists(file):
        return []
    with open(file, "r") as f:
        return json.load(f)

def save_data(file, data):
    """
    Save data to a JSON file with indentation for readability.
    """
    with open(file, "w") as f:
        json.dump(data, f, indent=4)

# ---------- Main Features ----------
def view_hairstyles(hairstyles):
    """
    Display all hairstyles in the database.
    """
    if not hairstyles:
        print("\nNo hairstyles available yet.\n")
        return
    print("\n--- All Hairstyles ---")
    for i, style in enumerate(hairstyles, 1):
        print(f"{i}. {style['name']} ({style['type']}) - {style['occasion']}")

def filter_by_type(hairstyles):
    """
    Filter hairstyles by type (kinky, coily, curly).
    """
    hair_type = input("\nEnter hair type (kinky/coily/curly): ").strip().lower()
    filtered = [h for h in hairstyles if h['type'].lower() == hair_type]
    if not filtered:
        print(f"\nNo hairstyles found for {hair_type} hair.\n")
        return
    print(f"\n--- Hairstyles for {hair_type.title()} Hair ---")
    for i, style in enumerate(filtered, 1):
        print(f"{i}. {style['name']} - {style['occasion']}")

def save_favorite(hairstyles):
    """
    Allow the user to pick a hairstyle and save it to favorites.json.
    """
    view_hairstyles(hairstyles)
    choice = input("\nEnter the number of the hairstyle to save as favorite: ").strip()
    if not choice.isdigit() or int(choice) < 1 or int(choice) > len(hairstyles):
        print("Invalid choice.")
        return
    favorites = load_data(FAV_FILE)
    favorites.append(hairstyles[int(choice) - 1])
    save_data(FAV_FILE, favorites)
    print("Added to favorites!")

def view_favorites():
    """
    Display the user's saved favorite hairstyles.
    """
    favorites = load_data(FAV_FILE)
    if not favorites:
        print("\nNo favorites saved yet.\n")
        return
    print("\n--- Your Favorites ---")
    for i, style in enumerate(favorites, 1):
        print(f"{i}. {style['name']} ({style['type']}) - {style['occasion']}")

# ---------- Menu ----------
def main():
    """
    Main menu loop for CurlWrld.
    Allows the user to choose different actions.
    """
    hairstyles = load_data(DATA_FILE)

    while True:
        print("\n=== CurlWrld Menu ===")
        print("1. View All Hairstyles")
        print("2. Filter by Hair Type")
        print("3. Save Hairstyle to Favorites")
        print("4. View Favorites")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            view_hairstyles(hairstyles)
        elif choice == "2":
            filter_by_type(hairstyles)
        elif choice == "3":
            save_favorite(hairstyles)
        elif choice == "4":
            view_favorites()
        elif choice == "5":
            print("Goodbye from CurlWrld 👋")
            break
        else:
            print("Invalid option, try again!")

# ---------- Entry Point ----------
if __name__ == "__main__":
    # Add starter data if hairstyles.json doesn't exist yet
    starter_data = [
        {"name": "Twist Out", "type": "kinky", "occasion": "Casual"},
        {"name": "Bantu Knots", "type": "coily", "occasion": "Formal"},
        {"name": "Wash and Go", "type": "curly", "occasion": "Everyday"}
    ]
    if not os.path.exists(DATA_FILE):
        save_data(DATA_FILE, starter_data)
    main()