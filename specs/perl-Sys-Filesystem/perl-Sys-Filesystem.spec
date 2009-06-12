# $Id$
# Authority: dries
# Upstream: Nicola Worthington <nicolaw$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Sys-Filesystem

Summary: Interface to filesystem names and their properties
Name: perl-Sys-Filesystem
Version: 1.23
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Sys-Filesystem/

Source: http://www.cpan.org/modules/by-module/Sys/Sys-Filesystem-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Module::Build)

%description
Sys::Filesystem is intended to be a portable interface to list and
query filesystem names and their properties.

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
%{__rm} -f %{buildroot}%{perl_vendorlib}/Sys/Filesystem/Mswin32.pm

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/Sys::Filesystem*
%{perl_vendorlib}/Sys/Filesystem.pm
%{perl_vendorlib}/Sys/Filesystem/

%changelog
* Fri Jun 12 2009 Christoph Maser <cmr@financial.com> - 1.23-1
- Updated to version 1.23.

* Sun Dec 07 2007 Dries Verachtert <dries@ulyssis.org> - 1.22-1
- Updated to release 1.22.
- Fixed Win32::DriveInfo requirement, thanks to Noah Romer.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 1.21-1
- Updated to release 1.21.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 1.18-1
- Updated to release 1.18.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.16-1
- Initial package.
