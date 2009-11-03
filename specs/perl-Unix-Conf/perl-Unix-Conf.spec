# $Id$
# Authority: dag
# Upstream: Karthik Krishnamurthy <karthik,k$extremix,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Unix-Conf

Summary: Front end for class methods in various utility modules under the Unix::Conf namespace
Name: perl-Unix-Conf
Version: 0.2
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Unix-Conf/

Source: http://www.cpan.org/modules/by-module/Unix/Unix-Conf-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Front end for class methods in various utility modules
under the Unix::Conf namespace.

This package contains the following Perl module:

    Unix::Conf

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
%doc Changes MANIFEST README
%doc %{_mandir}/man3/Unix::Conf.3pm*
%doc %{_mandir}/man3/Unix::Conf::ConfIO.3pm*
%doc %{_mandir}/man3/Unix::Conf::Err.3pm*
%dir %{perl_vendorlib}/Unix/
%{perl_vendorlib}/Unix/Conf/
%{perl_vendorlib}/Unix/Conf.pm

%changelog
* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.2-1
- Initial package. (using DAR)
