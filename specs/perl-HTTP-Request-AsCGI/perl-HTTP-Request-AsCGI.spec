# $Id$
# Authority: dries
# Upstream: Marcus Ramberg <mramberg$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTTP-Request-AsCGI

Summary: Setup a CGI enviroment from a HTTP::Request
Name: perl-HTTP-Request-AsCGI
Version: 0.9
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTTP-Request-AsCGI/

Source: http://www.cpan.org/modules/by-module/HTTP/HTTP-Request-AsCGI-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Provides a convinient way of setting up an CGI enviroment from a HTTP::Request.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/HTTP/Request/AsCGI.pm

%changelog
* Sun Jul  5 2009 Christoph Maser <cmr@financial.com> - 0.9-1
- Updated to version 0.9.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.5-1
- Updated to release 0.5.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.3-1.2
- Rebuild for Fedora Core 5.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 0.3-1
- Updated to release 0.3.

* Thu Dec 15 2005 Dries Verachtert <dries@ulyssis.org> - 0.2-1
- Initial package.
