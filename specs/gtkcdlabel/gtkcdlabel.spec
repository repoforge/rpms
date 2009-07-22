# $Id$
# Authority: dag

%define desktop_vendor rpmforge

Summary: Utility to generate CD covers with cdlabelgen
Name: gtkcdlabel
Version: 1.14
Release: 1
License: GPL
Group: Applications/Publishing
URL: http://gtkcdlabel.sourceforge.net/

Source: http://dl.sf.net/sourceforge/gtkcdlabel/gtkcdlabel-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: cdlabelgen >= 3.0.0
Requires: pygtk2
Requires: python
Requires: python-id3

%description
gtkcdlabel is a utility to generate CD covers with cdlabelgen.

%prep
%setup -c

%{__mv} -f usr/share/doc/gtkcdlabel/* .

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0644 usr/share/gtkcdlabel/gtkcdlabel.glade %{buildroot}%{_datadir}/gtkcdlabel/gtkcdlabel.glade
%{__install} -Dp -m0644 usr/share/gtkcdlabel/gtkcdlabel.ui %{buildroot}%{_datadir}/gtkcdlabel/gtkcdlabel.ui
%{__install} -Dp -m0644 usr/share/pixmaps/gtkcdlabel.xpm %{buildroot}%{_datadir}/pixmaps/gtkcdlabel.xpm
%{__install} -Dp -m0755 usr/bin/gtkcdlabel.py %{buildroot}%{_bindir}/gtkcdlabel.py

desktop-file-install --vendor="%{desktop_vendor}" \
    --dir %{buildroot}%{_datadir}/applications/ \
    usr/share/applications/gtkcdlabel.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING README
%{_bindir}/gtkcdlabel.py
%{_datadir}/applications/%{desktop_vendor}-gtkcdlabel.desktop
%{_datadir}/gtkcdlabel/
%{_datadir}/pixmaps/gtkcdlabel.xpm
%exclude %{_bindir}/gtkcdlabel.py?

%changelog
* Tue Jul 21 2009 Dag Wieers <dag@wieers.com> - 1.14-1
- Initial package. (using DAR)
