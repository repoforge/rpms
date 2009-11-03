# $Id$
# Authority: dries
# Upstream: Stevan Little <stevan,little$iinteractive,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Tree-Simple-VisitorFactory

Summary: Visitor for Tree::Simple objects
Name: perl-Tree-Simple-VisitorFactory
Version: 0.10
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Tree-Simple-VisitorFactory/

Source: http://www.cpan.org/modules/by-module/Tree/Tree-Simple-VisitorFactory-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module implements different versions of the Visitor pattern for Simple::Tree objects.

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
%doc %{_mandir}/man3/Tree::Simple::VisitorFactory.3pm*
%doc %{_mandir}/man3/Tree::Simple::Visitor::*.3pm*
%dir %{perl_vendorlib}/Tree/
%dir %{perl_vendorlib}/Tree/Simple/
%{perl_vendorlib}/Tree/Simple/Visitor/
%{perl_vendorlib}/Tree/Simple/VisitorFactory.pm

%changelog
* Thu Dec 15 2005 Dries Verachtert <dries@ulyssis.org> - 0.10-1
- Initial package.
