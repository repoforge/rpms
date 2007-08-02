# $Id$
# Authority: dries
# Upstream: Nicholas J Humfrey <njh$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Socket-Multicast6

Summary: Constructors and constants for IPv4 and IPv6 multicast socket operations
Name: perl-Socket-Multicast6
Version: 0.02
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Socket-Multicast6/

Source: http://search.cpan.org//CPAN/authors/id/N/NJ/NJH/Socket-Multicast6-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
Constructors and constants for IPv4 and IPv6 multicast socket operations.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/Socket::Multicast6*
%{perl_vendorarch}/Socket/Multicast6.pm
%{perl_vendorarch}/auto/Socket/Multicast6/

%changelog
* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.02-1
- Initial package.
