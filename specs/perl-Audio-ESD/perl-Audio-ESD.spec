# $Id$
# Authority: dries
# Upstream: David Huggins-Daines <dhd$pobox,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Audio-ESD

Summary: Extension for talking to the Enlightened Sound Daemon
Name: perl-Audio-ESD
Version: 0.02
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Audio-ESD/

Source: http://www.cpan.org/modules/by-module/Audio/Audio-ESD-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: esound-devel

%description
This module provides a Perl interface to the Enlightened Sound Daemon,
which is used on many GNU/Linux systems to mix sound output streams
from multiple desktop applications.  It allows you to open input,
output, monitoring, and filtering streams which function like normal
Perl filehandles, as well as to control various parameters on the ESD
server.

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
%doc Changes README
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/Audio/
%{perl_vendorarch}/Audio/ESD.pm
%dir %{perl_vendorarch}/auto/Audio/
%{perl_vendorarch}/auto/Audio/ESD/

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.02-1
- Initial package.
