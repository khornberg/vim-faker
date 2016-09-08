" --------------------------------
" Add our plugin to the path
" --------------------------------
python import sys
python import vim
python sys.path.append(vim.eval('expand("<sfile>:h")'))

" --------------------------------
"  Function(s)
" --------------------------------
function! Faker()
python << endOfPython

from vim_faker import vim_faker

current_word = vim.eval('expand("<cword>")')
result = vim_faker(current_word)
vim.command("normal BcW%s" % result)

endOfPython
endfunction

" --------------------------------
"  Expose our commands to the user
" --------------------------------
command! faker call Faker()
