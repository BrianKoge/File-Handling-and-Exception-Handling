# Step 1: Function to read from a file
def read_file(filename):
    try:
        with open(filename, "r") as f:   # open in read mode
            content = f.read()
        return content
    except FileNotFoundError:
        print(f"❌ Error: The file '{filename}' was not found.")
        return None
    except PermissionError:
        print(f"❌ Error: You don’t have permission to read '{filename}'.")
        return None


# Step 2: Function to modify the content
def modify_content(content):
    # Example modification: make text uppercase & add a footer
    modified = content.upper()
    modified += "\n\n--- Modified by Python Program ---"
    return modified


# Step 3: Function to write to a new file
def write_file(new_filename, content):
    with open(new_filename, "w") as f:   # open in write mode
        f.write(content)


# Step 4: Main program to call functions
def main():
    filename = input("Enter the filename to read: ")
    content = read_file(filename)

    if content is not None:   # proceed only if reading succeeded
        modified = modify_content(content)
        new_filename = "modified_" + filename
        write_file(new_filename, modified)

        # Step 5: Print success message
        print(f"✅ File successfully modified and saved as '{new_filename}'.")


# Run the program
if __name__ == "__main__":
    main()
