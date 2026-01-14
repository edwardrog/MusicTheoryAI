# 🎵 MusicTheoryAI

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Stars](https://img.shields.io/github/stars/edwardrog/MusicTheoryAI?style=social)](https://github.com/edwardrog/MusicTheoryAI)

An interactive Python platform combining music education with AI technology. Learn music theory through gamified exercises, real-time feedback, and personalized learning paths.

## ✨ Features

- 🎼 **Interactive Music Theory Lessons** - Learn scales, chords, progressions, and harmony
- 🤖 **AI-Powered Exercises** - Adaptive difficulty based on your learning pace
- 🎹 **MIDI Integration** - Connect your musical instruments for real-time feedback
- 📊 **Progress Tracking** - Detailed analytics on your learning journey
- 🌐 **Web Interface** - Modern, responsive UI built with Flask
- 🎓 **Curriculum** - Structured learning paths from beginner to advanced

## 🚀 Quick Start

### Prerequisites

- Python 3.9 or higher
- pip or conda
- Optional: MIDI device for instrument input

### Installation

```bash
git clone https://github.com/edwardrog/MusicTheoryAI.git
cd MusicTheoryAI
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

Visit `http://localhost:5000`

## 📚 Documentation

- [Getting Started Guide](docs/GETTING_STARTED.md)
- [API Documentation](docs/API.md)
- [Contributing Guide](CONTRIBUTING.md)

## 🎯 Project Roadmap

- [ ] v0.1 - Basic scale and chord recognition
- [ ] v0.2 - MIDI input integration
- [ ] v0.3 - Web UI with progress tracking
- [ ] v0.4 - AI-powered adaptive learning
- [ ] v1.0 - Full curriculum and analytics

## 🏗️ Project Structure

```
MusicTheoryAI/
├── app.py
├── requirements.txt
├── src/
│   ├── theory/
│   │   ├── scales.py
│   │   ├── chords.py
│   │   └── intervals.py
│   ├── ai/
│   │   └── model.py
│   ├── midi/
│   │   └── handler.py
│   └── api/
│       └── routes.py
├── templates/
├── static/
├── tests/
└── docs/
```

## 🧪 Testing

```bash
pytest
pytest --cov=src
```

## 🤝 Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📄 License

MIT License - See [LICENSE](LICENSE)

---

**Status:** Active Development 🚀 | **Last Updated:** January 2026
