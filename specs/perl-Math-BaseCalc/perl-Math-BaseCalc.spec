# $Id$
# Authority: dries
# Upstream: Ken Williams <ken$forum,swarthmore,edu>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Math-BaseCalc

Summary: Convert numbers between various bases
Name: perl-Math-BaseCalc
Version: 1.013
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-BaseCalc/

Source: http://www.cpan.org/modules/by-module/Math/Math-BaseCalc-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)

%description
This module facilitates the conversion of numbers between various number
bases. You may define your own digit sets, or use any of several
predefined digit sets.

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
%doc Changes MANIFEST META.yml README SIGNATURE
%doc %{_mandir}/man3/Math::BaseCalc.3pm*
%dir %{perl_vendorlib}/Math/
#%{perl_vendorlib}/Math/BaseCalc/
%{perl_vendorlib}/Math/BaseCalc.pm

%changelog
* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 1.013-1
- Updated to version 1.013.

* Mon Oct 13 2008 Dag Wieers <dag@wieers.com> - 1.012-1
- Updated to release 1.012.

* Tue Apr 05 2005 Dries Verachtert <dries@ulyssis.org> - 1.011-1
- Initial package.
