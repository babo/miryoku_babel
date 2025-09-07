#!/bin/sh
rm -rf tangled
emacs --batch -Q -L org-mode/lisp -f package-initialize -eval '(setq org-babel-python-command "python3")'  -eval "(require 'ob-python)" -eval "(setq org-confirm-babel-evaluate nil)" -eval "(setq python-indent-guess-indent-offset-verbose nil)" ./readme.org -f org-babel-tangle
