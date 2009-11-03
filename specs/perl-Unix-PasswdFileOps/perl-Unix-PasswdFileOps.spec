# $Id$
# Authority: dag
# Upstream: Ben Maynard <cpan$geekserv,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Unix-PasswdFileOps

Summary: Perl module for operations on Unix Passwd file
Name: perl-Unix-PasswdFileOps
Version: 0.2
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Unix-PasswdFileOps/

Source: http://www.cpan.org/modules/by-module/Unix/Unix-PasswdFileOps-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Unix-PasswdFileOps is a Perl module for operations on Unix Passwd file.

This package contains the following Perl module:

    Unix::PasswdFileOps

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Unix::PasswdFileOps.3pm*
%dir %{perl_vendorlib}/Unix/
#%{perl_vendorlib}/Unix/PasswdFileOps/
%{perl_vendorlib}/Unix/PasswdFileOps.pm

%changelog
* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.2-1
- Initial package. (using DAR)
