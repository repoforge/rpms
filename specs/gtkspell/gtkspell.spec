# $Id$
# Authority: matthias

Summary: Gtk2 spell checker interface library
Name: gtkspell
Version: 2.0.6
Release: 1
License: GPL
Group: System Environment/Libraries
URL: http://gtkspell.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

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
%makeinstall
%find_lang %{name}

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

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
* Mon Jul 19 2004 Dag Wieers <dag@wieers.com> - 2.0.6-1
- Updated to release 2.0.6.

* Fri Feb 28 2003 Dag Wieers <dag@wieers.com> - 2.0.4-0
- Initial package. (using DAR)
