# Codveda-Project
# Word Counter

A beginner-level Python program that reads the contents of a plain text file and reports the total number of words. The program validates user input, checks for file existence, and handles edge cases such as empty files — making it a practical introduction to file handling and exception management in Python.

---

## Features

- Reads any plain text file specified by the user
- Counts total words by splitting on spaces and newlines
- Validates that the file exists before attempting to open it
- Detects and reports empty files without crashing
- No third-party libraries required — uses Python standard library only

---

## Getting Started

### Prerequisites

Python 3.x must be installed. No external packages are required. Verify your installation by running:

```bash
python --version
```

### Installation

1. Download or clone the project files to your local machine.
2. Place `word_counter.py` in a folder of your choice.
3. Add a plain text file (e.g. `sample.txt`) to the same folder for testing.
4. Open a terminal or command prompt and navigate to the project folder.
5. Run the program using the command below.

```bash
python word_counter.py
```

---

## Usage

When the program runs, it will prompt you to enter a file name. Type the name of the text file (including the `.txt` extension) and press Enter. The program will display the total word count, or an appropriate error message if the file is not found or is empty.

### Example — Successful count

```
Enter the file name: sample.txt
File: sample.txt
Total words: 47
```

### Example — File not found

```
Enter the file name: missing.txt
Error: File not found.
```

### Example — Empty file

```
Enter the file name: empty.txt
The file is empty.
```

---

## Error Handling

The program covers three scenarios:

| Scenario | Handling Method | Message Displayed |
|----------|-----------------|-------------------|
| File does not exist | `os.path.exists()` check | Error: File not found. |
| File is empty | `contents.strip()` check | The file is empty. |
| File is valid | `words.split()` + `len()` | Total word count shown |

---

## Project Structure

```
word-counter/
│
├── word_counter.py     # Main program
├── sample.txt          # Example input file (optional)
└── README.md           # Project documentation
```

---

## License

This project is open source and free to use for educational and learning purposes.
