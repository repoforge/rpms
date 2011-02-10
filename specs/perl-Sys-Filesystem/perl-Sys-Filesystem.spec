# $Id$
# Authority: dries
# Upstream: Jens Rehsack <rehsack@cpan.org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Sys-Filesystem

Summary: Interface to filesystem names and their properties
Name: perl-Sys-Filesystem
Version: 1.30
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Sys-Filesystem/

Source: http://search.cpan.org/CPAN/authors/id/R/RE/REHSACK/Sys-Filesystem-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl(Carp)
BuildRequires: perl(FindBin)
BuildRequires: perl(IO)
BuildRequires: perl(Module::Build) >= 0.36
BuildRequires: perl(Module::Pluggable) >= 3.9
BuildRequires: perl(Params::Util) >= 1.00
BuildRequires: perl(Test::More) >= 0.9
BuildRequires: perl >= 5.008
Requires: perl(Carp)
Requires: perl(FindBin)
Requires: perl(IO)
Requires: perl(Module::Pluggable) >= 3.9
Requires: perl(Params::Util) >= 1.00
Requires: perl >= 5.008

### remove autoreq Perl dependencies
%filter_from_requires /^perl*/d
%filter_setup


%description
Sys::Filesystem is intended to be a portable interface to list and
query filesystem names and their properties.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Build.PL --installdirs vendor --destdir %{buildroot}
./Build

%install
%{__rm} -rf %{buildroot}
./Build pure_install

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
* Thu Feb 10 2011 Christoph Maser <cmaser@gmx.de> - 1.30-1
- Updated to version 1.30.

* Wed Dec  9 2009 Christoph Maser <cmr@financial.com> - 1.25-1
- Updated to version 1.25.

* Thu Oct 22 2009 Christoph Maser <cmr@financial.com> - 1.24-1
- Updated to version 1.24.

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
