print('****************************************************************************************************')
print('strings-dedent')
print('****************************************************************************************************')


import textwrap


input_text = textwrap.dedent(
"""
    Summary of changes:
    - Updated auth middleware

    [STUB] Skipping external webhook
    - Added unit tests for token expiry
    - Verified CI pipeline passes
""")
print('Input: ', input_text)

# taken from mvf
def _excerpt(text: str, max_lines: int = 30) -> str:
  lines = text.strip().splitlines()
  print('Lines: \n', lines)
  meaningful = [l for l in lines if l.strip() and not l.startswith("[STUB]")]
  if len(meaningful) <= max_lines:
      return "\n".join(meaningful)
  test = "\n".join(meaningful[:max_lines]) + f"\n\n_(truncated — {len(meaningful)} lines total)_"
  return test 


output_text = _excerpt(input_text)
print('Output: \n', output_text)