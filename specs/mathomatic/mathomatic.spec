# $Id: $

# Authority: dries
# Upstream: George J. Gesslein

Summary: Small, portable symbolic math program
Name: mathomatic
Version: 11.2c
Release: 1
License: LGPL
Group: Applications/Engineering
URL: http://www.lightlink.com/computer/math/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://www.panix.com/~gesslein/mathomatic-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
Mathomatic is a small, portable symbolic math program that can automatically
solve, simplify, differentiate, combine, and compare algebraic equations,
perform polynomial and complex arithmetic, etc. It was written by George
Gesslein II and has been under development since 1986.

%prep
%setup -n am

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m 755 %{buildroot}%{_bindir} \
	%{buildroot}%{_mandir}/man1
%{__sed} -i "s/.PREFIX.\/bin/\(bindir\)/g;" makefile
%{__sed} -i "s/.PREFIX.\/man/\(mandir\)/g;" makefile
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc *.txt *.htm
%{_bindir}/*
%{_datadir}/man/man1/am.*

%changelog
* Fri Jun 25 2004 Dries Verachtert <dries@ulyssis.org> 11.2c-1
- Update to 11.2c

* Fri Jun 11 2004 Dries Verachtert <dries@ulyssis.org> 11.2b-1
- Update to 11.2b

* Sat May 29 2004 Dries Verachtert <dries@ulyssis.org> 11.1d-1
- Update to 11.1d

* Tue Apr 27 2004 Dries Verachtert <dries@ulyssis.org> 11.0e-1
- Initial package
