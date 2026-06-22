from fnmatch import fnmatch

def should_ignore(
    path_str,
    ignore_patterns
):
    return any(
        fnmatch(path_str, pattern)
        for pattern in ignore_patterns
    )