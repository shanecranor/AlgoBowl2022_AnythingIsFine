import importlib
from importlib.resources import path
from multiprocessing.spawn import import_main_path
import os
from pydoc import importfile
import difflib
import sys




def verify_generated_code():
    generated_code = generated_code().splitlines(True)

    with open(os.path.join( path, "__init__.py"), "r") as fh:
        actual = fh.readlines()

        diff = list(
            difflib.unified_diff(
                actual, generated_code, fromfile="current", tofile="updated"
            )
        )
        if diff:
            print("Generated code is NOT up-to-date!", file=sys.stderr)
            print(15 * "*", file=sys.stderr)
            print("".join(diff), file=sys.stderr)
            print(15 * "*", file=sys.stderr)
            print("Re-run with generate to update code.", file=sys.stderr)
            return 1

    print("Generated code is up-to-date!")

    return 0 
