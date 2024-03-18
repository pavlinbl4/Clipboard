import sys

import pyperclip
import contextlib
from io import StringIO

@contextlib.contextmanager
def clipboard_context():
    saved_stdout = sys.stdout
    output = StringIO()
    try:
        sys.stdout = output
        yield output
    finally:
        sys.stdout = saved_stdout
        pyperclip.copy(output.getvalue())

with clipboard_context() as clip:
    print("This text will be copied to the clipboard.")
    print("You can now paste it elsewhere.")

print("The output has been copied to the clipboard.")