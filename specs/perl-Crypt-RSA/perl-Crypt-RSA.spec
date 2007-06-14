# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define rname Crypt-RSA

Summary: Crypt-RSA module for perl
Name: perl-Crypt-RSA
Version: 1.58
Release: 1
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Crypt-RSA/

Source: http://www.cpan.org/modules/by-module/Crypt/Crypt-RSA-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.00503, perl(ExtUtils::MakeMaker)
Requires: perl >= 0:5.00503

%description
Crypt-RSA module for perl

%prep
%setup -n %{rname}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc MANIFEST README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/Crypt/
%{perl_vendorlib}/Crypt/RSA.pm
%{perl_vendorlib}/Crypt/RSA/

%changelog
* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 1.58-1
- Updated to release 1.58.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.57-1.2
- Rebuild for Fedora Core 5.

* Thu Jan 12 2006 Dag Wieers <dag@wieers.com> - 1.57-1
- Initial package. (using DAR)
