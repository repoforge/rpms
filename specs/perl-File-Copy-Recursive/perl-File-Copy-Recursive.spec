# $Id$
# Authority: dries
# Upstream: Daniel Muey <dmuey$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name File-Copy-Recursive

Summary: Copy files recusively
Name: perl-File-Copy-Recursive
Version: 0.31
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/File-Copy-Recursive/

Source: http://search.cpan.org/CPAN/authors/id/D/DM/DMUEY/File-Copy-Recursive-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module has 3 functions, one to copy files only, one to copy directories
only and one to do either depending on the argument's type.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/File/Copy/Recursive.pm

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.31-1
- Updated to release 0.31.

* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 0.30-1
- Updated to release 0.30.

* Tue Nov 14 2006 Dries Verachtert <dries@ulyssis.org> - 0.29-1
- Updated to release 0.29.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.28-1
- Updated to release 0.28.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 0.23-1
- Updated to release 0.23.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.19-1
- Updated to release 0.19.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.16-1.2
- Rebuild for Fedora Core 5.

* Thu Dec 15 2005 Dries Verachtert <dries@ulyssis.org> - 0.16-1
- Initial package.
