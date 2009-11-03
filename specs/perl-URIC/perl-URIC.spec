# $Id$
# Authority: dag
# Upstream: Loic Dachary <loic$senga,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name URIC
%define real_version 4.08

Summary: Perl module that implements URIC (analyse and transform URIs)
Name: perl-URIC
Version: 2.02
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/URIC/

Source: http://www.cpan.org/authors/id/L/LD/LDACHARY/URIC-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
perl-URIC is a Perl module that implements URIC.

URIC is a library that analyses URIs and transform them. It is designed to
be fast and occupy as few memory as possible. The basic usage of this
library is to transform an URI into a structure with one field for each
component of the URI and vice versa. It is available as a C library and
as a Perl library.

This package contains the following Perl module:

    URI2::Heuristic

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc MANIFEST NOTES README
%doc %{_mandir}/man3/URI2::Heuristic.3pm*
%{perl_vendorarch}/URIC.pm
%{perl_vendorarch}/auto/URIC/

%changelog
* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 2.02-1
- Initial package. (using DAR)
