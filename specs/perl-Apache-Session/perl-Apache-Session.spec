# $Id$
# Authority: dries
# Upstream: Casey West <casey$geeknest,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Apache-Session

Summary: Persistence framework for session data
Name: perl-Apache-Session
Version: 1.86
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Apache-Session/

Source: http://www.cpan.org/modules/by-module/Apache/Apache-Session-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl-DBI

%description
These modules provide persistent storage for arbitrary data, in arbitrary
backing stores.  The details of interacting with the backing store are
abstracted to make all backing stores behave alike.  The programmer simply
interacts with a tied hash.

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
%doc CHANGES Contributing.txt INSTALL MANIFEST META.yml README TODO eg/
%doc %{_mandir}/man3/Apache::Session.3pm*
%doc %{_mandir}/man3/Apache::Session::*.3pm*
%dir %{perl_vendorlib}/Apache/
%{perl_vendorlib}/Apache/Session/
%{perl_vendorlib}/Apache/Session.pm

%changelog
* Sun Feb 17 2008 Dag Wieers <dag@wieers.com> - 1.86-1
- Updated to release 1.86.

* Thu Dec 27 2007 Dag Wieers <dag@wieers.com> - 1.85-1
- Updated to release 1.85.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 1.81-1
- Updated to release 1.81.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.80-1
- Updated to release 1.80.

* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 1.6-1
- Initial package.

