import exiftool

# Define an array of file paths
base_path = r"C:\Users\drago\Desktop\Python Projects\photo-organization-tool\MetadataTest"
file_paths = ["edit1.JPG", "edit2.JPG", "edit3.JPG", "YOMAMA.txt", "doesnotexist.JPG"]

# Define the new title
new_rating = "5"

# Prepare the arguments for ExifTool
args = [b"-Rating=" + new_rating.encode('utf-8'), b"-overwrite_original"]

# Add the file paths to the argument list
args.extend([(base_path + "\\" + file_path).encode('utf-8') for file_path in file_paths])

failed_files = []

# Use ExifTool to set the title and overwrite the original files
with exiftool.ExifTool() as et:
    result = et.execute(*args)

# Check the result to determine if any files failed
print(result.splitlines())
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