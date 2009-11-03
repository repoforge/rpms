# $Id$
# Authority: dag
# Upstream: Mike Taylor <perl$miketaylor,org,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name ZOOM-IRSpy

Summary: Perl module for discovering and analysing IR services
Name: perl-ZOOM-IRSpy
Version: 1.00
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/ZOOM-IRSpy/

Source: http://www.cpan.org/authors/id/M/MI/MIRK/ZOOM-IRSpy-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
perl-ZOOM-IRSpy is a Perl module for discovering and analysing IR services.

This package contains the following Perl module:

    ZOOM::IRSpy

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST MANIFEST.SKIP META.yml README
%doc %{_mandir}/man3/ZOOM::IRSpy.3pm*
%dir %{perl_vendorarch}/ZOOM/
%{perl_vendorarch}/ZOOM/IRSpy.pm
%dir %{perl_vendorarch}/auto/ZOOM/
%{perl_vendorarch}/auto/ZOOM/IRSpy/

%changelog
* Thu Oct 11 2007 Dag Wieers <dag@wieers.com> - 1.00-1
- Initial package. (using DAR)
