# $Id$
# Authority: dries
# Upstream: Nikolay Pelov <pelov$cs,kuleuven,ac,be>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Authen-PAM

Summary: Interface to the PAM library
Name: perl-Authen-PAM
Version: 0.14 
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Authen-PAM/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://www.cpan.org/modules/by-module/Authen/Authen-PAM-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, pam-devel

%description
This module provides a Perl interface to the PAM library.

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
%doc README Changes FAQ.pod
%{_mandir}/man3/*
%{perl_vendorarch}/Authen/FAQ.pod
%{perl_vendorarch}/Authen/PAM.pm
%{perl_vendorarch}/auto/Authen/PAM/PAM.bs
%{perl_vendorarch}/auto/Authen/PAM/PAM.so

%changelog
* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 0.14-1
- Initial package.

