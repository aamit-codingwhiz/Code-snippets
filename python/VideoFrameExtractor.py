import cv2
import os

class VideoFrameExtractor:
    """
    A class for extracting frames from a video and saving them as individual image files.
    """

    def __init__(self, video_path, output_folder):
        """
        Initializes a new VideoFrameExtractor object.

        :param video_path: The path to the input video file.
        :type video_path: str
        :param output_folder: The path to the folder where the extracted frames will be saved.
        :type output_folder: str
        """
        self.video_path = video_path
        self.output_folder = output_folder
        self.cap = cv2.VideoCapture(video_path)
        self.frame_number = 0

        # Create the output folder if it doesn't exist
        if not os.path.exists(output_folder):
            os.mkdir(output_folder)

    def extract_frames(self):
        """
        Extracts frames from the video and saves them in the output folder.
        """
        while True:
            # Read the current frame
            ret, frame = self.cap.read()

            # Break the loop if the video has ended
            if not ret:
                break

            # Save the frame to the output folder
            frame_path = os.path.join(self.output_folder, f"frame_{self.frame_number:04d}.jpg")
            cv2.imwrite(frame_path, frame)

            # Increment the frame number
            self.frame_number += 1

    def release(self):
        """
        Releases the video capture object.
        """
        self.cap.release()

   
# example usage
extractor = VideoFrameExtractor("path/to/video.mp4", "path/to/output/folder")
extractor.extract_frames()
extractor.release()
