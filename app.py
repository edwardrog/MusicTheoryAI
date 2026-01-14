"""
MusicTheoryAI - Interactive Music Education Platform
Main Flask application entry point
"""

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import json
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Configure app
app.config['JSON_SORT_KEYS'] = False


class MusicalNote:
      """Represents a musical note with frequency information"""

    NOTE_FREQUENCIES = {
              'C': 261.63, 'C#': 277.18, 'D': 293.66, 'D#': 311.13,
              'E': 329.63, 'F': 349.23, 'F#': 369.99, 'G': 392.00,
              'G#': 415.30, 'A': 440.00, 'A#': 466.16, 'B': 493.88
    }

    def __init__(self, name):
              """Initialize a note with its name"""
              if name not in self.NOTE_FREQUENCIES:
                            raise ValueError(f"Invalid note: {name}")
                        self.name = name
        self.frequency = self.NOTE_FREQUENCIES[name]

    def get_info(self):
              """Get information about the note"""
        return {
                      'name': self.name,
                      'frequency': self.frequency,
                      'octave': 4
        }


class Chord:
      """Represents a musical chord"""

    CHORD_TYPES = {
              'major': [0, 4, 7],
              'minor': [0, 3, 7],
              'major7': [0, 4, 7, 11],
              'minor7': [0, 3, 7, 10],
              'dominant7': [0, 4, 7, 10],
    }

    def __init__(self, root, chord_type='major'):
              """Initialize a chord"""
        if chord_type not in self.CHORD_TYPES:
                      raise ValueError(f"Invalid chord type: {chord_type}")
                  self.root = root
        self.chord_type = chord_type
        self.intervals = self.CHORD_TYPES[chord_type]

    def get_notes(self):
              """Get the notes that make up this chord"""
        notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        root_index = notes.index(self.root)
        chord_notes = []

        for interval in self.intervals:
                      note_index = (root_index + interval) % 12
                      chord_notes.append(notes[note_index])

        return chord_notes

    def get_info(self):
              """Get information about the chord"""
        return {
                      'root': self.root,
                      'type': self.chord_type,
                      'notes': self.get_notes(),
                      'intervals': self.intervals
        }


class Scale:
      """Represents a musical scale"""

    SCALE_PATTERNS = {
              'major': [0, 2, 4, 5, 7, 9, 11],
              'minor': [0, 2, 3, 5, 7, 8, 10],
              'pentatonic_major': [0, 2, 4, 7, 9],
              'pentatonic_minor': [0, 3, 5, 7, 10],
              'blues': [0, 3, 5, 6, 7, 10],
    }

    def __init__(self, root, scale_type='major'):
              """Initialize a scale"""
        if scale_type not in self.SCALE_PATTERNS:
                      raise ValueError(f"Invalid scale type: {scale_type}")
                  self.root = root
        self.scale_type = scale_type
        self.pattern = self.SCALE_PATTERNS[scale_type]

    def get_notes(self):
              """Get all notes in this scale"""
        notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        root_index = notes.index(self.root)
        scale_notes = []

        for interval in self.pattern:
                      note_index = (root_index + interval) % 12
                      scale_notes.append(notes[note_index])

        return scale_notes

    def get_info(self):
              """Get information about the scale"""
        return {
                      'root': self.root,
                      'type': self.scale_type,
                      'notes': self.get_notes(),
                      'pattern': self.pattern
        }


# Routes
@app.route('/')
def index():
      """Home page"""
    return jsonify({
              'message': 'Welcome to MusicTheoryAI',
              'description': 'An interactive platform for learning music theory',
              'version': '0.1.0',
              'endpoints': {
                            '/api/note/<note>': 'Get information about a note',
                            '/api/chord/<root>/<type>': 'Get information about a chord',
                            '/api/scale/<root>/<type>': 'Get information about a scale',
                            '/api/health': 'Health check endpoint'
              }
    })


@app.route('/api/health')
def health():
      """Health check endpoint"""
    return jsonify({
              'status': 'healthy',
              'timestamp': datetime.now().isoformat()
    })


@app.route('/api/note/<note>')
def get_note(note):
      """Get information about a specific note"""
    try:
              musical_note = MusicalNote(note)
        return jsonify(musical_note.get_info())
except ValueError as e:
        return jsonify({'error': str(e)}), 400


@app.route('/api/chord/<root>/<chord_type>')
def get_chord(root, chord_type):
      """Get information about a chord"""
    try:
              chord = Chord(root, chord_type)
        return jsonify(chord.get_info())
except ValueError as e:
        return jsonify({'error': str(e)}), 400


@app.route('/api/scale/<root>/<scale_type>')
def get_scale(root, scale_type):
      """Get information about a scale"""
    try:
              scale = Scale(root, scale_type)
        return jsonify(scale.get_info())
except ValueError as e:
        return jsonify({'error': str(e)}), 400


@app.route('/api/notes')
def get_all_notes():
      """Get all available notes"""
    return jsonify({
              'notes': list(MusicalNote.NOTE_FREQUENCIES.keys()),
              'count': len(MusicalNote.NOTE_FREQUENCIES)
    })


@app.route('/api/chord-types')
def get_chord_types():
      """Get all available chord types"""
    return jsonify({
              'types': list(Chord.CHORD_TYPES.keys()),
              'count': len(Chord.CHORD_TYPES)
    })


@app.route('/api/scale-types')
def get_scale_types():
      """Get all available scale types"""
    return jsonify({
              'types': list(Scale.SCALE_PATTERNS.keys()),
              'count': len(Scale.SCALE_PATTERNS)
    })


if __name__ == '__main__':
      app.run(debug=True, host='0.0.0.0', port=5000)
