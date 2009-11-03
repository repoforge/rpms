# $Id$
# Authority: dag
# Upstream: Kevin A. Lenzo <lenzo$yetanother,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name YAPC

Summary: Perl module that implements Yet Another Perl Conference
Name: perl-YAPC
Version: 1.01
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/YAPC/

Source: http://www.cpan.org/authors/id/L/LE/LENZO/YAPC-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-YAPC is a Perl module that implements Yet Another Perl Conference.

This package contains the following Perl module:

    YAPC

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
%doc Changes MANIFEST
%doc %{_mandir}/man3/YAPC.3pm*
%doc %{_mandir}/man3/YAPC::Venue.3pm*
%{perl_vendorlib}/YAPC/
%{perl_vendorlib}/YAPC.pm

%changelog
* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 1.01-1
- Initial package. (using DAR)
