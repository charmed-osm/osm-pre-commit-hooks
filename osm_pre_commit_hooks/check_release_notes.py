#!/usr/bin/python3

import argparse
from typing import Optional
from typing import Sequence


def find_release_notes(
    filenames: Sequence[str],
    release_notes_path: str,
) -> int:
    release_notes = [f for f in filenames if f.startswith(release_notes_path)]
   
    retv = 0 
    if not release_notes:
        print("No release note found for this commit.")
        retv = 1
    elif len(release_notes) > 1:
        print("Too many release notes. There should be only 1 per commit.")
        retv = 1
        
    return retv
    

def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'filenames', nargs='*',
        help='Filenames pre-commit believes are changed.',
    )
    parser.add_argument(
        '--release-notes-path', type=str, default='releasenotes/notes',
        help='Path for where the release notes are stored',
    )
    args = parser.parse_args(argv)

    return find_release_notes(
        args.filenames,
        args.release_notes_path,
    )


if __name__ == '__main__':
    exit(main())
