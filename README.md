# Password Strength Analyzer

A small Python cybersecurity project that evaluates password strength using length, character diversity, common-password checks, repeated characters, and predictable sequences. It returns a score, classification, and practical recommendations.

## Features

- Scores passwords from 0 to 100
- Classifies results as **WEAK**, **FAIR**, **GOOD**, or **STRONG**
- Checks uppercase, lowercase, numeric, and special characters
- Flags a small set of common weak passwords
- Detects repeated characters and simple predictable sequences
- Uses `getpass` so the entered password is not displayed in the terminal
- Does not intentionally save, log, or transmit the password
- Includes automated unit tests
- Uses only the Python standard library

## Project Structure

```text
password-strength-analyzer/
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
├── main.py
├── password_analyzer.py
└── tests/
    └── test_password_analyzer.py
```

## Requirements

- Python 3.9 or later recommended
- No third-party Python packages are required

## Run the Project

From the project directory:

```bash
python main.py
```

On some systems, use:

```bash
python3 main.py
```

## Run Tests

```bash
python -m unittest discover -s tests -v
```

## Scoring Categories

- **0-39:** Weak
- **40-59:** Fair
- **60-79:** Good
- **80-100:** Strong

The score is an educational heuristic, not a formal measurement of password entropy or a guarantee that a password is secure.

## Security and Privacy

The command-line program analyzes the password locally in memory. The application does not contain code to write entered passwords to files, databases, logs, or network services. Avoid using your real production passwords when demonstrating or testing software.

## Possible Future Improvements

- Configurable password policies
- Expanded compromised/common-password detection using an offline dataset
- Entropy estimation
- Graphical or web interface
- Localization
- Continuous integration for automated tests

## Educational Use

This project can support introductory lessons on password security, secure input handling, Python functions, regular expressions, unit testing, and Git/GitHub workflows.

## Author

**Dr. Opeoluwa Omotayo Ajilore**  
Lecturer, Computer Science

## License

Released under the MIT License. See [LICENSE](LICENSE).
