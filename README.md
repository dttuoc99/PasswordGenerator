# PasswordGenerator-simple-
I want to create a simple password generator tools which will generate a wordlist of passwords for me to spray during bug hunting :)))

## Usage
❯ python3 password-generator.py --help
usage: password-generator.py [-h] --domain DOMAIN --num NUM [--special] [--limit LIMIT]
                             [--mode {uppercase,lowercase,random}]

Generate domain combinations with numbers and special characters.

options:
  -h, --help            show this help message and exit
  --domain DOMAIN       Domain string (e.g., 'cj23group')
  --num NUM             Number or range (e.g., '1-2024' or '2004')
  --special             Add special characters (e.g., '@', '#')
  --limit LIMIT         Limit number of generated outputs (default: 100)
  --mode {uppercase,lowercase,random}
                        Switch between modes (uppercase, lowercase, or random)
