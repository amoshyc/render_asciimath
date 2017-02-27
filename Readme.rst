Render AsciiMath
#######################

This is a Pelican_ plugin to render AsciiMath_ . It makes use of Mathjax_ with config ``AM_HTMLorMML`` and the mathjax script is loaded dynamically, just like `render math`_. But unlike `render math`_ , this plugin is very simple as I wrote it for my personal use. Currently, it only supports **articles written in restructuredText**.

.. _Pelican: http://docs.getpelican.com/en/stable/
.. _AsciiMath: http://asciimath.org/
.. _MathJax: https://www.mathjax.org/
.. _render math: https://github.com/getpelican/pelican-plugins/tree/master/render_math

Installation
*************

To enable this plugin, simply add the path of this plugin (an absolute path or a relative path to your ``PLUGIN_PATHS``) to your plugin list in your ``pelicanconf.py``, for example::

    PLUGIN_PATHS = ["plugins"]
    PLUGINS = ["render_asciimath"]

if file structure is something like::

    <project folder>
    ├── content
    ├── develop_server.sh
    ├── fabfile.py
    ├── Makefile
    ├── output
    ├── pelicanconf.py
    ├── plugins
    │   ├── extract_toc
    │   ├── render_asciimath
    │   ├── render_math
    │   └── tag_cloud
    ├── publishconf.py
    └── themes


Usage
************

Inline Markup
==============

Just write it and render your pelican project as usual.

::

    So the solution is :am:`x = (-b +- sqrt(b^2 - 4ac)) / (2a)`.

or::

    So the solution is :asciimath:`x = (-b +- sqrt(b^2 - 4ac)) / (2a)`.

is rendered as

.. image:: https://imgur.com/BOtsJF2.png

If you use a lot of inline AsciiMath in your article and don't want to type the ``:am:`` every time, you can set up the ``default-role`` to AsciiMath. Insert::

    .. default-role:: am

to the begining of your article content. And then you can use::

    So the solution is `x = (-b +- sqrt(b^2 - 4ac)) / (2a)`.

to write inline AsciiMath. Notice that it is wrapped in **single backtick**.

Directive
==============

::

    .. am::

        x = (-b +- sqrt(b^2 - 4ac)) / (2a)
        int_0^1 f(x)dx
        where
            a = 1
            b = 2

or::

    .. asciimath::

        x = (-b +- sqrt(b^2 - 4ac)) / (2a)
        int_0^1 f(x)dx
        where
            a = 1
            b = 2

.. image:: https://imgur.com/hQLR5d3.png

Notice that I add some custom rules.

1. Line breaks is preserved. (converted to ``<br/>``)
2. Leading space is preserved. (converted to ``'\ '`` which is a space in AsciiMath)

Customization
**************

You can modify the ``asciimath.css``. The style is also dynamically added when Pelican compiling the source to html.

1. Each inline asciimath is wrap in a ``.asciimath-inline`` class.

2. Each line in asciimath directive is wrap in a ``.asciimath-line`` class and the directive is wrap in ``.asciimath-block``.

By default, ``asciimath.css`` centeralize the asciimath directive and add some margin between lines in a directive.
