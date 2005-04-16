# $Id$
# Authority: dries
# Upstream: Dave Paris <a-mused$pobox,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Crypt-Blowfish

Summary: Perl Blowfish encryption module
Name: perl-Crypt-Blowfish
Version: 2.09
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Crypt-Blowfish/

Source: http://search.cpan.org/CPAN/authors/id/D/DP/DPARIS/Crypt-Blowfish-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
This is Crypt::Blowfish version, an XS-based implementation of the
Blowfish cryptography algorithm designed by Bruce Schneier.  It's designed
to take full advantage of Crypt::CBC when desired.  Blowfish keys may be
up to 448 bits (56 bytes) long.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorarch}/Crypt/Blowfish.pm
%{perl_vendorarch}/auto/Crypt/Blowfish

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 2.09-1
- Initial package.
