# $Id$
# Authority: dries
# Upstream: Andy Grundman <andy$hybridized,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTTP-Body

Summary: HTTP Body parser
Name: perl-HTTP-Body
Version: 1.02
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTTP-Body/

Source: http://www.cpan.org/modules/by-module/HTTP/HTTP-Body-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module contains a HTTP body parser.

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
%doc %{_mandir}/man3/HTTP::Body.3pm*
%doc %{_mandir}/man3/HTTP::Body::*.3pm*
%dir %{perl_vendorlib}/HTTP/
%{perl_vendorlib}/HTTP/Body/
%{perl_vendorlib}/HTTP/Body.pm

%changelog
* Sun Mar 02 2008 Dag Wieers <dag@wieers.com> - 1.02-1
- Updated to release 1.02.

* Mon Feb 25 2008 Dag Wieers <dag@wieers.com> - 1.01-1
- Updated to release 1.01.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.9-1
- Updated to release 0.9.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 0.6-1
- Updated to release 0.6.

* Thu Dec 15 2005 Dries Verachtert <dries@ulyssis.org> - 0.5-1
- Initial package.
