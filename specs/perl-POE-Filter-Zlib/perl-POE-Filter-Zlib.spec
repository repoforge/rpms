# $Id$
# Authority: dries
# Upstream: Chris Williams <chris$bingosnet,co,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name POE-Filter-Zlib

Summary: POE filter wrapped around Compress::Zlib
Name: perl-POE-Filter-Zlib
Version: 2.02
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/POE-Filter-Zlib/

Source: http://www.cpan.org/modules/by-module/POE/POE-Filter-Zlib-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(POE::Filter::Line)
BuildRequires: perl(POE::Filter::Stackable)
BuildRequires: perl(Test::More) >= 0.47

%description
A POE filter wrapped around Compress::Zlib.

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

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/POE::Filter::Zlib.3pm*
%doc %{_mandir}/man3/POE::Filter::Zlib::*.3pm*
%dir %{perl_vendorlib}/POE/
%dir %{perl_vendorlib}/POE/Filter/
%{perl_vendorlib}/POE/Filter/Zlib/
%{perl_vendorlib}/POE/Filter/Zlib.pm

%changelog
* Fri Jul  3 2009 Christoph Maser <cmr@financial.com> - 2.02-1
- Updated to version 2.02.

* Fri Mar 14 2008 Dag Wieers <dag@wieers.com> - 1.94-1
- Updated to release 1.94.

* Fri Jan 04 2008 Dag Wieers <dag@wieers.com> - 1.93-1
- Updated to release 1.93.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 1.92-1
- Updated to release 1.92.

* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 1.8-1
- Updated to release 1.8.

* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 1.7-1
- Updated to release 1.7.

* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 1.6-1
- Initial package.
