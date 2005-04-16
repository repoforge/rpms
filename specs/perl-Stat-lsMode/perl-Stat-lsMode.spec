# $Id$
# Authority: dries
# Upstream: Mark Jason Dominus (&#38518;&#25935;&#20462;) <mjd$plover,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Stat-lsMode

Summary: Format file modes like the ls -l command does
Name: perl-Stat-lsMode
Version: 0.50
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Stat-lsMode/

Source: http://search.cpan.org/CPAN/authors/id/M/MJ/MJD/Stat-lsMode-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module is for formatting file modes and permissions the way that
ls -l does.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Stat/lsMode.pm

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.50-1
- Initial package.
