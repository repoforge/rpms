# $Id$
# Authority: dries
# Upstream: Graciliano Monteiro Passos <gmpassos$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Geo-IPfree

Summary: Look up the country of an ipaddress.
Name: perl-Geo-IPfree
Version: 0.2
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Geo-IPfree/

Source: http://search.cpan.org/CPAN/authors/id/G/GM/GMPASSOS/Geo-IPfree-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
With this module, you can lookup the country of an ipaddress.

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
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Geo/IPfree.pm
%{perl_vendorlib}/Geo/*.pl
%{perl_vendorlib}/Geo/ipscountry.dat

%changelog
* Sun Dec 11 2005 Dries Verachtert <dries@ulyssis.org> - 0.2-1
- Initial package.
