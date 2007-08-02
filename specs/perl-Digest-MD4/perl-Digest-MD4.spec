# $Id$
# Authority: dries
# Upstream: Mike McCauley <mikem$open,com,au>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Digest-MD4

Summary: Perl interface to the MD4 Algorithm
Name: perl-Digest-MD4
Version: 1.5
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Digest-MD4/

Source: http://search.cpan.org/CPAN/authors/id/M/MI/MIKEM/DigestMD4/Digest-MD4-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
The Digest::MD5 module allows you to use the RSA Data Security
Inc. MD5 Message Digest algorithm from within Perl programs.  The
algorithm takes as input a message of arbitrary length and produces as
output a 128-bit "fingerprint" or "message digest" of the input.
MD5 is described in RFC 1321.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorarch}/Digest/MD4.pm
%{perl_vendorarch}/auto/Digest/MD4

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.5-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.5-1
- Initial package.
