# $Id$
# Authority: dag
# Upstream: Paul Marquess <pmqs$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Compress-Zlib

Summary: Perl module to interface to zlib compression library
Name: perl-Compress-Zlib
Version: 2.009
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Compress-Zlib/

Source: http://www.cpan.org/modules/by-module/Compress/Compress-Zlib-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.004
BuildRequires: perl(Compress::Raw::Zlib) >= 2.005
BuildRequires: perl(IO::Compress::Base) >= 2.005
BuildRequires: perl(IO::Compress::Gzip) >= 2.005
BuildRequires: perl(IO::Compress::Gzip::Constants) >= 2.005
BuildRequires: perl(IO::Uncompress::Base) >= 2.005
BuildRequires: perl(IO::Uncompress::Gunzip) >= 2.005
BuildRequires: perl(ExtUtils::MakeMaker)

Requires: perl >= 0:5.004

%description
perl-Compress-Zlib is a Perl module to interface to zlib compression library.

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

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README examples/
%doc %{_mandir}/man3/Compress::Zlib.3pm*
%dir %{perl_vendorlib}/Compress/
#%{perl_vendorlib}/Compress/Zlib/
%{perl_vendorlib}/Compress/Zlib.pm
%{perl_vendorlib}/auto/Compress/Zlib/

%changelog
* Sat May 03 2008 Dag Wieers <dag@wieers.com> - 2.009-1
- Updated to release 2.009.

* Tue Nov 13 2007 Dag Wieers <dag@wieers.com> - 2.008-1
- Updated to release 2.008.

* Wed Nov 07 2007 Dag Wieers <dag@wieers.com> - 2.007-1
- Updated to release 2.007.

* Wed Aug 08 2007 Dag Wieers <dag@wieers.com> - 2.005-1
- Updated to release 2.005.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 1.42-1
- Updated to release 1.42.

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
