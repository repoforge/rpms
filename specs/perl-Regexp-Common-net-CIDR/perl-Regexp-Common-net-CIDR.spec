# $Id$
# Authority: dries
# Upstream: Ruslan U. Zakirov <Ruslan,Zakirov$gmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Regexp-Common-net-CIDR

Summary: Provide patterns for CDIR blocks
Name: perl-Regexp-Common-net-CIDR
Version: 0.02
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Regexp-Common-net-CIDR/

Source: http://www.cpan.org/modules/by-module/Regexp/Regexp-Common-net-CIDR-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 2:5.8.0
BuildRequires: perl(Regexp::Common)
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl >= 2:5.8.0

%description
Provide patterns for CDIR blocks.

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
%doc %{_mandir}/man3/Regexp::Common::net::CIDR.3pm*
%dir %{perl_vendorlib}/Regexp/
%dir %{perl_vendorlib}/Regexp/Common/
%dir %{perl_vendorlib}/Regexp/Common/net/
#%{perl_vendorlib}/Regexp/Common/net/CIDR/
%{perl_vendorlib}/Regexp/Common/net/CIDR.pm

%changelog
* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 0.02-1
- Updated to release 0.02.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.01-1
- Initial package.
