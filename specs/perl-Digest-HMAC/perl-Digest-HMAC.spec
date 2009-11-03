# $Id$
# Authority: dag

# ExclusiveDist: rh6 el2 rh7 rh8

%{?dtag: %{expand: %%define %dtag 1}}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Digest-HMAC

Summary: Digest-HMAC Perl module
Name: perl-Digest-HMAC
Version: 1.01
Release: 2.2%{?dist}
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Digest-HMAC/

Source: http://www.cpan.org/modules/by-module/Digest/Digest-HMAC-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.00503
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Digest::SHA1)
%{?rh7:BuildRequires: perl(Digest::MD5)}

Requires: perl >= 0:5.00503
Requires: perl(Digest::SHA1)
%{?rh7:Requires: perl(Digest::MD5)}

%description
HMAC is used for message integrity checks between two parties that
share a secret key, and works in combination with some other Digest
algorithm, usually MD5 or SHA-1. The HMAC mechanism is described in
RFC 2104.

HMAC follow the common Digest:: interface, but the constructor takes
the secret key and the name of some other simple Digest:: as argument.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}
#{__make} %{?_smp_mflags} test

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README rfc2104.txt
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/Digest/
%{perl_vendorlib}/Digest/HMAC.pm
%{perl_vendorlib}/Digest/HMAC_*.pm

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.01-2.2
- Rebuild for Fedora Core 5.

* Fri Jan 13 2006 Dag Wieers <dag@wieers.com> - 1.01-2
- Cosmetic cleanup.

* Sun Jan 26 2003 Dag Wieers <dag@wieers.com> - 1.01-1
- Initial package. (using DAR)
