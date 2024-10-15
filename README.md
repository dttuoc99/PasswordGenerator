# PasswordGenerator(v1.0)
I want to create a simple password generator tools which will generate a wordlist of passwords for me to spray during bug hunting :)))

## Usage
```
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
```

## Example
```
❯ python3 password-generator.py --domain example123group --num 123 --special --mode uppercase --limit 10
EXAMPLE123GROUP$123
EXAMPLE123GROUP@123
EXAMPLE123GROUP&123
EXAMPLE123GROUP%123
EXAMPLE123GROUP#123
EXAMPLE123GROUP#123
EXAMPLE123GROUP&123
EXAMPLE123GROUP&123
EXAMPLE123GROUP$123
EXAMPLE123GROUP@123

❯ python3 password-generator.py --domain example123group --num 123 --special --limit 10
example123group@123
example123group%123
example123group#123
example123group&123
example123group&123
example123group#123
example123group%123
example123group$123
example123group&123
example123group%123

❯ python3 password-generator.py --domain example123group --num 123 --special --mode random --limit 10
eXAMPlE123GrOUp#123
eXampLe123GROup&123
examPle123GrOuP%123
ExaMpLE123GrouP@123
ExAMpLE123gRoUP&123
exaMple123GROUp&123
EXAmple123grouP$123
exAmplE123groUP%123
eXaMpLE123gRoup%123
exAMpLE123GRouP@123
```
