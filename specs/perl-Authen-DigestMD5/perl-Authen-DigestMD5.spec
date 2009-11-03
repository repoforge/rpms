# $Id$
# Authority: dag
# Upstream: Salvador Fandiño García <salva$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Authen-DigestMD5

Summary: SASL DIGEST-MD5 authentication (RFC2831) perl module
Name: perl-Authen-DigestMD5
Version: 0.04
Release: 2%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Authen-DigestMD5/

Source: http://www.cpan.org/modules/by-module/Authen/Authen-DigestMD5-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl

%description
Authen-DigestMD5 is a perl module that implements SASL DIGEST-MD5
authentication (RFC2831).

%prep
%setup -n %{real_name}-%{version}

### Fix wrong script interpreter, and set permissions to avoid extra deps
%{__perl} -i.orig -e 's|/usr/local/bin/perl|%{__perl}|' digest-md5-auth.pl
%{__chmod} 0644 digest-md5-auth.pl

### Fix character encoding
%{__mv} DigestMD5.pm DigestMD5.pm.not-utf8
/usr/bin/iconv -f iso8859-1 -t utf8 -o DigestMD5.pm DigestMD5.pm.not-utf8

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Authen::DigestMD5.3pm*
%dir %{perl_vendorlib}/Authen/
%{perl_vendorlib}/Authen/digest-md5-auth.pl
%{perl_vendorlib}/Authen/DigestMD5.pm

%changelog
* Sun May 27 2007 Dag Wieers <dag@wieers.com> - 0.04-2
- Fix dependencies to /usr/local/perl and perl(OpenLDAP).

* Sun Apr 29 2007 Dag Wieers <dag@wieers.com> - 0.04-1
- Initial package. (using DAR)
