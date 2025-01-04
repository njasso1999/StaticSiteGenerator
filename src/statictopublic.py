import os
import shutil

def static_to_public(directory):
    public_dir = "./public" + directory.replace("./static", "")
    if directory == "./static":
        shutil.rmtree("./public")
        os.mkdir("./public")
    directory_list = os.listdir(directory)
    for file in directory_list:
        file_directory = os.path.join(directory, file)
        if os.path.isfile(file_directory):
            shutil.copy(file_directory, public_dir)
        else:
            child_dir = os.path.join(public_dir, file)
            os.mkdir(child_dir)
            static_to_public(file_directory)