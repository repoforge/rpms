# $Id$
# Authority: dries
# Upstream: chromatic <chromatic$wgz,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name P5NCI

Summary: Extension for loading shared libraries and their functions
Name: perl-P5NCI
Version: 0.31
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/P5NCI/

Source: http://search.cpan.org/CPAN/authors/id/C/CH/CHROMATIC/P5NCI-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl-Module-Build

%description
A perl extension for loading shared libraries and their functions.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_vendorarch}/auto/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/P5NCI.3pm*
%doc %{_mandir}/man3/P5NCI::*3pm*
%{perl_vendorarch}/P5NCI.pm
%{perl_vendorarch}/P5NCI/
%{perl_vendorarch}/auto/P5NCI/

%changelog
* Sun May 24 2009 Fabian Arrotin <fabian.arrotin@arrfab.net> - 0.31-1
- Added a missing BuildRequires: perl-Module-Build
* Sat May 23 2009 Dries Verachtert <dries@ulyssis.org> - 0.31-1
- Initial package.
