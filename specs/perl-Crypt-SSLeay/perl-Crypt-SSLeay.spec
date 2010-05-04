# $Id$
# Authority: dag
# Upstream: David Landgren

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Crypt-SSLeay

Summary: OpenSSL support for LWP
Name: perl-Crypt-SSLeay
Version: 0.57
Release: 3%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Crypt-SSLeay/

Source: http://www.cpan.org/modules/by-module/Crypt/Crypt-SSLeay-%{version}.tar.gz
Patch0: perl-Crypt-SSLeay-0.55-cryptdef.patch
Patch1: perl-Crypt-SSLeay-0.55-lib64.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

Provides: perl-Business-OnlinePayment-alternative = 3.00
Provides: perl-Net-Nessus-XMLRPC-alternative = 0.20

%description
OpenSSL support for LWP.

%prep
%setup -n %{real_name}-%{version}
%patch0 -p1 -b .cryptdef
#patch1 -p1 -b .lib64

%build
if pkg-config openssl ; then
  export INC="$CFLAGS $(pkg-config --cflags-only-I openssl)"
  export LDFLAGS="$LDFLAGS $(pkg-config --libs-only-L openssl)"
fi
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}" \
    INC="$INC" \
    LDFLAGS="$LDFLAGS" </dev/null
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
%doc Changes MANIFEST MANIFEST.SKIP META.yml README TODO
%doc %{_mandir}/man3/Crypt::SSLeay.3pm*
%doc %{_mandir}/man3/Net::SSL.3pm*
%dir %{perl_vendorarch}/Crypt/
%{perl_vendorarch}/Crypt/SSLeay/
%{perl_vendorarch}/Crypt/SSLeay.pm
%dir %{perl_vendorarch}/Net/
%{perl_vendorarch}/Net/SSL.pm
%dir %{perl_vendorarch}/auto/Crypt/
%{perl_vendorarch}/auto/Crypt/SSLeay/

%changelog
* Tue May 04 2010 Steve Huff <shuff@vecna.org> - 0.57-3
- Satisfies an alternative dependency for perl-Net-Nessus-XMLRPC.

* Tue Nov 17 2009 Steve Huff <shuff@vecna.org> - 0.57-2
- Satisfies an alternative dependency for perl-Business-OnlinePayment.

* Thu Nov 08 2007 Dag Wieers <dag@wieers.com> - 0.57-1
- Updated to release 0.57.

* Sat Aug 04 2007 Dag Wieers <dag@wieers.com> - 0.56-1
- Initial package. (using DAR)
