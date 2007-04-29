# $Id$
# Authority: dries
# Upstream: Sebastian Riedel <sri$oook,de>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTTP-Body

Summary: HTTP Body parser
Name: perl-HTTP-Body
Version: 0.9
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTTP-Body/

Source: http://search.cpan.org/CPAN/authors/id/A/AG/AGRUNDMA/HTTP-Body-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module contains a HTTP body parser.

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
%{perl_vendorlib}/HTTP/Body.pm
%{perl_vendorlib}/HTTP/Body/

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.9-1
- Updated to release 0.9.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.6-1.2
- Rebuild for Fedora Core 5.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 0.6-1
- Updated to release 0.6.

* Thu Dec 15 2005 Dries Verachtert <dries@ulyssis.org> - 0.5-1
- Initial package.
