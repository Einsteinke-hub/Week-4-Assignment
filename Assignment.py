def main():
    # Ask user for filename
    filename = input("Enter the filename to read: ")

    try:
        # Try opening the file
        with open(filename, "r") as python:
            content = python.read()
        
        # Modify content (example: make it uppercase)
        modified_content = content.upper()

        # Write to a new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as modified_python:
            modified_python.write(modified_content)

        print(f"✅ File has been modified and saved as: {new_filename}")

    except FileNotFoundError:
        print("❌ Error: The file does not exist. Please check the filename.")
    except PermissionError:
        print("❌ Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")

if __name__ == "__main__":
    main()
