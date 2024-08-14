import exiftool
import time

def set_metadata(base_path, file_path, subject, new_value):
    with exiftool.ExifTool() as et:
        result = et.execute(f"-{subject}={new_value}".encode('utf-8'), b"-overwrite_original", (base_path + "\\" + file_path).encode('utf-8'))
    return result


if __name__ == "__main__":
    # Define an array of file paths
    base_path = r"C:\Users\drago\Desktop\Python Projects\photo-organization-tool\MetadataTest"
    # file_paths = ["edit1.JPG", "edit2.JPG", "edit3.JPG"]
    file_paths = [f"edit1 - Copy ({i + 2})" for i in range(35)]

    # Define the new title
    subject = "Rating"
    new_rating = "5"

    start_time = time.time()

    for file in file_paths:
        set_metadata(base_path, file, subject, new_rating)
        print(file)

    # Stop the timer
    end_time = time.time()

    # Calculate the time taken
    time_taken = end_time - start_time

    # Print the time taken
    print(f"\nTime taken : {time_taken:.4f} seconds")

# if result:
#     output = result.decode('utf-8').splitlines()
#     for line in output:
#         if "Error" in line:
#             # Extract the filename from the error message
#             for file_path in file_paths:
#                 if file_path in line:
#                     failed_files.append(file_path)
#
# # Output the results
# if failed_files:
#     print("Failed to update the following files:")
#     for failed_file in failed_files:
#         print(failed_file)
# else:
#     print("Title metadata updated and original files overwritten successfully!")
#
# print("Title metadata updated and original files overwritten successfully!")