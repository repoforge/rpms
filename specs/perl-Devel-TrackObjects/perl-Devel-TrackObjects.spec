# $Id$
# Authority: dries
# Upstream: Steffen Ullrich <Steffen_Ullrich$genua,de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Devel-TrackObjects

Summary: Track usage of objects
Name: perl-Devel-TrackObjects
Version: 0.3
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Devel-TrackObjects/

Source: http://www.cpan.org/modules/by-module/Devel/Devel-TrackObjects-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Track usage of objects.

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
%doc COPYRIGHT Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Devel::TrackObjects.3pm*
%dir %{perl_vendorlib}/Devel/
#%{perl_vendorlib}/Devel/TrackObjects/
%{perl_vendorlib}/Devel/TrackObjects.pm

%changelog
* Sun Feb 24 2008 Dag Wieers <dag@wieers.com> - 0.3-1
- Updated to release 0.3.

* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 0.2-1
- Updated to release 0.2.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.1-1
- Initial package.
