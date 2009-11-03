# $Id$
# Authority: dries
# Upstream: Andrew V. Makarow <makarow$mail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Sys-Manage

Summary: Systems management command volley
Name: perl-Sys-Manage
Version: 0.59
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Sys-Manage/

Source: http://www.cpan.org/modules/by-module/Sys/Sys-Manage-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Systems management command volley.

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
%doc MANIFEST META.yml readme examples/
%doc %{_mandir}/man3/Sys::Manage.3pm.gz
%doc %{_mandir}/man3/Sys::Manage::*.3pm*
%dir %{perl_vendorlib}/Sys/
%{perl_vendorlib}/Sys/Manage/
#%{perl_vendorlib}/Sys/Manage.pm
%{perl_vendorlib}/Sys/Manage.pod

%changelog
* Fri Mar 07 2008 Dag Wieers <dag@wieers.com> - 0.59-1
- Updated to release 0.59.

* Fri Jan 04 2008 Dag Wieers <dag@wieers.com> - 0.58-1
- Updated to release 0.58.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 0.57-1
- Updated to release 0.57.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.56-1
- Updated to release 0.56.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.54-1
- Updated to release 0.54.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 0.53-1
- Updated to release 0.53.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.52-1
- Updated to release 0.52.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 0.51-1
- Updated to release 0.51.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.50-1
- Initial package.
