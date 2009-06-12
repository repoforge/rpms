# $Id$
# Authority: dag
# Upstream: Paul Seamons <perl$seamons,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Template-Alloy

Summary: TT2/3, HT, HTE, Tmpl, and Velocity Engine
Name: perl-Template-Alloy
Version: 1.013
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Template-Alloy/

Source: http://www.cpan.org/modules/by-module/Template/Template-Alloy-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
perl-Template-Alloy is a Perl module that implements a TT2/3, HT, HTE,
Tmpl, and Velocity Engine.

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
find samples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST MANIFEST.SKIP META.yml README samples/
%doc %{_mandir}/man3/Template::Alloy.3pm*
%doc %{_mandir}/man3/Template::Alloy::*.3pm*
%dir %{perl_vendorlib}/Template/
%{perl_vendorlib}/Template/Alloy/
%{perl_vendorlib}/Template/Alloy.pm
%{perl_vendorlib}/Template/Alloy.pod

%changelog
* Fri Jun 12 2009 Christoph Maser <cmr@financial.com> - 1.013-1
- Updated to version 1.013.

* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 1.012-1
- Updated to release 1.012.

* Fri Dec 14 2007 Dag Wieers <dag@wieers.com> - 1.011-1
- Updated to release 1.011.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 1.009-1
- Updated to release 1.009.

* Tue Aug 07 2007 Dag Wieers <dag@wieers.com> - 1.006-1
- Initial package. (using DAR)
