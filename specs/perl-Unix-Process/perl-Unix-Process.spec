# $Id$
# Authority: dag
# Upstream: Paul Miller <japh$voltar-confed,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Unix-Process
%define real_version 1.001001

Summary: Perl module to get pid info from (/bin/ps)
Name: perl-Unix-Process
Version: 1.3101
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Unix-Process/

Source: http://www.cpan.org/modules/by-module/Unix/Unix-Process-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Unix-Process is a Perl module to get pid info from (/bin/ps).

This package contains the following Perl module:

    Unix::Process

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
%doc Changes MANIFEST MANIFEST.SKIP README 
%doc %{_mandir}/man3/Unix::Process.3pm*
%dir %{perl_vendorlib}/Unix/
%{perl_vendorlib}/Unix/Process.pm

%changelog
* Mon Jun  8 2009 Christoph Maser <cmr@financial.com> - 1.3101-1
- Updated to version 1.3101.

* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 1.1.1-1
- Initial package. (using DAR)
