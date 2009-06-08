# $Id$
# Authority: dag
# Upstream: Gunnar Wolf <gwolf$gwolf,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name User-Simple

Summary: Perl module that implements a simple user sessions management
Name: perl-User-Simple
Version: 1.43
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/User-Simple/

Source: http://www.cpan.org/modules/by-module/User/User-Simple-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Module::Build)

%description
perl-User-Simple is a Perl module that implements
a simple user sessions management.

This package contains the following Perl module:

    User::Simple

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
%doc Changes MANIFEST META.yml README examples/
%doc %{_mandir}/man3/User::Simple.3pm*
%doc %{_mandir}/man3/User::Simple::Admin.3pm*
%dir %{perl_vendorlib}/User/
%{perl_vendorlib}/User/Simple/
%{perl_vendorlib}/User/Simple.pm

%changelog
* Mon Jun  8 2009 Christoph Maser <cmr@financial.com> - 1.43-1
- Updated to version 1.43.

* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 1.35-1
- Initial package. (using DAR)
