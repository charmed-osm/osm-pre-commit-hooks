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

#### `check-builtin-literals`
Require literal syntax when initializing empty or zero Python builtin types.
  - Allows calling constructors with positional arguments (e.g., `list('abc')`).
  - Allows calling constructors from the `builtins` (`__builtin__`) namespace (`builtins.list()`).
  - Ignore this requirement for specific builtin types with `--ignore=type1,type2,…`.
  - Forbid `dict` keyword syntax with `--no-allow-dict-kwargs`.

#### `check-case-conflict`
Check for files with names that would conflict on a case-insensitive filesystem like MacOS HFS+ or Windows FAT.

### As a standalone package

If you'd like to use these hooks, they're also available as a standalone package.

Simply `pip install osm-pre-commit-hooks`
