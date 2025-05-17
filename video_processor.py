import ffmpeg
import os

def process_video(input_path, output_path, action):
    try:
        probe = ffmpeg.probe(input_path)
        duration = float(probe['format']['duration'])

        if action['action'] == 'trim':
            stream = ffmpeg.input(input_path, ss=action['start'], t=action['duration'])
            stream = ffmpeg.output(stream, output_path, c='copy', loglevel='quiet')
            ffmpeg.run(stream)

        elif action['action'] == 'trim_end':
            start = max(0, duration - action['duration'])
            stream = ffmpeg.input(input_path, ss=start)
            stream = ffmpeg.output(stream, output_path, c='copy', loglevel='quiet')
            ffmpeg.run(stream)

        elif action['action'] == 'highlights':
            # Heuristic: Take middle 20% of video
            start = duration * 0.4
            length = duration * 0.2
            stream = ffmpeg.input(input_path, ss=start, t=length)
            stream = ffmpeg.output(stream, output_path, c='copy', loglevel='quiet')
            ffmpeg.run(stream)

        else:
            raise ValueError("Invalid action")

        return True
    except Exception as e:
        print(f"Error processing video: {e}")
        return False