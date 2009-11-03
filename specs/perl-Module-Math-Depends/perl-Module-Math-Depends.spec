# $Id$
# Authority: dries
# Upstream: Adam Kennedy <adamk$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Module-Math-Depends

Summary: Convenience object for manipulating module dependencies
Name: perl-Module-Math-Depends
Version: 0.02
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Module-Math-Depends/

Source: http://www.cpan.org/modules/by-module/Module/Module-Math-Depends-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.005
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More) >= 0.42
Requires: perl >= 0:5.005

%description
Convenience object for manipulating module dependencies.

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
%doc Changes LICENSE MANIFEST META.yml README
%doc %{_mandir}/man3/Module::Math::Depends.3pm*
%dir %{perl_vendorlib}/Module/
%dir %{perl_vendorlib}/Module/Math/
#%{perl_vendorlib}/Module/Math/Depends/
%{perl_vendorlib}/Module/Math/Depends.pm

%changelog
* Wed Oct 15 2008 Dag Wieers <dag@wieers.com> - 0.02-1
- Updated to release 0.02.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.01-1
- Initial package.
