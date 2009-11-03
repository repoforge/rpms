# $Id$
# Authority: dries
# Upstream: Douglas Wilson <dougw%20at%20cpan%20dot%20org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-CIDR-Lite

Summary: Merge IPv4 or IPv6 CIDR addresses
Name: perl-Net-CIDR-Lite
Version: 0.20
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-CIDR-Lite/

Source: http://www.cpan.org/modules/by-module/Net/Net-CIDR-Lite-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Perl extension for merging IPv4 or IPv6 CIDR addresses.

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
%doc Changes README
%doc %{_mandir}/man3/Net::CIDR::Lite*
%{perl_vendorlib}/Net/CIDR/Lite.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.20-1.2
- Rebuild for Fedora Core 5.

* Fri Mar  3 2006 Dries Verachtert <dries@ulyssis.org> - 0.20-1
- Initial package.

