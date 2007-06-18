# $Id$

# Authority: dries
# Upstream: Michael Robinton <michael$bizsystems,com>

%define real_name Net-DNS-Codes
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Collection of C library DNS codes
Name: perl-Net-DNS-Codes
Version: 0.09
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-DNS-Codes/

Source: http://www.cpan.org/modules/by-module/Net/Net-DNS-Codes-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
Net::DNS::Codes provides forward and reverse lookup for most common "C"
library DNS codes as well as all the codes for the DNS HEADER field.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Net/DNS/Codes.pm

%changelog
* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.09-1
- Updated to release 0.09.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.08-1.2
- Rebuild for Fedora Core 5.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.08-1
- Initial package.
