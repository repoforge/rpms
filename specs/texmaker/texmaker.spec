# $Id$
# Authority: dag
# Upstream: Pascal Brachet <pbrachet$xm1math,net>

%define desktop_vendor rpmforge

Summary: LaTeX editor
Name: texmaker
Version: 1.9
Release: 2%{?dist}
License: GPL
Group: Applications/Publishing
URL: http://www.xm1math.net/texmaker/

Source: http://www.xm1math.net/texmaker/texmaker-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: qt4-devel, gcc-c++
BuildRequires: desktop-file-utils

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
%setup

%{__perl} -pi.orig -e 's|PREFIX"|"%{_prefix}|' *.cpp

%{__cat} <<EOF >texmaker.desktop
[Desktop Entry]
Name=Texmaker TeX Editor
Comment=Create and edit LaTeX documents
Exec=texmaker
MimeType=text/x-tex
Icon=texmaker.png
Terminal=false
Type=Application
Encoding=UTF-8
Categories=Application;Office;WordProcessor;
EOF

%build
export PATH="%{_libdir}/qt4/bin:$PATH"

qmake -unix texmaker.pro

%{__make} %{?_smp_mflags}

%install

#%{__make} install DESTDIR="%{buildroot}"

%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 texmaker %{buildroot}%{_bindir}/texmaker
%{__install} -Dp -m0644 utilities/texmaker16x16.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/texmaker.png
%{__install} -Dp -m0644 utilities/texmaker32x32.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/texmaker.png
%{__install} -Dp -m0644 utilities/texmaker48x48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/texmaker.png
%{__install} -Dp -m0644 utilities/texmaker48x48.png %{buildroot}%{_datadir}/pixmaps/texmaker.png

%{__install} -d -m0755 %{buildroot}%{_datadir}/texmaker/
%{__install} -p -m0644 utilities/*.{css,gif,html,png} %{buildroot}%{_datadir}/texmaker/

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
    desktop-file-install --vendor %{desktop_vendor}    \
        --add-category X-Red-Hat-Base              \
        --dir %{buildroot}%{_datadir}/applications \
        texmaker.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc INSTALL utilities/AUTHORS utilities/COPYING
%{_bindir}/texmaker
%{_datadir}/applications/%{desktop_vendor}-texmaker.desktop
%{_datadir}/icons/hicolor/*/apps/texmaker.png
%{_datadir}/pixmaps/texmaker.png
%{_datadir}/texmaker/

%changelog
* Fri Nov 13 2009 Yury V. Zaytsev - 1.9-2
- Salvaged uncommitted SPEC from build logs.
- Updated SPEC file with small fixes here and there.

* Thu May 21 2009 Dag Wieers <dag@wieers.com> - 1.9-1 - 5993+/dag
- Updated to release 1.9.

* Sun Apr 27 2008 Dag Wieers <dag@wieers.com> - 1.7-1
- Updated to release 1.7.

* Thu Jun 21 2007 Dag Wieers <dag@weers.com> - 1.6-1
- Updated to release 1.6.

* Wed Aug 02 2006 Dag Wieers <dag@weers.com> - 1.4-1
- Updated to release 1.4.

* Sat Jul 23 2005 Dag Wieers <dag@weers.com> - 1.2.1-1
- Updated to release 1.2.1.

* Mon Jul 11 2005 Dag Wieers <dag@weers.com> - 1.2-1
- Updated to release 1.2.

* Sat Apr 30 2005 Dag Wieers <dag@weers.com> - 1.12-1
- Updated to release 1.12.

* Wed Jan 26 2005 Dag Wieers <dag@weers.com> - 1.11-2
- Fixed location of the documentation. (Richard Heck)

* Sun Aug 15 2004 Dag Wieers <dag@weers.com> - 1.11-1
- Updated to release 1.11.

* Sun Jul 11 2004 Dag Wieers <dag@weers.com> - 1.1-1
- Updated to release 1.1.

* Sat Sep 20 2003 Dag Wieers <dag@weers.com> - 1.0.1-0
- Initial package. (using DAR)
