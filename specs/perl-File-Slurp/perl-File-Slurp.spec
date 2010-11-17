# $Id$
# Authority: dries
# Upstream: Uri Guttman <uri$stemsystems,com>

### EL6 ships with perl-File-Slurp-9999.13-7.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name File-Slurp

Summary: Efficient reading and writing of complete files
Name: perl-File-Slurp
Version: 9999.13
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/File-Slurp/

Source: http://www.cpan.org/modules/by-module/File/File-Slurp-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module provides subroutines to read or write entire files with a
simple call.  It also has a subroutine for reading the list of filenames
in a directory.

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
%doc %{_mandir}/man3/File::Slurp.3pm*
%dir %{perl_vendorlib}/File/
#%{perl_vendorlib}/File/Slurp/
%{perl_vendorlib}/File/Slurp.pm

%changelog
* Sat Jan 26 2008 Dag Wieers <dag@wieers.com> - 9999.13-1
- Updated to release 9999.13.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 9999.12-1
- Updated to release 9999.12.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 9999.09-1
- Updated to release 9999.09.

* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 9999.07-1
- Updated to release 9999.07.

* Sat Jan 01 2005 Dries Verachtert <dries@ulyssis.org> - 9999.06-2
- Fixed the license tag (Thanks to David Necas !)

* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 9999.06-1
- Updated to release 9999.06.

* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 9999.04
- Initial package.
