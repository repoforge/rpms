# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Compress-Zlib

Summary: Compress-Zlib module for perl
Name: perl-Compress-Zlib
Version: 1.41
Release: 1.2
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Compress-Zlib/

Source: http://www.cpan.org/modules/by-module/Compress/Compress-Zlib-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 0:5.004, zlib-devel >= 1.0.2
Requires: perl >= 0:5.004, zlib >= 1.0.2

%description
Compress-Zlib module for perl

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}/auto/*{,/*{,/*}}/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ANNOUNCE README
%doc %{_mandir}/man?/*
%{perl_vendorarch}/Compress/
%{perl_vendorarch}/auto/Compress/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.41-1.2
- Rebuild for Fedora Core 5.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.41-1
- Updated to release 1.41.

* Mon Sep 05 2005 Dag Wieers <dag@wieers.com> - 1.37-1
- Updated to release 1.37.

* Thu Mar 10 2005 Dag Wieers <dag@wieers.com> - 1.34-1
- Updated to release 1.34.

* Thu Mar 18 2004 Dag Wieers <dag@wieers.com> - 1.33-0
- Updated to release 1.33.

* Mon Jul 14 2003 Dag Wieers <dag@wieers.com> - 1.22-0
- Updated to release 1.22.

* Sun Jan 26 2003 Dag Wieers <dag@wieers.com>
- Initial package. (using DAR)
