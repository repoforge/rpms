# $Id$
# Authority: dag
# Upstream: Stevan Little <stevan$iinteractive,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Tree-Simple-Visitor-FindByPath
%define real_version 0.03

Summary: Perl module named Tree-Simple-Visitor-FindByPath
Name: perl-Tree-Simple-Visitor-FindByPath
Version: 0.10
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Tree-Simple-Visitor-FindByPath/

Source: http://www.cpan.org/modules/by-module/Tree/Tree-Simple-VisitorFactory-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Tree-Simple-Visitor-FindByPath is a Perl module.

%prep
%setup -n Tree-Simple-VisitorFactory-%{version}

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
%doc %{_mandir}/man3/Tree::Simple::Visitor::FindByPath.3pm*
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/Tree/
%dir %{perl_vendorlib}/Tree/Simple/
%dir %{perl_vendorlib}/Tree/Simple/Visitor/
%{perl_vendorlib}/Tree/Simple/Visitor/FindByPath/
%{perl_vendorlib}/Tree/Simple/Visitor/FindByPath.pm

%changelog
* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 0.10-1
- Initial package. (using DAR)
