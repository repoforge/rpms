# $Id$
# Authority: dag
# Upstream: Michel Rodriguez <xmltwig$gmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Tree-XPathEngine

Summary: Perl module that implements a re-usable XPath engine
Name: perl-Tree-XPathEngine
Version: 0.05
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Tree-XPathEngine/

Source: http://www.cpan.org/modules/by-module/Tree/Tree-XPathEngine-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Tree-XPathEngine is a Perl module that implements a re-usable XPath engine.

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
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/Tree/
%{perl_vendorlib}/Tree/XPathEngine/
%{perl_vendorlib}/Tree/XPathEngine.pm

%changelog
* Sun Aug 05 2007 Dag Wieers <dag@wieers.com> - 0.05-1
- Initial package. (using DAR)
