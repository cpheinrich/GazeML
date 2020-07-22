import subprocess
import argparse
import os

""" 

This is a convenience entrypoint for running the elg_demo.py file end-to-end. 

The main difference between this entrypoint and simply using elg_demo.py, is that this
entrypoint supports a --from_dir argument which will attempt to run on all files in a
provided directory one after another
"""

VIDEO_EXTENSIONS = ['.mov', '.mp4', '.wmv', '.flv', '.avi', '.mpeg', '.mpg', '.webm', '.ogg']


def run_inference(from_video):
    args = ["python3", "elg_demo.py", "--from_video", from_video]
    subprocess.call(args)


def is_video(path):
    name, ext = os.path.splitext(path)
    ext = ext.lower()
    if ext in VIDEO_EXTENSIONS:
        return True
    else:
        return False


if __name__ == '__main__':
    # Set global log level
    parser = argparse.ArgumentParser(description='Demonstration of landmarks localization.')
    parser.add_argument('--from_video', type=str, help='Use this video path instead of webcam')
    parser.add_argument('--from_dir', type=str, help='Path to a directory of videos')

    args = parser.parse_args()
    if args.from_video is not None:
        run_inference(args.from_video)
    elif args.from_dir is not None:
        videos = os.listdir(args.from_dir)
        for video in videos:
            if is_video(video):
                video_path = os.path.join(args.from_dir, video)
                run_inference(video_path)
            else:
                print("{} is not a valid video format. Skipping".format(video))
    else:
        raise NotImplementedError(
            """You must supply a video path to the --from_video argument or a path to a directory of videos with the  --from_dir argument to run inference!""")
