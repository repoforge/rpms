# $Id: $
# Authority: dries
# Upstream: Josh Carter <josh$multipart-mixed,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Image-IPTCInfo

Summary: Extract IPTC image meta-data
Name: perl-Image-IPTCInfo
Version: 1.95
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Image-IPTCInfo/

Source: http://www.cpan.org/modules/by-module/Image/Image-IPTCInfo-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
Requires: perl

%description
This Perl extention allows you to extract IPTC meta information from images.

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
%doc MANIFEST META.yml README
%doc %{_mandir}/man3/Image::IPTCInfo.3pm*
%dir %{perl_vendorlib}/Image/
%{perl_vendorlib}/Image/demo.pl
%{perl_vendorlib}/Image/IPTCInfo.pm

%changelog
* Wed Jul 23 2008 Dries Verachtert <dries@ulyssis.org> - 1.95-1
- Initial package.
