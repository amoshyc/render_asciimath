import os
from docutils import nodes
from docutils.parsers.rst import Directive, directives, roles
from pelican import signals, generators

fmt_line = '<div class="asciimath-line">`{}`</div>'
fmt_block = '<div class="asciimath-block">{}</div>'
fmt_inline = '<span class="asciimath-inline">`{}`</span>'
mathjax_script = '''
<script type='text/javascript'>
    // script
    var script = document.createElement("script");
    script.type = "text/javascript";
    script.src =
     "https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=AM_HTMLorMML";
    document.getElementsByTagName("head")[0].appendChild(script);

    // style
    var style = document.createElement('style');
    style.type = 'text/css';
    style.innerHTML = "{}";
    document.getElementsByTagName('head')[0].appendChild(style);
</script>
'''

def asciimath_role(role, rawtext, text, lineno, inliner, options={}, content=[]):
    result = fmt_inline.format(text)
    return [nodes.raw('', result, format='html')], []

class AsciiMath(Directive):
    required_arguments = 0
    optional_arguments = 0
    has_content = True

    def process_line(self, text):
        # leading space
        idx = 0 # find the index of first char that is not space
        while idx < len(text) and text[idx] == ' ':
            idx += 1
        text = '\ ' * (idx + 1) + text[idx:]

        return fmt_line.format(text)

    def run(self):
        quoted = map(self.process_line, self.content)
        result = fmt_block.format('<br>'.join(quoted))
        return [nodes.raw('', result, format='html')]

def add_asciimath_support(generator):
    cur_dir = os.path.dirname(os.path.realpath(__file__))
    css_path = cur_dir + '/asciimath.css'
    try:
        with open(css_path) as f:
            style = f.read().replace('\n', '') # make the style one line
    except:
        print('Unable to find {}'.format(css_path))
        style = ''

    for article in generator.articles:
        if not article.source_path.endswith('.rst'):
            continue
        if not 'class="asciimath-' in article._content:
            continue

        article._content += mathjax_script.format(style)

def register():
    roles.register_local_role('am', asciimath_role)
    roles.register_local_role('asciimath', asciimath_role)
    directives.register_directive('am', AsciiMath)
    directives.register_directive('asciimath', AsciiMath)
    signals.article_generator_finalized.connect(add_asciimath_support)
