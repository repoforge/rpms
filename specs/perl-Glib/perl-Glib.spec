# $Id$

# Authority: dag

# Upstream: gtk-perl-list@gnome.org

%define rname Glib

Summary: Glib module for perl.
Name: perl-Glib
Version: 1.00
Release: 0
License: LGPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Glib/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/gtk2-perl/%{rname}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: perl >= 0:5.8.0, glib2-devel, perl(ExtUtils::Depends), perl(ExtUtils::PkgConfig)
Requires: perl >= 0:5.8.0, glib2 >= 2.0.6

%description
This module provides perl access to GLib and GLib's GObject libraries.  GLib is
a portability and utility library; GObject provides a generic type system with
inheritance and a powerful signal system.  Together these libraries are used as
the foundation for many of the libraries that make up the Gnome environment,
and are used in many unrelated projects.

%prep
%setup -n %{rname}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL \
	PREFIX="%{buildroot}%{_prefix}" \
	INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags} \
	OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_libdir}/perl5/*/*-linux-thread-multi/
%{__rm} -f %{buildroot}%{_libdir}/perl5/vendor_perl/*/*-linux-thread-multi/auto/*{,/*}/.packlist

%clean 
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST README
%doc %{_mandir}/man?/*
%{_libdir}/perl5/vendor_perl/*/*

%changelog
* Sat Oct 11 2003 Dag Wieers <dag@wieers.com> - 1.00-0
- Updated to release 1.00.

* Sun Sep 07 2003 Dag Wieers <dag@wieers.com> - 0.97-0
- Updated to release 0.97.

* Sat Aug 30 2003 Dag Wieers <dag@wieers.com> - 0.96-0
- Updated to release 0.96.

* Fri Aug 22 2003 Dag Wieers <dag@wieers.com> - 0.95-0
- Updated to release 0.95.

* Sat Aug 16 2003 Dag Wieers <dag@wieers.com> - 0.94-0
- Updated to release 0.94.

* Sat Aug 02 2003 Dag Wieers <dag@wieers.com> - 0.92-0
- Updated to release 0.92.

* Sun Jul 27 2003 Dag Wieers <dag@wieers.com> - 0.91-0
- Updated to release 0.91.

* Sun Jul 20 2003 Dag Wieers <dag@wieers.com> - 0.90-0
- Initial package. (using DAR)
