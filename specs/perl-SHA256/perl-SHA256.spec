# $Id$
# Authority: dries
# Upstream: Rafael R. Sevilla <sevillar$team,ph,inter,net>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name SHA256

Summary: Implements the SHA-256/384/512 hash algorithm
Name: perl-SHA256
Version: 0.01b
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/SHA256/

Source: http://search.cpan.org/CPAN/authors/id/D/DI/DIDO/SHA256-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
This module implements the SHA-256/384/512 hash algorithm developed by
NIST.

%prep
%setup -n %{real_name}-0.01

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
%doc README
%doc %{_mandir}/man3/*
%{perl_vendorarch}/Digest/SHA256.p*
%{perl_vendorarch}/Digest/sha256.pod
#%{perl_vendorarch}/Digest/SHA256/
%{perl_vendorarch}/auto/Digest/SHA256/

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.01b-1.2
- Rebuild for Fedora Core 5.

* Wed Dec 21 2005 Dries Verachtert <dries@ulyssis.org> - 0.01b-1
- Initial package.
