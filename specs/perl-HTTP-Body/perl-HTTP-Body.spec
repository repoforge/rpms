# $Id$
# Authority: dries
# Upstream: Marcus Ramberg <mramberg@cpan.org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTTP-Body

Summary: HTTP Body parser
Name: perl-HTTP-Body
Version: 1.06
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTTP-Body/

Source: http://search.cpan.org/CPAN/authors/id/M/MR/MRAMBERG/HTTP-Body-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Carp)
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Temp) >= 0.14
BuildRequires: perl(HTTP::Headers)
BuildRequires: perl(IO::File)
BuildRequires: perl(Test::Deep)
#BuildRequires: perl(Test::More) >= 0.86
BuildRequires: perl(Test::More)
Requires: perl(Carp)
Requires: perl(File::Temp) >= 0.14
Requires: perl(HTTP::Headers)
Requires: perl(IO::File)

%filter_from_requires /^perl*/d
%filter_setup

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
* Tue Jan 12 2010 Christoph Maser <cmr@financial.com> - 1.06-1
- Updated to version 1.06.

* Sun Jul  5 2009 Christoph Maser <cmr@financial.com> - 1.05-1
- Updated to version 1.05.

* Wed Oct 08 2008 Dag Wieers <dag@wieers.com> - 1.04-1
- Updated to release 1.04.

* Mon May 05 2008 Dag Wieers <dag@wieers.com> - 1.03-1
- Updated to release 1.03.

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
