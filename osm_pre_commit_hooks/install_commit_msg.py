#!/usr/bin/python3

import argparse
import requests
import stat
from pathlib import Path
from typing import Optional
from typing import Sequence


def install_commit_msg(
    commit_msg_url: str,
) -> int:
    commit_msg_path = Path(".") / ".git" / "hooks" / "commit-msg"
    
    if not commit_msg_path.exists():
        print(commit_msg_url)
        response = requests.get(commit_msg_url, allow_redirects=True)
        with open(commit_msg_path, "wb") as f:
            f.write(response.content)
    
    if (commit_msg_path.stat().st_mode & stat.S_IXUSR) == 0:
        print("Reached lack of execute permissions")
        commit_msg_path.chmod(commit_msg_path.stat().st_mode | stat.S_IXUSR)

    return 0


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--commit-msg-url",
        type=str,
        default="http://osm.etsi.org/gerrit/tools/hooks/commit-msg",
        help="Path for where the release notes are stored",
    )
    args = parser.parse_args(argv)

    return install_commit_msg(
        args.commit_msg_url,
    )


if __name__ == '__main__':
    exit(main())
