
import os
import zipfile
import glob

urls = ["https://ait.ethz.ch/projects/2018/landmarks-gaze/downloads/ELG_i180x108_f60x36_n64_m3.zip",
        "https://ait.ethz.ch/projects/2018/landmarks-gaze/downloads/ELG_i60x36_f60x36_n32_m2.zip"]


def unzip_files(file_dir):
    """ Unzips zip files in file_dir
    Args:
        file_dir: Absolute path to a directory containing zip files
    """
    print("Unzipping files in {}".format(file_dir))
    zip_files = glob.glob(os.path.join(file_dir, "*.zip"))
    for zip_file in zip_files:
        root, ext = os.path.splitext(zip_file)
        if os.path.isdir(root):
            print("Zip file {} is already unzipped".format(zip_file))
        else:
            print("Unzipping file {}".format(zip_file))
            unzipper = zipfile.ZipFile(zip_file, 'r')
            unzipper.extractall(file_dir)


def get_weights(dest_dir):
    import wget
    for url in urls:
        file_name = os.path.basename(url)
        dest_path = os.path.join(dest_dir, file_name)
        if os.path.exists(dest_path):
            print("Weight file {} already downloaded".format(file_name))
        else:
            print("Downloading weights from {} to {}".format(url, dest_path))
            os.makedirs(dest_dir, exist_ok=True)
            wget.download(url, out=dest_path)
    unzip_files(dest_dir)
