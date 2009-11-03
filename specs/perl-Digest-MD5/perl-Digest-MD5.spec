# $Id$
# Authority: dag

# ExclusiveDist: el2

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Digest-MD5

Summary: Perl interface to the MD5 algorithm
Name: perl-Digest-MD5
Version: 2.39
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Digest-MD5/

Source: http://www.cpan.org/modules/by-module/Digest/Digest-MD5-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
The Digest::MD5 module allows you to use the RSA Data Security Inc.
MD5 Message Digest algorithm from within Perl programs. The algorithm
takes as input a message of arbitrary length and produces as output
a 128-bit "fingerprint" or "message digest" of the input.

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
%doc Changes README
%doc %{_mandir}/man3/*
%dir %{perl_vendorarch}/Digest/
%{perl_vendorarch}/Digest/MD5.pm
%dir %{perl_vendorarch}/auto/Digest/
%{perl_vendorarch}/auto/Digest/MD5/

%changelog
* Mon Jul  6 2009 Christoph Maser <cmr@financial.com> - 2.39-1
- Updated to version 2.39.

* Thu Jan 12 2006 Dag Wieers <dag@wieers.com> - 2.36-1
- Initial package. (using DAR)
