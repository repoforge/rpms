# $Id$
# Authority: dag

# ExcludeDist: el4

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Digest-SHA1

Summary: Digest-SHA1 Perl module
Name: perl-Digest-SHA1
Version: 2.12
Release: 1
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Digest-SHA1/

Source: http://www.cpan.org/modules/by-module/Digest/Digest-SHA1-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 0:5.00503
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl >= 0:5.00503

%description
The Digest::SHA1 module allows you to use the NIST SHA-1 message
digest algorithm from within Perl programs. The algorithm takes as
input a message of arbitrary length and produces as output a 160-bit
"fingerprint" or "message digest" of the input.

The Digest::SHA1 module provide a procedural interface for simple use,
as well as an object oriented interface that can handle messages of
arbitrary length and which can read files directly.

A binary digest will be 20 bytes long. A hex digest will be 40
characters long. A base64 digest will be 27 characters long.

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
%doc Changes MANIFEST README fip180-1*
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/Digest/
%{perl_vendorarch}/Digest/SHA1.pm
%dir %{perl_vendorarch}/auto/Digest/
%{perl_vendorarch}/auto/Digest/SHA1/

%changelog
* Mon Jul  6 2009 Christoph Maser <cmr@financial.com> - 2.12-1
- Updated to version 2.12.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 2.11-1
- Updated to release 2.11.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.10-1.2
- Rebuild for Fedora Core 5.

* Fri Mar 18 2005 Dag Wieers <dag@wieers.com> - 2.10-1
- Cosmetic cleanup.

* Thu Mar 18 2004 Dag Wieers <dag@wieers.com> - 2.07-1
- Updated to release 2.07.

* Sun Jan 26 2003 Dag Wieers <dag@wieers.com> - 2.03-0
- Initial package. (using DAR)
