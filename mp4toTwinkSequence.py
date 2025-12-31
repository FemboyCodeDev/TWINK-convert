import cv2

def process_video(video_path):
    # Create a VideoCapture object
    cap = cv2.VideoCapture(video_path)

    # Check if the video opened successfully
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    frame_count = 0

    while True:
        # cap.read() returns a boolean (ret) and the frame itself
        ret, frame = cap.read()

        # If ret is False, we have reached the end of the video
        if not ret:
            break

        # --- This is where you process your frame ---
        # For example, let's just display the frame count
        # and show the video in a window

        frame_count += 1

        if frame_count % 1 == 0:
            cv2.imshow('Video Frame', frame)

            frame_resized = cv2.resize(frame,(64,64))

            cv2.imshow('Video Frame Resized', frame_resized)

            img = frame_resized
            content = ""
            for x in range(64):
                for y in range(64):
                    r,g,b = img[x][y]
                    if r+g+b > 1:
                        if (r==g and g==b) or ((abs(r-g)<10) and (abs(r-b) < 10) and (abs(g-b) < 10)):
                            row = f"{y}:{x}:█:{r}"
                        else:
                            row = f"{y}:{x}:█:{r}:{g}:{b}"
                        content = content + row + "\n"
            with open(f"seq\\frame_{frame_count}.TWINK","w",encoding = "utf-8") as file:
                file.write(content)
            
            
            print(f"Processing frame: {frame_count}")

            # Press 'q' on the keyboard to exit the loop early
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    # Release the video capture object and close windows
    cap.release()
    cv2.destroyAllWindows()
    print(f"\nFinished! Total frames processed: {frame_count} :3")

if __name__ == "__main__":
    path_to_video = "bad-apple.mp4"
    process_video(path_to_video)
