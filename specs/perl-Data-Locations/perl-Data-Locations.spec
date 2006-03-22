# $Id$
# Authority: dries
# Upstream: Steffen Beyer <sb$engelschall,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Data-Locations

Summary: Magic insertion points in your data
Name: perl-Data-Locations
Version: 5.4
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Data-Locations/

Source: http://search.cpan.org/CPAN/authors/id/S/ST/STBEY/Data-Locations-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
Magic insertion points in your data.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README.txt
%doc %{_mandir}/man3/*
%{perl_vendorarch}/Data/Locations.pm
%{perl_vendorarch}/auto/Data/Locations

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 5.4-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 5.4-1
- Initial package.
