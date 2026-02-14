
# hatch-django-locales

This package provides a hatchling plugin (build hook) for Django projects that
automatically compiles locale files when building the package. 

## Usage

In your projects `pyproject.toml`, make sure you are using the hatchling build system 
and add the following:

```toml
[tool.hatch.build.hooks.django-locales]
dependencies = ["hatch-django-locales>=0.1.5", "django"]
search-directories = ["src"]
```

The ``search-directories`` option should be a list of directories to glob 
for ``locale`` directories and is your project root by default.
Make sure that the ``.mo`` files are actually included in the wheels produced 
by your build process.