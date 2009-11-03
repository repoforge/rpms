# $Id$
# Authority: dries
# Upstream: John D Groenveld <groenveld$acm,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Apache-DBILogin

Summary: Authenticates and authorizes via a DBI connection
Name: perl-Apache-DBILogin
Version: 2.06
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Apache-DBILogin/

Source: http://www.cpan.org/modules/by-module/Apache/Apache-DBILogin-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
The perl module Apache::DBILogin uses Apache mod_perl and the
DBI/DBD modules to integrate database authentication with Apache.

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
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Apache/DBILogin.pm

%changelog
* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 2.06-1
- Updated to release 2.06.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 2.03-1
- Initial package.
