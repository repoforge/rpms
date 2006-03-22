# $Id$
# Authority: dries
# Upstream: Richard Clamp <richardc$unixbeard,net>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Module-CoreList

Summary: Get the list of modules shipped with versions of perl
Name: perl-Module-CoreList
Version: 2.02
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Module-CoreList/

Source: http://www.cpan.org/modules/by-module/Module/Module-CoreList-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl-Module-Build

%description
This module gets the list of modules shipped with versions of perl.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

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
%{_bindir}/*
%doc %{_mandir}/man1/*
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/Module/
%{perl_vendorlib}/Module/CoreList.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 2.02-1.2
- Rebuild for Fedora Core 5.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 2.02-1
- Updated to release 2.02.

* Wed Jan 05 2005 Dries Verachtert <dries@ulyssis.org> - 1.98-1
- Updated to release 1.98.

* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 1.97-1
- Updated to release 1.97.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 1.95-1
- Initial package.
