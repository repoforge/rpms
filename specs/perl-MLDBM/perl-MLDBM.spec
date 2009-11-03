# $Id$
# Authority: dag
# Upstream: Joshua Chamas <josh$chamas,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name MLDBM

Summary: MLDBM module for perl
Name: perl-MLDBM
Version: 2.01
Release: 2.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/MLDBM/

Source: http://www.cpan.org/modules/by-module/MLDBM/MLDBM-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 2:5.8.0
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl >= 2:5.8.0

%description
MLDBM module for perl.

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
%doc Changes MANIFEST README
%doc %{_mandir}/man3/MLDBM.3pm*
%{perl_vendorlib}/MLDBM/
%{perl_vendorlib}/MLDBM.pm

%changelog
* Fri Jan 13 2006 Dag Wieers <dag@wieers.com> - 2.01-2
- Cosmetic cleanup.

* Wed Jul 16 2003 Dag Wieers <dag@wieers.com> - 2.01-0
- Initial package. (using DAR)
