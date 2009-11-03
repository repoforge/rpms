# $Id$
# Authority: dries
# Upstream: Stelios Xanthakis <sxanth$ceid,upatras,gr>

Summary: C source code analyzer
Name: ncc
Version: 2.7
Release: 1%{?dist}
License: Artistic
Group: Development/Languages
URL: http://students.ceid.upatras.gr/~sxanth/ncc/index.html

Source: http://students.ceid.upatras.gr/~sxanth/ncc/ncc-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, ncurses-devel

%description
ncc is a C source code analyzer which generates program flow and variable
usage information. Using it should be as easy as changing CC=gcc to CC=ncc
in makefiles, and effort has been made to support most common gcc
extensions. ncc has been tested with the sources of the Linux kernel, gtk,
gcc, gdb, bind, mpg123, ncftp, and many other famous projects.

%prep
%setup
# fix install
%{__perl} -pi -e "s|ln (.*) ..BINDIR..(.*) ..BINDIR./(.*)|ln \$1 %{_bindir}/\$2 %{buildroot}%{_bindir}/\$3|g;" Makefile
#%{__perl} -pi -e "s|cp (.*) /usr/bin/(.*)|cp \$1 %{buildroot}%{_bindir}/\$2|g;" Makefile
#%{__perl} -pi -e "s|cp (.*) /usr/share/man/(.*)|cp \$1 %{buildroot}%{_mandir}/man1/|g;" Makefile
%{__perl} -pi -e "s|cp doc/nognu|#|g;" Makefile

%build
%{__make} %{?_smp_mflags} LCFLAGS=-fpermissive

%install
%{__rm} -rf %{buildroot}
%{__install} -d %{buildroot}%{_bindir} %{buildroot}%{_mandir}/man1
%makeinstall DESTDIR=%{buildroot}%{_prefix}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc doc/*
%doc %{_mandir}/man?/ncc*
%{_bindir}/ncc
%{_bindir}/nccar
%{_bindir}/nccc++
%{_bindir}/nccg++
%{_bindir}/nccld
%{_bindir}/nccnav
%{_bindir}/nccnavi

%changelog
* Mon Sep  3 2007 Dries Verachtert <dries@ulyssis.org> - 2.7-1
- Updated to release 2.7.

* Tue Jan 09 2007 Dries Verachtert <dries@ulyssis.org> - 2.6-1
- Updated to release 2.6.

* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 2.5-1
- Updated to release 2.5.

* Tue Aug 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.4-1
- Updated to release 2.4.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.3-1.2
- Rebuild for Fedora Core 5.

* Sun Jan 29 2006 Dries Verachtert <dries@ulyssis.org> - 2.3-1
- Updated to release 2.3.

* Tue Sep 13 2005 Dries Verachtert <dries@ulyssis.org> - 2.2-1
- Initial package.
