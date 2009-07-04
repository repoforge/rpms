# $Id$
# Authority: dries
# Upstream: Olaf Kolkman <net-dns-sec$ripe,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-DNS-SEC

Summary: Support for DNS Resource Record
Name: perl-Net-DNS-SEC
Version: 0.15
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-DNS-SEC/

Source: http://www.cpan.org/modules/by-module/Net/Net-DNS-SEC-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module implements DNS Resource Record types that are relevant
for DNSSEC operations. The implementation is based on the DNSSEC-bis
document set.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/Net/DNS/SEC/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%{_mandir}/man3/Net::DNS::*.3pm*
%{perl_vendorlib}/Net/DNS/Keyset.pm
%{perl_vendorlib}/Net/DNS/SEC.pm
%{perl_vendorlib}/Net/DNS/RR/
%{perl_vendorlib}/Net/DNS/SEC/

%changelog
* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 0.15-1
- Updated to version 0.15.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.14-1
- Updated to release 0.14.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.13-1.2
- Rebuild for Fedora Core 5.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 0.13-1
- Updated to release 0.13.

* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 0.12-1
- Initial package.
