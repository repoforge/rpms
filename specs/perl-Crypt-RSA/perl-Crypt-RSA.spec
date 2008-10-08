# $Id$
# Authority: dag
# Upstream: Vipul Ved Prakash <mail$vipul,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Crypt-RSA

Summary: RSA public-key cryptosystem
Name: perl-Crypt-RSA
Version: 1.98
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Crypt-RSA/

Source: http://www.cpan.org/modules/by-module/Crypt/Crypt-RSA-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.6.0
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl >= 0:5.6.0

%description
RSA public-key cryptosystem.

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
%doc ARTISTIC COPYING Changes MANIFEST MANIFEST.skip META.yml README TODO
%doc %{_mandir}/man3/Crypt::RSA.3pm*
%doc %{_mandir}/man3/Crypt::RSA::*.3pm*
%dir %{perl_vendorlib}/Crypt/
%{perl_vendorlib}/Crypt/RSA/
%{perl_vendorlib}/Crypt/RSA.pm

%changelog
* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 1.98-1
- Updated to release 1.98.

* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 1.58-1
- Updated to release 1.58.

* Thu Jan 12 2006 Dag Wieers <dag@wieers.com> - 1.57-1
- Initial package. (using DAR)
