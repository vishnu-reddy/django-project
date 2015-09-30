__version__ = '1.0.0'
__version_info__ = tuple(
    map(
        lambda x: int(x) if x.isdigit() else x,
        __version__.replace('-', '.', 1).split('.')
    )
)
