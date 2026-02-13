
# hatch-django-locales

This package provides a hatchling plugin for Django projects that
automatically compiles locale files when building the package. 

## Usage

In your projects `pyproject.toml`, adjust the following:

```toml
[build-system]
requires = ["hatchling", "uv-dynamic-versioning", "hatch-django-locales>=0.1.4"]
build-backend = "hatchling.build"

[tool.hatch.build.hooks.django-locales]
```