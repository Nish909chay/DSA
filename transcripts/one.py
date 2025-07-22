import re

def extract_text_only(input_file, output_file):
    with open(input_file, 'r', encoding='utf-16') as f:
        data = f.read()

    # Correct regex for single-quoted 'text' fields, multiline
    texts = re.findall(r"'text':\s*'([^']*)'", data, re.DOTALL)

    with open(output_file, 'w', encoding='utf-8') as f:
        for line in texts:
            f.write(line.replace('\\n', '\n').strip() + '\n')

extract_text_only(
    r'c:\Users\Admin\Desktop\Striver DS\codes\transcripts\os_trans.txt',
    r'c:\Users\Admin\Desktop\Striver DS\codes\transcripts\os_trans_cleaned.txt'
)