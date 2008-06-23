# $Id$
# Authority: dries
# Upstream: Phil Harvey <phil$owl,phy,queensu,ca>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Image-ExifTool
%define real_version 1.07

Summary: Read and write meta information
Name: perl-Image-ExifTool
Version: 7.30
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Image-ExifTool/

Source: http://www.cpan.org/modules/by-module/Image/Image-ExifTool-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
ExifTool is a highly customizable Perl script for reading and writing meta
information in images.

%prep
%setup -n %{real_name}-%{version}

### Prevent 'use a' to end up as a perl(a) dependency.
%{__perl} -pi -e 's| use a | Use a |' lib/Image/ExifTool/Canon.pm

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
%doc %{_mandir}/man1/exiftool.1*
%doc %{_mandir}/man3/File::RandomAccess.3pm*
%doc %{_mandir}/man3/Image::ExifTool.3pm*
%doc %{_mandir}/man3/Image::ExifTool::*.3pm*
%{_bindir}/exiftool
%dir %{perl_vendorlib}/File/
%{perl_vendorlib}/File/RandomAccess.pm
%{perl_vendorlib}/File/RandomAccess.pod
%dir %{perl_vendorlib}/Image/
%{perl_vendorlib}/Image/ExifTool/
%{perl_vendorlib}/Image/ExifTool.pm
%{perl_vendorlib}/Image/ExifTool.pod

%changelog
* Mon Jun 23 2008 Dag Wieers <dag@wieers.com> - 7.30-1
- Updated to release 7.30.

* Mon May 05 2008 Dag Wieers <dag@wieers.com> - 7.25-1
- Updated to release 7.25.

* Fri Mar 14 2008 Dag Wieers <dag@wieers.com> - 7.21-1
- Updated to release 7.21.

* Thu Feb 28 2008 Dag Wieers <dag@wieers.com> - 7.15-2
- Remove the erroneous perl(a) dependency. (Jelmer Jellema)

* Wed Feb 20 2008 Dag Wieers <dag@wieers.com> - 7.15-1
- Updated to release 7.15.

* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 7.00-1
- Updated to release 7.00.

* Mon Jun 18 2007 Dries Verachtert <dries@ulyssis.org> - 6.90-1
- Updated to release 6.90.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 6.76-1
- Updated to release 6.76.

* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 6.66-1
- Updated to release 6.66.

* Sat Sep 23 2006 Dries Verachtert <dries@ulyssis.org> - 6.42-1
- Updated to release 6.42.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 6.36-1
- Updated to release 6.36.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 6.17-1
- Updated to release 6.17.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 6.00-1
- Updated to release 6.00.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 5.87-1
- Updated to release 5.87.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 5.77-1
- Initial package.
