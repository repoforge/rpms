# $Id$
# Authority: dries
# Upstream: Nicholas Clark <nick$talking,bollo,cx>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name PerlIO-gzip

Summary: PerlIO layer to gzip and gunzip
Name: perl-PerlIO-gzip
Version: 0.18
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/PerlIO-gzip/

Source: http://www.cpan.org/modules/by-module/PerlIO/PerlIO-gzip-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: zlib-devel
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module contains a layer for the PerlIO system to
transparently gzip/gunzip files.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/PerlIO/
%{perl_vendorarch}/PerlIO/gzip.pm
%{perl_vendorarch}/auto/PerlIO/

%changelog
* Tue Nov 14 2006 Dries Verachtert <dries@ulyssis.org> - 0.18-1
- Updated to release 0.18.

* Wed Oct 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.17-1
- Update to release 0.17.

* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 0.15-1
- Initial package.
