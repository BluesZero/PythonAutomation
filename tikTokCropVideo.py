from moviepy.editor import VideoFileClip

def trimVideoForTikTok(originalVideoPath, outputVideoPath):
    # Load the video
    clip = VideoFileClip(originalVideoPath)

    # Get original dimensions of the video
    originalWidth, originalHeight = clip.size

    # Calculate new dimensions for 9:16 format, ensuring they are even numbers
    if originalWidth / originalHeight < 9 / 16:
        # Adjust by width
        newWidth = originalWidth
        newHeight = int(originalWidth * 16 / 9)
    else:
        # Adjust by height
        newWidth = int(originalHeight * 9 / 16)
        newHeight = originalHeight

    # Ensure dimensions are even
    newWidth -= newWidth % 2
    newHeight -= newHeight % 2

    # Coordinates for centered crop
    x1 = (originalWidth - newWidth) // 2
    y1 = (originalHeight - newHeight) // 2
    x2 = x1 + newWidth
    y2 = y1 + newHeight

    # Crop the video
    croppedVideo = clip.crop(x1=x1, y1=y1, x2=x2, y2=y2)

    # Save the video with additional parameters for compatibility
    croppedVideo.write_videofile(outputVideoPath, codec='libx264', audio_codec='aac',
                                 bitrate='8000k', preset='fast',
                                 ffmpeg_params=["-pix_fmt", "yuv420p", "-profile:v", "baseline", "-level", "3.0"])

# Example of usage
trimVideoForTikTok('./magicalDestroyer.mp4', 'cropped_video.mp4')
