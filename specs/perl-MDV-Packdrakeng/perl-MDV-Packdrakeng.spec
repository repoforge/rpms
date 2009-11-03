# $Id$
# Authority: dag
# Upstream: Olivier Thauvin <nanardon$nanardon,zarb,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name MDV-Packdrakeng

Summary: Simple Archive Extractor/Builder
Name: perl-MDV-Packdrakeng
Version: 1.13
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/MDV-Packdrakeng/

Source: http://www.cpan.org/authors/id/N/NA/NANARDON/MDV-Packdrakeng-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Simple Archive Extractor/Builder.

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
%doc ChangeLog MANIFEST META.yml README
%doc %{_mandir}/man3/MDV::Packdrakeng.3pm*
%doc %{_mandir}/man3/MDV::Packdrakeng::zlib.3pm*
%dir %{perl_vendorlib}/MDV/
%{perl_vendorlib}/MDV/Packdrakeng/
%{perl_vendorlib}/MDV/Packdrakeng.pm

%changelog
* Sat Nov 24 2007 Dag Wieers <dag@wieers.com> - 1.13-1
- Initial package. (using DAR)
