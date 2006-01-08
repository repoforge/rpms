# $Id$
# Authority: dries
# Upstream: Paul Timmins <paul$timmins,net>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Geo-Coordinates-VandH

Summary: Convert and Manipulate telco V and H coordinates.
Name: perl-Geo-Coordinates-VandH
Version: 1.11
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Geo-Coordinates-VandH/

Source: http://search.cpan.org/CPAN/authors/id/P/PT/PTIMMINS/Geo-Coordinates-VandH-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
With this module, you can convert and Manipulate telco V and H coordinates.

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
%doc CHANGES README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Geo/Coordinates/VandH.pm
%{perl_vendorlib}/Geo/Coordinates/vhtest.pl

%changelog
* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 1.11-1
- Updated to release 1.11.

* Sun Dec 11 2005 Dries Verachtert <dries@ulyssis.org> - 1.10-1
- Initial package.
