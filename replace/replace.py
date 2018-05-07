import re
import logging
from mkdocs.plugins import BasePlugin

# Regex for detecting text of format: {{ anytext }}
MATCH_REGEX = r"\{\{ (?P<name>.*) \}\}"

# TODO: Allow more general replacements, maybe from a file,
#       Allow using `page` variables


class ReplacePlugin(BasePlugin):
    """ A plugin for MkDocs to replace the meta vars from inside the markdown without
        modifying the template. This is especially useful in when using markdown-include extension,
        where you want certain specific parts of the text to based on the page being rendered.

        Example:
          Let us say you have a file `eat.md` with the following content:
          {{ meta.child_name }} loves eating chocolates.
      
          You include this in another markdown files ,say robert.md, john.md
          using markdown-include extension. These markdown files have their full names in the 
          meta data.

          But name you want won't be included, just plain text as `{{ meta.child_name }}

          Using this plugin, {{ meta.child_name }} is replaced by the meta data available for that
          particular page.
    """

    # This event is chosen as we need the markdown to be parsed for including other markdown file,
    # (if any) using markdown-include
    def on_page_content(self, html, page, config, site_navigation):

        match_iter = re.finditer(MATCH_REGEX, html)

        # TODO: Provide other options than just replacing from page.meta data.

        for match in match_iter:
            name = match.group('name')
            if name.startswith('meta.'):
                try:
                    meta_name = str(name.split('.')[1])
                    required_meta_data = str(page.meta[meta_name])
                    if not required_meta_data or not isinstance(required_meta_data, str):
                        logging.error('Unsupported meta data type. \
                                       Received %s : %s' % (meta_name, required_meta_data))
                        continue
                    html = html.replace(('{{ meta.%s }}' % meta_name), required_meta_data)

                except KeyError:
                    logging.error('Meta data not found: %s' % (meta_name))

        return html
