# mkdocs-replace-plugin

This is a plugin for [MkDocs](https://www.mkdocs.org).
This was written to aid the documentation of [Makeroid](https://www.makeroid.io)
This plugin was primarily designed to be used with the markdown-include plugin.

The `markdown-include` plugin provides a way to "embed" the contents of one file in another markdown file.
This allows in reusing the repeating portions of the documentation, instead of rewriting them everywhere.


## Example Use-case

Let us say we have three files : `car.md`, bus.md, `bicycle.md`
There is also a `wheels.md` file with the following content:
```
A {{ meta.vehicle }} has {{ meta.no_of_wheels }} wheels
```

This `wheels.md` file is included using the syntax for `markdown-include` in files containing the appropriate meta data as required.
Then, using this plugin, the meta data automatically replaces `{{ meta.vehicle }}`

## Installing this plugin

1. Install this plugin
`pip install git+https://github.com/SivagiriVisakan/mkdocs-replace-plugin.git`

2. Include this plugin in `mkdocs.yml` configuration file
```yaml
# mkdocs.yml
plugins:
  - replace
```

## Syntax

The syntax to be used inside the markdown file is `{{ meta.<your meta data name> }}`. Note the spaces near the curly braces.
Example: `{{ meta.vehicle }}`

## Limitations

Currently only strings are supported. Lists in the meta data are not supported.
