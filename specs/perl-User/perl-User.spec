# $Id$
# Authority: dag
# Upstream: Terrence Brannon <sundevil$livingcosmos,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name User

Summary: Perl module for locating user information regardless of OS
Name: perl-User
Version: 1.8
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/User/

Source: http://www.cpan.org/modules/by-module/User/User-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-User is a Perl module for locating user information regardless of OS.

This package contains the following Perl module:

    User

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
%doc Changes MANIFEST META.yml
%doc %{_mandir}/man3/User.3pm*
#%{perl_vendorlib}/User/
%{perl_vendorlib}/User.pm

%changelog
* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 1.8-1
- Initial package. (using DAR)
