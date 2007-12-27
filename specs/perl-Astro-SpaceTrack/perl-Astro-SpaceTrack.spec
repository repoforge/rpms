# $Id$
# Authority: dries
# Upstream: Tom Wyant <wyant$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Astro-SpaceTrack

Summary: Downloads orbital elements from the Space Track web site
Name: perl-Astro-SpaceTrack
Version: 0.031
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Astro-SpaceTrack/

Source: http://www.cpan.org/modules/by-module/Astro/Astro-SpaceTrack-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Tk)

%description
This library logs in to the Space Track web site and downloads orbital
elements. It does nothing that you can't do with a web browser, but it
does give you a way to automate things.

Note that you are required to register for a username and password before
making use of the Space Track web site.

FEDERAL LAW FORBIDS THE REDISTRIBUTION OF DOWNLOADED ORBITAL ELEMENTS
TO THIRD PARTIES WITHOUT PRIOR PERMISSION.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL -y INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
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
%doc Changes MANIFEST META.yml README eg/
%doc %{_mandir}/man1/SpaceTrack.1*
%doc %{_mandir}/man1/SpaceTrackTk.1*
%doc %{_mandir}/man3/Astro::SpaceTrack.3pm*
%{_bindir}/SpaceTrack
%{_bindir}/SpaceTrackTk
%dir %{perl_vendorlib}/Astro/
%{perl_vendorlib}/Astro/SpaceTrack/
%{perl_vendorlib}/Astro/SpaceTrack.pm

%changelog
* Thu Dec 27 2007 Dag Wieers <dag@wieers.com> - 0.031-1
- Updated to release 0.031.

* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 0.030-1
- Updated to release 0.030.

* Mon Jun 18 2007 Dries Verachtert <dries@ulyssis.org> - 0.028-1
- Updated to release 0.028.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.027-1
- Updated to release 0.027.

* Tue Nov 14 2006 Dries Verachtert <dries@ulyssis.org> - 0.026-1
- Updated to release 0.026.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.024-1
- Updated to release 0.024.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 0.018-1
- Updated to release 0.018.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.016-1
- Updated to release 0.016.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.013-1
- Initial package.
