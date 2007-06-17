# $Id$
# Authority: dries
# Upstream: Eric Estabrooks <eric$urbanrage,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Crypt-HCE_MD5

Summary: One way hash chaining encryption using MD5
Name: perl-Crypt-HCE_MD5
Version: 0.70
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Crypt-HCE_MD5/

Source: http://search.cpan.org/CPAN/authors/id/E/EE/EESTABROO/Crypt-HCE_MD5-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker), perl

%description
This module implements a chaining block cipher using a one
way hash.  This method of encryption is the same that is
used by radius (RFC2138) and is also described in Applied
Cryptography.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Crypt/HCE_MD5.pm
%{perl_vendorlib}/auto/Crypt/HCE_MD5

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.70-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.70-1
- Initial package.
