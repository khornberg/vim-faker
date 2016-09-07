" --------------------------------
" Add our plugin to the path
" --------------------------------
python import sys
python import vim
python sys.path.append(vim.eval('expand("<sfile>:h")'))

" --------------------------------
"  Function(s)
" --------------------------------
function! Faker(provider, ...)
python << endOfPython

from vim_faker import vim_faker

    print(vim_faker(provider))

endOfPython
endfunction

" --------------------------------
"  Expose our commands to the user
" --------------------------------
command! faker call Faker()
