# $Id$

# Authority: dries
# Upstream: Barrie Slaymaker <barries$slaysys,com>

%define real_name IPC-Run
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: IPC functions
Name: perl-IPC-Run
Version: 0.79
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/IPC-Run/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/R/RB/RBS/IPC-Run-%{version}.tar.gz
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
* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 0.79-1
- Updated to release 0.79.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.78-1
- Initial package.
