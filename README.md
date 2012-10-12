# PyJadeCoffin

Jade and Jinja2 template support for Django using
[PyJade](https://github.com/SyrusAkbary/pyjade)'s Jinja2 extension w/
[Coffin](https://github.com/coffin/coffin)

PyJadeCoffin was created because I wanted Jade mixin support in my django
project (which isn't supported in PyJade's django template loaders) and
relative path includes (which requires changes to Coffin's core components).

This package does the following:

- Registers PyJade's Jinja2 extension with Coffin so `.jade` files are rendered
  w/ mixin support.

- Subclasses `CoffinEnvironment` with custom `join_path` method to add relative
  path includes. This matches JS Jade behavior.

- Sets Jinja2's autoescape to `false` which allows HTML escaping to be handled
  in Jade templates.
