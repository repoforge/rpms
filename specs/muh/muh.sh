#!/bin/sh

if [ ! "$1" ]; then
	if [ ! -d "$HOME/.muh" ]; then
		echo "Creating $HOME/.muh directory." >&2
		cp -r %{_datadir}/muh/ $HOME/.muh/
		echo "Please configure $HOME/.muh/ before starting muh."
else
	%{_bindir}/muh.bin $@
fi
