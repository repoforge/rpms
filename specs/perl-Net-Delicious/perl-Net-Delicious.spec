# $Id$
# Authority: dries
# Upstream: Aaron Straup Cope <ascope$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-Delicious

Summary: OOP for the del.icio.us API
Name: perl-Net-Delicious
Version: 1.13
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-Delicious/

Source: http://www.cpan.org/modules/by-module/Net/Net-Delicious-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Module::Build)
BuildRequires: perl(Test::Simple) >= 0.47

%description
OOP for the del.icio.us API.

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
%doc Changes MANIFEST MANIFEST.SKIP META.yml README
%doc %{_mandir}/man3/Net::Delicious.3pm*
%doc %{_mandir}/man3/Net::Delicious::*.3pm*
%dir %{perl_vendorlib}/Net/
%{perl_vendorlib}/Net/Delicious/
%{perl_vendorlib}/Net/Delicious.pm

%changelog
* Fri Mar 07 2008 Dag Wieers <dag@wieers.com> - 1.13-1
- Updated to release 1.13.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 1.11-1
- Updated to release 1.11.

* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 1.01-1
- Updated to release 1.01.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.96-1
- Updated to release 0.96.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 0.95-1
- Updated to release 0.95.

* Thu Dec 22 2005 Dries Verachtert <dries@ulyssis.org> - 0.94-1
- Initial package.
