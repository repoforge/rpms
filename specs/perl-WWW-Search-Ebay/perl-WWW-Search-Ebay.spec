# $Id$

# Authority: dries
# Upstream: Martin 'Kingpin' Thurn <mthurn$verizon,net>

%define real_name WWW-Search-Ebay
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Backend for searching www.ebay.com
Name: perl-WWW-Search-Ebay
Version: 2.205
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/WWW-Search-Ebay/

Source: http://search.cpan.org/CPAN/authors/id/M/MT/MTHURN/WWW-Search-Ebay-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This is a backend for use with the WWW::Search module for searching on Ebay.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist


%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README ChangeLog
%doc %{_mandir}/man3/*
%{perl_vendorlib}/WWW/Search/Ebay.pm
%{perl_vendorlib}/WWW/Search/Ebay/*

%changelog
* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 2.205-1
- Updated to release 2.205.

* Tue Dec 14 2004 Dries Verachtert <dries@ulyssis.org> - 2.204-1
- Updated to release 2.204.

* Wed Oct 20 2004 Dries Verachtert <dries@ulyssis.org> - 2.196-1
- Update to release 2.196.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 2.194-1
- Initial package.