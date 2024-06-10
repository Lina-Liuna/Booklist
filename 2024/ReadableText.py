def rearrange_text(text):
    """
    Rearranges text sections into a specific format, ensuring the third line doesn't exceed a character limit and avoiding extra spaces/hyphens.

    Args:
        text: String containing the text to rearrange.

    Returns:
        String containing the rearranged text.
    """
    sections = text.split('\n\n')
    rearranged_sections = []

    for i, section in enumerate(sections, start=1):
        lines = section.split('\n')

        # Find the first line break after the opening parenthesis
        first_line_break = section.find(')') + 1  # Add 1 to move to the character after ')'
        if first_line_break > 0:
            first_line = section[:first_line_break]
            second_line = section[first_line_break:]
        else:
            # If no opening parenthesis found, treat the whole section as the first line
            first_line = section
            second_line = ""  # Empty second line

        # Check if the first line contains any alphanumeric characters
        if not any(c.isalnum() for c in first_line):
            continue

        # Limit third line length (assuming character limit is around 80)
        max_third_line_length = 80  # Adjust this value as needed
        third_line_part = f"({', '.join(lines[2:])})"  # Authors and year in parenthesis
        if len(first_line.rstrip()) + len(third_line_part) > max_third_line_length:
            # If first line + third line part exceeds limit, shorten the first line with ellipsis (...)
            shortened_first_line = first_line.rstrip()[:max_third_line_length - len(third_line_part) - 3] + "..."
            rearranged_section = f"=== {i}. {shortened_first_line.strip()}) \n— {second_line.strip()} {third_line_part}"
        else:
            # Single hyphen only if second line exists, remove extra space
            hyphen = '-' if second_line and not second_line.startswith('-') else ''
            rearranged_section = f"=== {i}. {first_line.rstrip().strip()}) \n{hyphen} {second_line.strip()} {third_line_part}"

        rearranged_sections.append(rearranged_section)

    rearranged_text = '\n\n'.join(rearranged_sections)
    return rearranged_text


import re


def remove_number_lines(text):
    # Regular expression pattern to match lines containing numbers with '.' or ','
    pattern = r'^.*[0-9.,]+.*$'

    # Split the text into lines
    lines = text.split('\n')

    # Filter out lines containing numbers with '.' or ','
    filtered_lines = [line for line in lines if not re.match(pattern, line.strip()) or not line.strip()]

    # Join the remaining lines back into text
    filtered_text = '\n'.join(filtered_lines)

    return filtered_text

filename = "/Users/linaliu/code/Booklist/2024/101Defenses_english.adoc"
# Step 2: Read all text from the file into a string
with open(filename, 'r') as file:
    text = file.read()

# Step 3: Rearrange the text
rearranged_text = rearrange_text(text)

# Print the rearranged text
print(rearranged_text)
