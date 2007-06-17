# $Id$

# Authority: dries
# Upstream: Vipul Ved Prakash <mail$vipul,net>


%define real_name Digest-Nilsimsa
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Nilsimsa algorithm
Name: perl-Digest-Nilsimsa
Version: 0.06
Release: 1.2
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Digest-Nilsimsa/

Source: http://www.cpan.org/modules/by-module/Digest/Digest-Nilsimsa-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
This module contains a perl version of the Nilsimsa code.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README
%{_mandir}/man3/*
%{perl_vendorarch}/Digest/Nilsimsa.pm
%{perl_vendorarch}/auto/Digest/Nilsimsa/Nilsimsa.bs
%{perl_vendorarch}/auto/Digest/Nilsimsa/Nilsimsa.so

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.06-1.2
- Rebuild for Fedora Core 5.

* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 0.06-1
- Initial package.
