# Authority: freshrpms
Summary: Gtk2 spell checker interface library.
Name: gtkspell
Version: 2.0.4
Release: 0
License: GPL
Group: System Environment/Libraries
URL: http://gtkspell.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://gtkspell.sourceforge.net/download/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: gtk2-devel, pspell-devel, libtool

%description
GtkSpell provides MSWord/MacOSX-style highlighting of misspelled words
in a GtkTextView widget. Right-clicking a misspelled word pops up a
menu of suggested replacements.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
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
#	--disable-gtk-doc
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
touch docs/html/index.sgml
%makeinstall

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/*.la

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc %{_datadir}/gtk-doc/html/gtkspell/
%{_includedir}/gtkspell-2.0/
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
#exclude %{_libdir}/*.la

%changelog
* Fri Feb 28 2003 Dag Wieers <dag@wieers.com> - 2.0.4-0
- Initial package. (using DAR)
