# $Id$
# Authority: dag
# Upstream: Gisle Aas <gisle$ActiveState,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name MIME-Base64

Summary: Perl module for encoding and decoding of base64 strings
Name: perl-MIME-Base64
Version: 3.10
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/MIME-Base64/

Source: http://search.cpan.org/CPAN/authors/id/G/GA/GAAS/MIME-Base64-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
perl-MIME-Base64 is a Perl module for encoding and decoding of base64 strings.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}" test

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST README
%doc %{_mandir}/man3/MIME::Base64.3pm*
%doc %{_mandir}/man3/MIME::QuotedPrint.3pm*
%dir %{perl_vendorarch}/MIME/
%{perl_vendorarch}/MIME/Base64.pm
%{perl_vendorarch}/MIME/QuotedPrint.pm
%dir %{perl_vendorarch}/auto/MIME/
%{perl_vendorarch}/auto/MIME/Base64/

%changelog
* Mon Nov 15 2010 David Hrbáč <david@hrbac.cz> - 3.10-1
- new upstream release

* Wed Feb  3 2010 Christoph Maser <cmr@financial.com> - 3.09-1
- Updated to version 3.09.

* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 3.08-1
- Updated to version 3.08.

* Sun Oct 07 2007 Dag Wieers <dag@wieers.com> - 3.07-1
- Initial package. (using DAR)
