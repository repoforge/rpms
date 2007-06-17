# $Id$

# Authority: dries
# Upstream: Uri Guttman <uri$sysarch,com>


%define real_name File-Slurp
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Efficient reading and writing of complete files
Name: perl-File-Slurp
Version: 9999.12
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/File-Slurp/

Source: http://www.cpan.org/modules/by-module/File/File-Slurp-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
This module provides subroutines to read or write entire files with a
simple call.  It also has a subroutine for reading the list of filenames
in a directory.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/File/Slurp.pm

%changelog
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
