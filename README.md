# vim-faker

## Installation

Use your plugin manager of choice.

- [Pathogen](https://github.com/tpope/vim-pathogen)
  - `git clone https://github.com/khornberg/vim-faker ~/.vim/bundle/vim-faker`
- [Vundle](https://github.com/gmarik/vundle)
  - Add `Bundle 'https://github.com/khornberg/vim-faker'` to .vimrc
  - Run `:BundleInstall`
- [NeoBundle](https://github.com/Shougo/neobundle.vim)
  - Add `NeoBundle 'https://github.com/khornberg/vim-faker'` to .vimrc
  - Run `:NeoBundleInstall`
- [vim-plug](https://github.com/junegunn/vim-plug)
  - Add `Plug 'https://github.com/khornberg/vim-faker'` to .vimrc
  - Run `:PlugInstall`

## Requirements

[`faker`](https://github.com/joke2k/faker)

Install with `pip install faker`

## Usage

In a buffer add the provider and call `Faker`

[Providers](https://faker.readthedocs.io/en/latest/providers.html)

### Example

Your buffer looks like
```
My name is name
```

While your cursor is over the second `name` call `:Faker`

### Example Keybinding

`noremap <leader>k :call Faker()<cr>`

## Todo

Support localization and kwargs for providers.
