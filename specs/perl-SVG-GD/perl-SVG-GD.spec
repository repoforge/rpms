# $Id: perl-IP-Country.spec 171 2004-03-28 01:43:07Z dag $
# Authority: dag
# Upstream: Ronan Oger<ronan$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name SVG-GD

Summary: Perl SVG-GD module
Name: perl-SVG-GD
Version: 0.20
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/SVG-GD/

Source: http://www.cpan.org/modules/by-module/SVG/SVG-GD-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.00503
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl >= 0:5.00503

%description
Perl SVG-GD module.

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

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes LICENSE MANIFEST META.yml README examples/
%doc %{_mandir}/man3/SVG::GD.3pm*
%dir %{perl_vendorlib}/SVG/
%{perl_vendorlib}/SVG/GD.pm

%changelog
* Wed Jun 17 2009 Christoph Maser <cmr@financial.com> - 0.20-1
- Updated to version 0.20.

* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 0.15-1
- Updated to release 0.15.

* Tue Aug 07 2007 Dag Wieers <dag@wieers.com> - 0.07-2
- Disabled auto-requires for examples/.

* Tue Apr 13 2004 Dag Wieers <dag@wieers.com> - 0.07-1
- Initial package. (using DAR)
