# $Id$

# Authority: dag

### FIXME: Makefiles don't allow -jX (parallel compilation) (Please fix upstream)
# Distcc: 0

%define dfi %(which desktop-file-install &>/dev/null; echo $?)

Summary: A LaTeX editor.
Name: texmaker
Version: 1.0.1
Release: 0
License: GPL
Group: Applications/Publishing
URL: http://perso.club-internet.fr/pascal.brachet/texmaker/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://perso.club-internet.fr/pascal.brachet/texmaker/%{name}_%{version}.tar.bz2
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: qt-devel >= 3.0, kdelibs-devel

%description
Texmaker is a program, that integrates many tools needed 
to develop documents with LaTeX, in just one application. 

It have thoses features:
- an editor to write your LaTeX source files 
  (syntax highlighting, undo-redo, search-replace, ...)
- the principal LaTex tags can be inserted directly with the "LaTeX", 
  "Math" and "Greek" menus 
- 370 mathematical symbols can be inserted in just one click 
- wizards to generate code ('Quick document', 'Quick letter', tabular,
  tabbing and array environments) 
- LaTeX-related programs can be launched via the "Tools" menu 
- the standard Bibtex entry types can be inserted in the ".bib" file
  with the "Bibliography" menu 
- a "structure view" of the document for easier navigation of a document 
  (by clicking on an item in the "Structure" frame, you can jump directly 
  to the corresponding part of your document 
- extensive LaTeX documentation 
- in the "Messages / Log File" frame, you can see information about processes 
  and the logfile after a LaTeX compilation 
- the "Next Latex Error" and "Previous Latex Error" commands let you reach the
  LaTeX errors detected by Kile in the log file 
- by clicking on the number of a line in the log file, the cursor jumps to the 
  corresponding line in the editor 

%prep
%setup -n %{name}_%{version}

%build
#export LD_LIBRARY_PATH="/usr/lix/qt3/lib:$LD_LIBRARY_PATH"
#export PATH="/usr/lib/qt3/bin:$PATH"
export QTDIR="/usr/lib/qt3"
$QTDIR/bin/qmake -makefile -unix "LIBS +=-lm $QTDIR/lib/libqt-mt.so.3" texmaker.pro

%{__make} %{?_smp_flags} \
	CFLAGS="%{optflags}" \
	CXXFLAGS="%{optflags}"


%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir} \
			%{buildroot}%{_datadir}/applications/ \
			%{buildroot}%{_datadir}/icons/hicolor/{16x16,32x32,48x48}/apps/ \
			%{buildroot}%{_datadir}/pixmaps/
%{__install} -m0755 texmaker %{buildroot}%{_bindir}
%{__install} -m0644 texmaker16x16.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/texmaker.png
%{__install} -m0644 texmaker32x32.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/texmaker.png
%{__install} -m0644 texmaker48x48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/texmaker.png
%{__install} -m0644 texmaker48x48.png %{buildroot}%{_datadir}/pixmaps/texmaker.png

%if %{dfi}
        %{__install} -m0644 %{name}.desktop %{buildroot}%{_datadir}/applications/
%else
	desktop-file-install --vendor net                  \
	        --add-category X-Red-Hat-Base              \
	        --dir %{buildroot}%{_datadir}/applications \
	        %{name}.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING latexhelp.html usermanual.html
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/pixmaps/*.png

%changelog
* Sat Sep 20 2003 Dag Wieers <dag@weers.com> - 1.0.1-0
- Initial package. (using DAR)
