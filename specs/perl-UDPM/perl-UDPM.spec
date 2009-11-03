# $Id$
# Authority: dag
# Upstream: Kevin C. Krinke <kckrinke$opendoorsoftware,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name UDPM

Summary: Perl module for User Dialogs
Name: perl-UDPM
Version: 0.88
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/UDPM/

Source: http://www.cpan.org/authors/id/K/KC/KCK/UDPM-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-UDPM is a Perl module for User Dialogs.

This package contains the following Perl module:

    UDPM

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
%doc COPYRIGHT Changes MANIFEST README examples/
%doc %{_mandir}/man3/UDPM.3pm*
#%{perl_vendorlib}/UDPM/
%{perl_vendorlib}/UDPM.pm

%changelog
* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.88-1
- Initial package. (using DAR)
