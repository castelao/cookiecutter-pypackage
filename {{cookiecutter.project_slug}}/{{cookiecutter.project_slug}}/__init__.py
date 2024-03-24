"""Top-level package for {{ cookiecutter.project_name }}."""

__author__ = """{{ cookiecutter.full_name }}"""
__email__ = '{{ cookiecutter.email }}'

from pkg_resources import get_distribution, DistributionNotFound

try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:  # pragma: no cover
    try:
        from ._version import version as __version__  # noqa
    except ImportError:  # pragma: no cover
        raise ImportError(
            "Failed to find (autogenerated) version.py. "
            "This might be because you are installing from GitHub's tarballs, "
            "use the PyPI ones."
        )
