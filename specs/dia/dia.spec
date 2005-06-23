# $Id$
# Authority: dag

##ExcludeDist: rh9 fc1 fc2
# ExcludeDist: el4

Summary: Diagram drawing program
Name: dia
Version: 0.94
Release: 1
epoch: 1
License: GPL
Group: Applications/Multimedia
URL: http://www.gnome.org/projects/dia/

Source: http://ftp.gnome.org/pub/gnome/sources/dia/%{version}/dia-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: glib2-devel >= 2.0.6, gtk2-devel >= 2.0.6, libxml2-devel >= 2.3.9
BuildRequires: libgnome-devel >= 2.0, libgnomeui-devel >= 2.0, pango-devel >= 1.1.5
BuildRequires: libart_lgpl-devel >= 2.3.10, libxslt-devel, libpng-devel
BuildRequires: python-devel >= 2.2.1, pygtk2-devel, gcc-c++

%description
The Dia drawing program is designed to be like the Microsoft(R) Visio
program. Dia can be used to draw different types of diagrams, and
includes support for UML static structure diagrams (class diagrams),
entity relationship modeling, and network diagrams. Dia can load and
save diagrams to a custom file format, can load and save in .xml
format, and can export to PostScript(TM).

%prep
%setup

### FIXME: Create proper desktop file
#%{__cat} <<EOF >dia.desktop
#[desktop]
#Name=Dia Diagrams
#Comment=Create diagrams
#EOF

%build
#{__aclocal}
#./autogen.sh
%configure \
	--enable-gnome \
	--with-python
#	--enable-maintainer-mode
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}
#%{__mv} %{buildroot}%{_bindir}/dia %{buildroot}%{_bindir}/dia-bin
#%{__install} -Dp -m0755 dia.sh %{buildroot}%{_bindir}/dia

### Clean up buildroot
#{__rm} -f %{buildroot}%{_libdir}/dia/*.la

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING KNOWN_BUGS NEWS README TODO doc/
%doc %{_datadir}/gnome/help/dia/
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_libdir}/dia/
%{_datadir}/applications/*.desktop
%{_datadir}/dia/
%{_datadir}/mime-info/*
%{_datadir}/pixmaps/*
%exclude %{_localstatedir}/scrollkeeper/

%changelog
* Wed Aug 25 2004 Dag Wieers <dag@wieers.com> - 0.94-1.
- Updated to release 0.94.

* Wed May 05 2004 Dag Wieers <dag@wieers.com> - 0.93-1.
- Updated to release 0.93.

* Sun Nov 09 2003 Dag Wieers <dag@wieers.com> - 0.92.2-1
- Fixed the "Couldn't find standard objects..." error. (Krzysztof Leszczynski)

* Sat Nov 01 2003 Dag Wieers <dag@wieers.com> - 0.92.2-0
- Updated to release 0.92.2.

* Sun Oct 26 2003 Dag Wieers <dag@wieers.com> - 0.92.1-0
- Updated to release 0.92.1.

* Mon Oct 20 2003 Dag Wieers <dag@wieers.com> - 0.92-0
- Updated to release 0.92.

* Wed Sep 24 2003 Dag Wieers <dag@wieers.com> - 0.92-0-pre3
- Updated to release 0.92-pre3.

* Tue May 06 2003 Dag Wieers <dag@wieers.com> - 0.91-0
- Updated to release 0.91.

* Thu Jan 3 2003 Dag Wieers <dag@wieers.com> - 0.90.20030131-0
- Initial package. (using DAR)
