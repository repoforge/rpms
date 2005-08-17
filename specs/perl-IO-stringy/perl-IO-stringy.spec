# $Id$
# Authority: dries

%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)

%define rname IO-stringy

Summary: IO-Stringy - I/O on in-core objects like strings and arrays
Name: perl-IO-stringy
Version: 2.109
Release: 1
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/IO-stringy/

Source: http://www.cpan.org/modules/by-module/IO/IO-stringy-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.00503
Requires: perl >= 0:5.00503

Obsoletes: perl-IO-Stringy <= %{version}-%{release}
Provides: perl-IO-Stringy

%description
This toolkit primarily provides modules for performing both traditional
and object-oriented i/o) on things *other* than normal filehandles; in
particular, IO::Scalar, IO::ScalarArray, and IO::Lines.

In the more-traditional IO::Handle front, we have IO::AtomicFile which
may be used to painlessly create files which are updated atomically.

%prep
%setup -n %{rname}-%{version} 

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL \
	PREFIX="%{buildroot}%{_prefix}" \
	INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib}
%{__rm} -rf %{buildroot}%{perl_vendorarch}

%clean 
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README* MANIFEST COPYING docs/*
%doc %{_mandir}/man3/*.3pm*
%{perl_vendorlib}/IO/

%changelog
* Sun Aug 08 2004 Dag Wieers <dag@wieers.com> - 2.109-1
- Cosmetic cleanup.

* Mon May 17 2004 Dag Wieers <dag@wieers.com> - 2.109-0
- Updated to release 2.109.

* Wed Dec 03 2003 Dag Wieers <dag@wieers.com> - 2.108-4
- Renamed to perl-IO-stringy to satisfy Axel Thimm.

* Wed Aug 27 2003 Dag Wieers <dag@wieers.com> - 2.108-3
- Provide perl-IO-stringy too.

* Sun Jan 26 2003 Dag Wieers <dag@wieers.com> - 2.108-0
- Initial package. (using DAR)
