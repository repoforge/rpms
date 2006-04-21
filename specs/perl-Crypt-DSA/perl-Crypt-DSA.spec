# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define rname Crypt-DSA

Summary: Crypt-DSA module for perl
Name: perl-Crypt-DSA
Version: 0.13
Release: 1.2
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Crypt-DSA/

Source: http://www.cpan.org/modules/by-module/Crypt/Crypt-DSA-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.00503, perl(Math::BigInt) >= 1.60, perl(Digest::SHA1) >= 2.02
BuildRequires: perl(Convert::PEM) >= 0.07, perl(Data::Buffer) >= 0.01
Requires: perl >= 0:5.00503

%description
Crypt-DSA module for perl

%prep
%setup -n %{rname}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

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
%{perl_vendorlib}/Crypt/DSA.pm
%{perl_vendorlib}/Crypt/DSA/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.13-1.2
- Rebuild for Fedora Core 5.

* Thu Jan 12 2006 Dag Wieers <dag@wieers.com> - 0.13-1
- Initial package. (using DAR)
