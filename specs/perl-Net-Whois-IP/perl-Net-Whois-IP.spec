# $Id$
# Authority: dries
# Upstream: Ben Schmitz <ben$foink,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-Whois-IP

Summary: Lookup the whois information for ipaddresses
Name: perl-Net-Whois-IP
Version: 1.04
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-Whois-IP/

Source: http://www.cpan.org/modules/by-module/Net/Net-Whois-IP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Perl extension for looking up the whois information for ipadresses.

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
%doc Changes
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/Net/Whois
%{perl_vendorlib}/Net/Whois/IP.pm
%{perl_vendorlib}/auto/Net/Whois/IP/

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 1.04-1
- Updated to release 1.04.

* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 1.02-1
- Updated to release 1.02.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.01-2.2
- Rebuild for Fedora Core 5.

* Sat Jan 14 2006 Dries Verachtert <dries@ulyssis.org> - 1.01-2
- Also added the directory, thanks to Earl Sammons.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.01-1
- Initial package.

