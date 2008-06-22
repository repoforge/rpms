# $Id$
# Authority: dries
# Upstream: Philip M. Gollucci <pgollucci$p6m7g8,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Apache-DBI

Summary: Persistent database connections and basic authentication support
Name: perl-Apache-DBI
Version: 1.07
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Apache-DBI/

Source: http://www.cpan.org/modules/by-module/Apache/Apache-DBI-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

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
