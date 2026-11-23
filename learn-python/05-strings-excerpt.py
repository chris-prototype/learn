print('****************************************************************************************************')
print('strings-excerpt')
print('****************************************************************************************************')


import textwrap


input_text = textwrap.dedent(
"""
    Summary of changes:
    - Updated auth middleware

    [STUB] Skipping external webhook
    - Added unit tests for token expiry
    - 4 empty lines below




""")

# taken from mvf
def _excerpt(text: str, max_lines: int = 30) -> str:
    # original input
    print('INPUT: \n\n', input_text)

    # strip
    stripped = text.strip()
    print('STRIPPED: \n\n', stripped)

    # create a list
    lines = stripped.splitlines()
    print('LINES: \n\n', lines)

    # remove stubs and ...
    meaningful = [l for l in lines if l.strip() and not l.startswith("[STUB]")]
    if len(meaningful) <= max_lines:
        return "\n".join(meaningful)
    test = "\n".join(meaningful[:max_lines]) + f"\n\n_(truncated — {len(meaningful)} lines total)_"
    return test 


output_text = _excerpt(input_text)
print('OUTPUT: \n\n', output_text)