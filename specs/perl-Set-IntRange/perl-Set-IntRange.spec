# $Id$

# Authority: dries
# Upstream: Steffen Beyer <sb$engelschall,com>

%define real_name Set-IntRange
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

Summary: Sets of Integers
Name: perl-Set-IntRange
Version: 5.1
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Set-IntRange/

Source: http://search.cpan.org/CPAN/authors/id/S/ST/STBEY/Set-IntRange-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module allows you to work with sets of integers.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX=%{buildroot}%{_prefix}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README.txt
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Set/IntRange.pm

%changelog
* Sun Mar  6 2005 Dries Verachtert <dries@ulyssis.org> - 5.1-1
- Initial package.

