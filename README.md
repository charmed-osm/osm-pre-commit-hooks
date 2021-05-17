osm-pre-commit-hooks
====================

Pre-commit hooks for OSM.

See also: https://github.com/pre-commit/pre-commit
See also: https://osm.etsi.org

### Using osm-pre-commit-hooks with pre-commit

Add this to your `.pre-commit-config.yaml`

```yaml
  - repo: https://github.com/charmed-osm/osm-pre-commit-hooks
    rev: v0.1.0  # Use the ref you want to point at
    hooks:
      - id: trailing-whitespace
    # -   id: ...
```

### Hooks available

#### `check-release-notes`
Check if there is a release notes file.
  - Limits checked files to those indicated as staged for addition by git.
  - `--release-notes-path` - Path where the release notes are located.

#### `install-commit-msg`
Manual hook to install commit-msg.
  - Should be run on the first time that the repository is cloned.
  - `--commit-msg-url` - URL to the commit-msg script.

#### `tox-black`
Run tox -e black.

#### `tox-cover`
Run tox -e black.

#### `tox-flake8`
Run tox -e flake8.

#### `tox-pylint`
Run tox -e pylint.

#### `tox-safety`
Run tox -e safety.

### As a standalone package

If you'd like to use these hooks, they're also available as a standalone package.

Simply `pip install osm-pre-commit-hooks`
