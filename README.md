# SimpleAdd

Sublime text plugin for computing the sum of numerical terms in a region of
selected text.  Basic heuristics are used to detect the numeric terms.

This plugin makes it convenient to quickly compute the sum of a list of
numbers delimited by commas or whitespace characters, and possibly
intertwined with general alphanumeric text.

### Usage

First highlight the regions of text, then hit `alt+shift+a` or
`ctrl+shift+p` -> "Simple Add".  The sum of numeric terms will be shown the
status bar.

### Default Shortcuts

- __Simple Add__: `alt+shift+a`

### Installation

Using [Package Control](https://packagecontrol.io/packages/SimpleAdd),
type `ctrl+shift+p` > "Package Control: Install Package" > "SimpleAdd".

Alternatively, clone this repository as follows:

    $ git clone https://github.com/fsaad/Sublime-SimpleAdd ~/.config/sublime-text-3/Packages/SimpleAdd
