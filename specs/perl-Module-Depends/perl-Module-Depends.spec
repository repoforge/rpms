# $Id$
# Authority: dries
# Upstream: Richard Clamp <richardc$unixbeard,net>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Module-Depends

Summary: Identify the dependencies of a distribution
Name: perl-Module-Depends
Version: 0.12
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Module-Depends/

Source: http://www.cpan.org/modules/by-module/Module/Module-Depends-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Identify the dependencies of a distribution.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
		%{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/Module/
%{perl_vendorlib}/Module/Depends.pm
%{perl_vendorlib}/Module/Depends/

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.12-1
- Updated to release 0.12.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.10-1.2
- Rebuild for Fedora Core 5.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 0.10-1
- Updated to release 0.10.

* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 0.07-1
- Updated to release 0.07.

* Fri Dec 10 2004 Dries Verachtert <dries@ulyssis.org> - 0.05-1
- Initial package.
