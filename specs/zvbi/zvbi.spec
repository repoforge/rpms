# $Id$

Summary: Raw VBI, Teletext and Closed Caption decoding library
Name: zvbi
Version: 0.2.5
Release: 1.fr
License: GPL
Group: Applications/Multimedia
URL: http://zapping.sourceforge.net/
Source: http://dl.sf.net/zapping/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++, doxygen, gettext

%description
This library provides routines to access raw vbi sampling devices
(currently the V4L and V4L2 API are supported), a versatile raw vbi
bit slicer, decoders for various data services and basic search,
render and export functions for text pages. The library is the
vbi decoding backbone of the Zapping Gnome TV viewer and Zapzilla
Teletext browser. Documentation included.


%package devel
Summary: Static libraries and header files for zvbi development
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
The static libraries and header files needed for building programs that use
the zvbi library.


%prep
%setup -q

%build
%configure --disable-gtk-doc
make

%install
rm -rf %{buildroot}
%makeinstall
%find_lang %{name}

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr (-, root, root)
%doc AUTHORS BUGS COPYING ChangeLog NEWS README TODO doc/html
%{_libdir}/*.so.*

%files devel
%defattr (-, root, root)
%{_includedir}/*
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so

%changelog
* Tue Nov 11 2003 Matthias Saou <http://freshrpms.net/> 0.2.5-1.fr
- Update to 0.2.5.
- Rebuild for Fedora Core 1.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Thu Mar 20 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.2.4.
- Exclude .la file.

* Wed Oct  9 2002 Michael H. Schimek <mschimek@users.sourceforge.net>
- Update to 0.2.2.

* Tue Aug  6 2002 Michael H. Schimek <mschimek@users.sourceforge.net>
- Added %%find_lang for locale support.
- Split with a devel package.
- Disabled gtk-doc since detection works but not build if not in /usr/local.

* Tue Jun  4 2002 Michael H. Schimek <mschimek@users.sourceforge.net>
- Removed libunicode requirement
- Made package relocatable

* Sat Jan 26 2002 Michael H. Schimek <mschimek@users.sourceforge.net>
- Created

