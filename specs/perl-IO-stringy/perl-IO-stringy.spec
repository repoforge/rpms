# $Id$
# Authority: dries
# Upstream: David F. Skoll <dfs+pause$roaringpenguin,com>

### EL6 ships with perl-IO-stringy-2.110-10.1.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name IO-stringy

Summary: IO-Stringy - I/O on in-core objects like strings and arrays
Name: perl-IO-stringy
Version: 2.110
Release: 1.2%{?dist}
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/IO-stringy/

Source: http://www.cpan.org/modules/by-module/IO/IO-stringy-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.00503
BuildRequires: perl(ExtUtils::MakeMaker)
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
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find contrib/ examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING MANIFEST META.yml README contrib/ examples/
%doc %{_mandir}/man3/IO::*.3pm*
%{perl_vendorlib}/IO/

%changelog
* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 2.110-1
- Updated to release 2.110.

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
