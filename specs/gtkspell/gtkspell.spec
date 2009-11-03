# $Id$
# Authority: matthias

# ExclusiveDist: el2 rh7 rh9 el3 fc1 fc2 fc3

Summary: Gtk2 spell checker interface library
Name: gtkspell
Version: 2.0.9
Release: 1%{?dist}
License: GPL
Group: System Environment/Libraries
URL: http://gtkspell.sourceforge.net/

Source: http://gtkspell.sf.net/download/gtkspell-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk2-devel, pspell-devel, libtool, gettext, gcc-c++

%description
GtkSpell provides MSWord/MacOSX-style highlighting of misspelled words
in a GtkTextView widget. Right-clicking a misspelled word pops up a
menu of suggested replacements.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}, pkgconfig

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
touch docs/html/index.sgml
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_libdir}/libgtkspell.so.*

%files devel
%defattr(-, root, root, 0755)
%doc %{_datadir}/gtk-doc/html/gtkspell/
%{_includedir}/gtkspell-2.0/
%{_libdir}/libgtkspell.a
%exclude %{_libdir}/libgtkspell.la
%{_libdir}/libgtkspell.so
%{_libdir}/pkgconfig/gtkspell-2.0.pc

%changelog
* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 2.0.9-1
- Updated to release 2.0.9.

* Mon Jul 19 2004 Dag Wieers <dag@wieers.com> - 2.0.6-1
- Updated to release 2.0.6.

* Fri Feb 28 2003 Dag Wieers <dag@wieers.com> - 2.0.4-0
- Initial package. (using DAR)
