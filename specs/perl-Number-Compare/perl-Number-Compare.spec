# $Id$

# Authority: dries
# Upstream: Richard Clamp <richardc$unixbeard,net>

%define real_name Number-Compare
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Numeric comparisons
Name: perl-Number-Compare
Version: 0.01
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Number-Compare/

Source: http://search.cpan.org/CPAN/authors/id/R/RC/RCLAMP/Number-Compare-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module contains functions for numeric comparisons.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir=%{buildroot}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Number/Compare.pm
%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Fri Dec 10 2004 Dries Verachtert <dries@ulyssis.org> - 0.01-1
- Initial package.
