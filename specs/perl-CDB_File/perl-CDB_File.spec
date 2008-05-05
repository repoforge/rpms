# $Id$
# Authority: dries
# Upstream: Matt Sergeant <msergeant$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name CDB_File

Summary: Extension for access to cdb databases
Name: perl-CDB_File
Version: 0.96
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/CDB_File/

Source: http://www.cpan.org/modules/by-module/CDB_File/CDB_File-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
CDB_File is a module which provides a Perl interface to Dan Berstein's
cdb package.

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

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES COPYRIGHT INSTALL MANIFEST META.yml README
%doc %{_mandir}/man3/CDB_File.3pm*
%{perl_vendorarch}/auto/CDB_File/
%{perl_vendorarch}/bun-x.pl
%{perl_vendorarch}/CDB_File.pm

%changelog
* Sat May 03 2008 Dag Wieers <dag@wieers.com> - 0.96-1
- Updated to release 0.96.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.95-1
- Updated to release 0.95.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.94-1
- Initial package.
