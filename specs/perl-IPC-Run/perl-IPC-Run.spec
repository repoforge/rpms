# $Id$
# Authority: dries
# Upstream: Barrie Slaymaker <barries$slaysys,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name IPC-Run

Summary: IPC functions
Name: perl-IPC-Run
Version: 0.80
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/IPC-Run/

Source: http://search.cpan.org/CPAN/authors/id/R/RS/RSOD/IPC-Run-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module provides various IPC functionalities.

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
%{__rm} -f %{buildroot}%{perl_vendorlib}/IPC/Run/Win32*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes
%doc %{_mandir}/man3/*
%{perl_vendorlib}/IPC/Run.pm
%{perl_vendorlib}/IPC/Run/*

%changelog
* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 0.80-1
- Updated to release 0.80.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.79-1.2
- Rebuild for Fedora Core 5.

* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 0.79-1
- Updated to release 0.79.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.78-1
- Initial package.
