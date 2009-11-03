# $Id$
# Authority: dag
# Upstream: Chip Turner <cturner$pattern,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name RPM-Specfile

Summary: Perl module for creating rpm packages of other perl modules
Name: perl-RPM-Specfile
Version: 1.51
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/RPM-Specfile/

Source: http://www.cpan.org/modules/by-module/RPM/RPM-Specfile-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl

%description
Simple module for creation of RPM Spec files.  Used by cpanflute2 to turn CPAN
tarballs into RPM modules.
See the included script cpanflute2 for usage; documentation coming soon.

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/RPM::Specfile.3pm*
%{_bindir}/cpanflute2
%{_bindir}/cpanflute2-old
%dir %{perl_vendorlib}/RPM/
%{perl_vendorlib}/RPM/Specfile.pm

%changelog
* Sun Aug 05 2007 Dag Wieers <dag@wieers.com> - 1.51-1
- Updated to release 1.51.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.19-1
- Updated to release 1.19.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 1.13-1
- Update to 1.13.
- Rebuild for Fedora Core 1.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Thu Mar  6 2003 Matthias Saou <http://freshrpms.net/>
- Stole the package, minor cosmetic changes :-)

* Sun Feb  9 2003 Ville Skyttä <ville.skytta at iki.fi> 1.11-1.fedora.1
- First Fedora release.
