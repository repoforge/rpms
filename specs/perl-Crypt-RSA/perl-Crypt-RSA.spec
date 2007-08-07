# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

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
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
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
%doc MANIFEST README
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/Crypt/
%{perl_vendorlib}/Crypt/RSA/
%{perl_vendorlib}/Crypt/RSA.pm

%changelog
* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 1.58-1
- Updated to release 1.58.

* Thu Jan 12 2006 Dag Wieers <dag@wieers.com> - 1.57-1
- Initial package. (using DAR)
