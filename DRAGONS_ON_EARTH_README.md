# Dragons on Earth

A Python CLI application that generates fantasy dragon profiles, stories, and battle simulations.

## Features

- **Dragon Story Generator** - Random dragon tales for any location
- **Dragon Profile Creation** - Generate detailed dragon profiles with random stats
- **Dragon Battles** - Simulate battles between dragons
- **Dragon Lore** - Generate backstory for each dragon

## Requirements

- Python 3.11+
- No external dependencies (uses only standard library)

## Installation

```bash
git clone https://github.com/yourusername/dragons-on-earth.git
cd dragons-on-earth
python DragonsOnEarth.py
```

## Usage

```bash
python DragonsOnEarth.py
```

### Menu Options

1. **Simple Story** - Generate a random dragon story for a location
2. **Create Dragon Profile** - Build a detailed dragon with stats
3. **Battle Two Dragons** - Simulate a battle between dragons

## Example Output

```
=== DRAGONS ON EARTH ===

Enter a place: the mountain

1. Simple story
2. Create dragon profile
3. Battle two dragons

Choose option (1-3): 1

A dragon rises over the mountain, bringing wonder and flame.
```

## Docker

Build and run with Docker:

```bash
docker build -t dragons-on-earth .
docker run -it dragons-on-earth:latest
```

## License

MIT

## Author

Your Name
