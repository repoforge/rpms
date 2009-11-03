# $Id: texmaker.spec 219 2004-04-09 06:21:45Z dag $
# Authority: dag
# Upstream: Pascal Brachet <pbrachet$xm1math,net>

%{?dtag: %{expand: %%define %dtag 1}}

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}
%{?rh6:%define _without_freedesktop 1}

Summary: LaTeX editor
Name: texmaker
Version: 1.0.1
Release: 1%{?dist}
License: GPL
Group: Applications/Publishing
URL: http://www.xm1math.net/texmaker/

Source: http://www.xm1math.net/texmaker/texmaker_%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: qt-devel >= 3.0, kdelibs-devel
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}

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

%{__cat} <<EOF >texmaker.desktop
[Desktop Entry]
Name=Texmaker TeX Editor
Comment=Create and edit LaTeX documents
Exec=texmaker
Icon=texmaker.png
MimeType=text/x-tex
Terminal=false
Type=Application
Encoding=UTF-8
Categories=Application;Office;WordProcessor;
EOF

%build
source "%{_sysconfdir}/profile.d/qt.sh"
$QTDIR/bin/qmake -makefile -unix "LIBS +=-lm $QTDIR/lib/libqt-mt.so.3" texmaker.pro

%{__make} %{?_smp_mflags} \
	CXXFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 texmaker %{buildroot}%{_bindir}/texmaker
%{__install} -Dp -m0644 texmaker16x16.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/texmaker.png
%{__install} -Dp -m0644 texmaker32x32.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/texmaker.png
%{__install} -Dp -m0644 texmaker48x48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/texmaker.png
%{__install} -Dp -m0644 texmaker48x48.png %{buildroot}%{_datadir}/pixmaps/texmaker.png

%if %{?_without_freedesktop:1}0
	%{__install} -Dp -m0644 texmaker.desktop %{buildroot}%{_datadir}/applications/texmaker.desktop
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor kde                  \
		--add-category X-Red-Hat-Base              \
		--dir %{buildroot}%{_datadir}/applications \
		texmaker.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING latexhelp.html usermanual.html
%{_bindir}/*
%{?_without_freedesktop:%{_datadir}/applications/texmaker.desktop}
%{!?_without_freedesktop:%{_datadir}/applications/kde-texmaker.desktop}
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/pixmaps/*.png

%changelog
* Sun Jul 11 2004 Dag Wieers <dag@weers.com> - 1.0.1-1
- Improved desktop-file.

* Sat Sep 20 2003 Dag Wieers <dag@weers.com> - 1.0.1-0
- Initial package. (using DAR)
