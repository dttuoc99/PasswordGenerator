#!/usr/bin/env python3

import argparse
import random
import string

def parse_arguments():
    """
    Parse command line arguments using argparse.
    
    Returns:
        ArgumentParser instance
    """
    parser = argparse.ArgumentParser(description="Generate domain combinations with numbers and special characters.")
    
    # Argument 1: Domain
    parser.add_argument('--domain', type=str, required=True, help="Domain string (e.g., 'cj23group')")
    
    # Argument 2: Number range or single number
    parser.add_argument('--num', type=str, required=True, help="Number or range (e.g., '1-2024' or '2004')")
    
    # Argument 3: Special characters (no input, just flag)
    parser.add_argument('--special', action='store_true', help="Add special characters (e.g., '@', '#')")
    
    # Argument 4: Limit number of results
    parser.add_argument('--limit', type=int, default=100, help="Limit number of generated outputs (default: 100)")
    
    # Argument 5: Switch between modes ('uppercase', 'lowercase', or 'random')
    parser.add_argument('--mode', choices=['uppercase', 'lowercase', 'random'], default='lowercase', help="Switch between modes (uppercase, lowercase, or random)")

    return parser.parse_args()

def parse_number_range(num_range):
    if '-' in num_range:
        start, end = map(int, num_range.split('-'))
        return list(range(start, end + 1))
    else:
        return [int(num_range)]

def generate_variations(domain, numbers, add_special, limit):
    special_characters = ['@', '#', '$', '%', '&'] if add_special else ['']
    variations = []

    # Case variations for the domain string
    case_variants = [domain.lower(), domain.upper(), domain.capitalize(), domain.swapcase()]

    for case_variant in case_variants:
        for number in numbers:
            for special in special_characters:
                # Form the string: domain + special + number
                generated_string = f"{case_variant}{special}{number}"
                variations.append(generated_string)

    # Shuffle the result to add randomness
    random.shuffle(variations)
    
    return variations[:limit]

def randomize_string_case(s):
    """
    Randomly convert each character in the string to uppercase or lowercase.
    """
    return ''.join(random.choice([char.upper(), char.lower()]) for char in s)

def apply_mode(results, mode):
    """
    Apply mode to the results: either convert all to uppercase, lowercase, or randomly case-mix each string.
    """
    if mode == 'uppercase':
        return [result.upper() for result in results]
    elif mode == 'lowercase':
        return [result.lower() for result in results]
    elif mode == 'random':
        return [randomize_string_case(result) for result in results]
    return results

def main():
    args = parse_arguments()

    # Argument 1: Domain
    domain = args.domain

    # Argument 2: Parse the number(s)
    numbers = parse_number_range(args.num)

    # Argument 3: Add special characters if flagged
    add_special = args.special

    # Argument 4: Limit
    limit = args.limit

    # Argument 5: Mode
    mode = args.mode

    # Generate combinations
    results = generate_variations(domain, numbers, add_special, limit)

    # Apply mode to results
    results = apply_mode(results, mode)

    # Output the results
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
