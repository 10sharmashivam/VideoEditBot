# VideoEditBot

VideoEditBot is an AI-powered video editing tool that automates clip trimming using natural language prompts (e.g., "trim first 30 seconds" or "extract highlights"). Built with HuggingFace for NLP, Flask for the web interface, and FFmpeg for video processing, this project demonstrates skills in AI, web development, and media processing.

## Features
- Upload a video file via a web interface.
- Input NLP prompts to specify video edits (e.g., "cut last 10 seconds").
- Parse prompts using a rule-based NLP parser.
- Process videos with FFmpeg for fast, high-quality trimming.
- Download the edited video.

## Tech Stack
- **Python**: Core programming language.
- **Flask**: Lightweight web framework.
- **HuggingFace Transformers**: NLP for parsing user prompts.
- **FFmpeg**: Video processing with `ffmpeg-python`.
- **HTML/CSS**: Simple frontend for user interaction.

```
Ubuntu: sudo apt-get install ffmpeg
macOS: brew install ffmpeg
Windows: Download from ffmpeg.org and add to PATH.
```

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/10sharmashivam/VideoEditBot.git
   cd VideoEditBot