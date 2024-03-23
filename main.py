import wave
import sys

import pyaudio

file_name = "file_example_WAV_1MG.wav"

CHUNK = 1024

with wave.open(file_name, 'rb') as wf:
    # Instantiate PyAudio and initialize PortAudio system resources (1)
    p = pyaudio.PyAudio()

    print(p.get_host_api_count())
    print()

    # Open stream (2)
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    # Play samples from the wave file (3)
    while len(data := wf.readframes(CHUNK)):  # Requires Python 3.8+ for :=
        stream.write(data)

    # Close stream (4)
    stream.close()

    # Release PortAudio system resources (5)
    p.terminate()


# import os
# import time
# from spot_controller import SpotController
# import cv2

# ROBOT_IP = "10.0.0.3"#os.environ['ROBOT_IP']
# SPOT_USERNAME = "admin"#os.environ['SPOT_USERNAME']
# SPOT_PASSWORD = "2zqa8dgw7lor"#os.environ['SPOT_PASSWORD']


# def capture_image():
#     camera_capture = cv2.VideoCapture(0)
#     rv, image = camera_capture.read()
#     print(f"Image Dimensions: {image.shape}")
#     camera_capture.release()
#     cv2.imwrite(f'/merklebot/job_data/camera_{time.time()}.jpg', image)


# def main():
#     #example of using micro and speakers
#     print("Start recording audio")
#     sample_name = "aaaa.wav"
#     cmd = f'arecord -vv --format=cd --device={os.environ["AUDIO_INPUT_DEVICE"]} -r 48000 --duration=10 -c 1 {sample_name}'
#     print(cmd)
#     os.system(cmd)
#     print("Playing sound")
#     os.system(f"ffplay -nodisp -autoexit -loglevel quiet {sample_name}")
    
#     # # Capture image

#     # Use wrapper in context manager to lease control, turn on E-Stop, power on the robot and stand up at start
#     # and to return lease + sit down at the end
#     with SpotController(username=SPOT_USERNAME, password=SPOT_PASSWORD, robot_ip=ROBOT_IP) as spot:

#         time.sleep(2)
#         capture_image()
#         # Move head to specified positions with intermediate time.sleep
#         spot.move_head_in_points(yaws=[0.2, 0],
#                                  pitches=[0.3, 0],
#                                  rolls=[0.4, 0],
#                                  sleep_after_point_reached=1)
#         capture_image()
#         time.sleep(3)

#         # Make Spot to move by goal_x meters forward and goal_y meters left
#         spot.move_to_goal(goal_x=0.5, goal_y=0)
#         time.sleep(3)
#         capture_image()

#         # Control Spot by velocity in m/s (or in rad/s for rotation)
#         spot.move_by_velocity_control(v_x=-0.3, v_y=0, v_rot=0, cmd_duration=2)
#         capture_image()
#         time.sleep(3)


# if __name__ == '__main__':
#     main()
