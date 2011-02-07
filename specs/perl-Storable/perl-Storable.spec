# $Id$
# Authority: dag
# Upstream: Abhijit Menon-Sen <ams$wiw,org>

### Upstream perl package now provides perl(Storable)
# ExclusiveDist: el2

### EL2 ships with perl-Storable-0.6.11-6
%{?el2:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Storable

Summary: Perl module for persistence for Perl data structures
Name: perl-Storable
Version: 2.25
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Storable/

Source: http://search.cpan.org/CPAN/authors/id/A/AM/AMS/Storable-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl

%description
perl-Storable is a Perl module for persistence for Perl data structures.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;
find %{buildroot}%{_libdir} -name "*.so" -exec chmod u+w {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog MANIFEST META.yml README
%doc %{_mandir}/man3/Storable.3pm*
%{perl_vendorarch}/auto/Storable/
%{perl_vendorarch}/Storable.pm

%changelog
* Mon Feb  7 2011 Christoph Maser <cmaser@gmx.de> - 2.25-1
- Updated to version 2.25.

* Sat Aug 29 2009 Christoph Maser <cmr@financial.com> - 2.21-1
- Updated to version 2.21.

* Thu Jun 18 2009 Christoph Maser <cmr@financial.com> - 2.20-1
- Updated to version 2.20.

* Sat Nov 24 2007 Dag Wieers <dag@wieers.com> - 2.18-1
- Updated to release 2.18.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 2.17-1
- Updated to release 2.17.

* Sun Aug 05 2007 Dag Wieers <dag@wieers.com> - 2.16-1
- Updated to release 2.16.

* Sun Nov 13 2005 Dries Verachtert <dries@ulyssis.org> - 2.15-1
- Updated to release 2.15.

* Fri Mar 19 2004 Matthias Saou <http://freshrpms.net/> 2.11-1
- Initial RPM release.

