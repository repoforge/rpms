# $Id$
# Authority: dag
# Upstream: Guillaume Rousse <grousse$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Youri-Package-RPM-Generator
%define real_version 0.001000

Summary: Perl module to implement a template-based rpm generator
Name: perl-Youri-Package-RPM-Generator
Version: 0.1.0
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Youri-Package-RPM-Generator/

Source: http://www.cpan.org/authors/id/G/GR/GROUSSE/Youri-Package-RPM-Generator-v%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Youri-Package-RPM-Generator is a Perl module to implement
a template-based rpm generator.

This package contains the following Perl module:

    Youri::Package::RPM::Generator

%prep
%setup -n %{real_name}-v%{version}

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
%doc ChangeLog MANIFEST META.yml README
%doc %{_mandir}/man3/Youri::Package::RPM::Generator.3pm*
%dir %{perl_vendorlib}/Youri/
%dir %{perl_vendorlib}/Youri/Package/
%dir %{perl_vendorlib}/Youri/Package/RPM/
#%{perl_vendorlib}/Youri/Package/RPM/Generator/
%{perl_vendorlib}/Youri/Package/RPM/Generator.pm

%changelog
* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.1.0-1
- Initial package. (using DAR)
