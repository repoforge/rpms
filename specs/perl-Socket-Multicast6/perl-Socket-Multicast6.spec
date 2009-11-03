# $Id$
# Authority: dries
# Upstream: Nicholas J Humfrey <njh$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Socket-Multicast6

Summary: Constructors and constants for IPv4 and IPv6 multicast socket operations
Name: perl-Socket-Multicast6
Version: 0.02
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Socket-Multicast6/

Source: http://www.cpan.org/modules/by-module/Socket/Socket-Multicast6-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Constructors and constants for IPv4 and IPv6 multicast socket operations.

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
%doc %{_mandir}/man3/Socket::Multicast6*.3pm*
%dir %{perl_vendorarch}/Socket/
%{perl_vendorarch}/Socket/Multicast6.pm
%dir %{perl_vendorarch}/auto/Socket/
%{perl_vendorarch}/auto/Socket/Multicast6/

%changelog
* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.02-1
- Initial package.
