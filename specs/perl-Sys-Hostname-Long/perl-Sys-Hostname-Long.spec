# $Id$
# Authority: dries
# Upstream: Scott Penrose <scottp$dd,com,au>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Sys-Hostname-Long

Summary: Get the full hostname
Name: perl-Sys-Hostname-Long
Version: 1.4
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Sys-Hostname-Long/

Source: http://www.cpan.org/modules/by-module/Sys/Sys-Hostname-Long-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module uses different ways to get the full hostname.

%prep
%setup -n %{real_name}-%{version}
# Remove the usage of windows only modules.
%{__perl} -pi -e "s|use Win32::TieRegistry.*||g;" lib/Sys/Hostname/Long.pm

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
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Sys/Hostname/Long.pm
%{perl_vendorlib}/Sys/Hostname/testall.pl

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.4-1.2
- Rebuild for Fedora Core 5.

* Fri Mar  3 2006 Dries Verachtert <dries@ulyssis.org> - 1.4-1
- Initial package.
