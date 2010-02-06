# $Id$
# Authority: dries
# Upstream: Ask Bjoern Hansen <ask@perl.org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Apache-DBI

Summary: Persistent database connections and basic authentication support
Name: perl-Apache-DBI
Version: 1.08
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Apache-DBI/

Source: http://search.cpan.org/CPAN/authors/id/A/AB/ABH/Apache-DBI-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(DBI) >= 1
BuildRequires: perl(Digest::MD5) >= 2.2
BuildRequires: perl(Digest::SHA1) >= 2.01
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)
Requires: perl(DBI) >= 1
Requires: perl(Digest::MD5) >= 2.2
Requires: perl(Digest::SHA1) >= 2.01
Requires: perl(Test::More)

%filter_from_requires /^perl*/d
%filter_setup


%description
This module is supposed to be used with the Apache server together with
an embedded perl interpreter like mod_perl. It provides support for basic
authentication and authorization as well as support for persistent database
connections via Perl's Database Independent Interface (DBI).

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}
%{__make} test

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find eg/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README TODO traces.txt eg/
%doc %{_mandir}/man3/Apache::AuthDBI.3pm*
%doc %{_mandir}/man3/Apache::DBI.3pm*
%dir %{perl_vendorlib}/Apache/
%{perl_vendorlib}/Apache/AuthDBI.pm
%{perl_vendorlib}/Apache/DBI.pm


%changelog
* Sat Feb  6 2010 Christoph Maser <cmr@financial.com> - 1.08-1
- Updated to version 1.08.

* Sun Jun 22 2008 Dag Wieers <dag@wieers.com> - 1.07-1
- Updated to release 1.07.

* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 1.06-1
- Updated to release 1.06.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.9901-2
- Fixed the source url.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.9901-1
- Updated to release 0.9901.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.94-1
- Initial package.
