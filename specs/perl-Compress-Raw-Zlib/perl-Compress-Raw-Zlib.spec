# $Id$
# Authority: dries
# Upstream: Paul Marquess <pmqs$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Compress-Raw-Zlib

Summary: Low-Level Interface to zlib compression library
Name: perl-Compress-Raw-Zlib
Version: 2.003
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Compress-Raw-Zlib/

Source: http://search.cpan.org//CPAN/authors/id/P/PM/PMQS/Compress-Raw-Zlib-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
Low-Level Interface to zlib compression library.

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
%doc Changes README
%doc %{_mandir}/man3/Compress::Raw::Zlib*
%{perl_vendorarch}/Compress/Raw/Zlib.pm
%dir %{perl_vendorarch}/auto/Compress/
%dir %{perl_vendorarch}/auto/Compress/Raw/
%{perl_vendorarch}/auto/Compress/Raw/Zlib/

%changelog
* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 2.003-1
- Initial package.
