# $Id$

# Authority: dries
# Upstream: Andy Wardley <cpan$wardley,org>

%define real_name Math-Bezier
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Solution of Bezier Curves
Name: perl-Math-Bezier
Version: 0.01
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-Bezier/

Source: http://search.cpan.org/CPAN/authors/id/A/AB/ABW/Math-Bezier-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module implements the algorithm for the solution of Bezier
curves as presented by Robert D. Miller in Graphics Gems V,
"Quick and Simple Bezier Curve Drawing".

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
%doc README Changes
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Math/Bezier.pm
%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Fri Dec 10 2004 Dries Verachtert <dries@ulyssis.org> - 0.01-1
- Initial package.
