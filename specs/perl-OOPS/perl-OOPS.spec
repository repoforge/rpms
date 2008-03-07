# $Id$
# Authority: dag
# Upstream: David Muir Sharnoff <muir$idiom,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name OOPS

Summary: Object Oriented Persistent Store
Name: perl-OOPS
Version: 0.2004
Release: 1
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/OOPS/

Source: http://www.cpan.org/authors/id/M/MU/MUIR/modules/OOPS-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

### Provides required by package itself
Provides: perl(OOPS::DBOdebug)

%description
Object Oriented Persistent Store.

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
%doc CHANGELOG COPYING MANIFEST META.yml README
%doc %{_mandir}/man3/OOPS.3pm*
%doc %{_mandir}/man3/OOPS::*.3pm*
%{perl_vendorlib}/OOPS/
%{perl_vendorlib}/OOPS.pm
%{perl_vendorlib}/OOPS.pod

%changelog
* Fri Mar 07 2008 Dag Wieers <dag@wieers.com> - 0.2004-1
- Updated to release 0.2004.

* Sat Nov 24 2007 Dag Wieers <dag@wieers.com> - 0.2003-2
- Added selfcontained provides.

* Fri Nov 23 2007 Dag Wieers <dag@wieers.com> - 0.2003-1
- Initial package. (using DAR)
