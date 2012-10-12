# pyjade-coffin

Jade and Jinja2 template support for Django using
[PyJade](https://github.com/SyrusAkbary/pyjade)'s Jinja2 extension w/
[coffin](https://github.com/coffin/coffin)

pyjade-coffin was created because I wanted Jade mixin support in my django
project (which isn't supported in PyJade's django template loaders) and
relative path includes (which requires changes to coffin's core components).

## What this package does:

- Registers PyJade's Jinja2 extension with coffin so `.jade` files are rendered
  though Jinja2 which gives us mixin support.

- Add relative path include support by subclassing `coffinEnvironment` and 
  overriding the `join_path` method. This matches jade's native JavaScript
  engine's behavior.

- Sets Jinja2's autoescape to `false` which allows HTML escaping to be handled
  in Jade templates.

## Installation

- TODO

## Using It

- TODO
