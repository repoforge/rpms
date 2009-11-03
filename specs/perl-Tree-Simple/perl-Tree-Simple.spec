# $Id$
# Authority: dries
# Upstream: Stevan Little <stevan$iinteractive,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Tree-Simple

Summary: Simple tree object
Name: perl-Tree-Simple
Version: 1.18
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Tree-Simple/

Source: http://www.cpan.org/modules/by-module/Tree/Tree-Simple-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.6.0
BuildRequires: perl(Test::Exception) >= 0.15
BuildRequires: perl(Test::More) >= 0.47
Requires: perl >= 0:5.6.0

%description
A simple tree object.

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Tree::Simple.3pm*
%doc %{_mandir}/man3/Tree::Simple::*.3pm*
%dir %{perl_vendorlib}/Tree/
%{perl_vendorlib}/Tree/Simple/
%{perl_vendorlib}/Tree/Simple.pm

%changelog
* Mon Nov 19 2007 Dag Wieers <dag@wieers.com> - 1.18-1
- Updated to release 1.18.

* Tue Nov 14 2006 Dries Verachtert <dries@ulyssis.org> - 1.17-1
- Updated to release 1.17.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 1.16-1
- Updated to release 1.16.

* Thu Dec 15 2005 Dries Verachtert <dries@ulyssis.org> - 1.15-1
- Initial package.
