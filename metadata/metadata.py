import exiftool


def read_metadata(file_path, subject, default_value=""):
    with exiftool.ExifToolHelper() as et:
        metadata = et.get_metadata(file_path)[0]
        return_value = ""
        try:
            return_value = metadata[subject]
        except KeyError:
            set_metadata(file_path, subject, "")
            return default_value
        if return_value:
            return return_value


def set_metadata(file_path, subject, new_value):
    with exiftool.ExifTool() as et:
        result = et.execute(f"-{subject}={new_value}".encode('utf-8'), b"-overwrite_original", file_path.encode('utf-8'))
    print(result)
    return result


if __name__ == "__main__":
    with exiftool.ExifToolHelper() as et:
        metadata = et.get_metadata(r"C:\Users\drago\Desktop\Python Projects\photo-organization-tool\assets\Ben.JPG")[0]
        print(metadata)

    # set_metadata(r"C:\Users\drago\Desktop\Python Projects\photo-organization-tool\assets/rando.JPG", "EXIF:XPComment", "This is new")