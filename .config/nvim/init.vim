set nocompatible               " be improved, required
filetype off                   " required
" set the runtime path to include Vundle and initialize
set rtp+=~/.config/nvim/bundle/Vundle.vim
call vundle#begin()            " required
Plugin 'VundleVim/Vundle.vim'  " required

" ===================
" my plugins here
" ===================

Plugin 'dracula/vim'
Plugin 'itchyny/lightline.vim'
Plugin 'vim-python/python-syntax'
Plugin 'tpope/vim-commentary'
Plugin 'tpope/vim-fugitive'
Plugin 'vim-scripts/AutoComplPop'
Plugin 'nvim-lua/completion-nvim'
Plugin 'Raimondi/delimitMate'
Plugin 'nvim-treesitter/nvim-treesitter'
" ===================
" end of plugins
" ===================
call vundle#end()               " required
filetype plugin indent on       " required

let g:lightline = {
      \ 'colorscheme': 'dracula',
      \ }

set number

let g:python_highlight_all = 1

