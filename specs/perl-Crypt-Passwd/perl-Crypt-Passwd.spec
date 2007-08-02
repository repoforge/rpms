# $Id$
# Authority: dries
# Upstream: Luis Mu&#241;oz <luismunoz$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Crypt-Passwd

Summary: Interface to the UFC-Crypt library
Name: perl-Crypt-Passwd
Version: 0.03
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Crypt-Passwd/

Source: http://search.cpan.org/CPAN/authors/id/L/LU/LUISMUNOZ/Crypt-Passwd-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl(ExtUtils::MakeMaker), perl

%description
This module provides a simple interface to the UFC-Crypt's functions
crypt() and crypt16(). This can also be an interface to other similar
libraries as the actual functions are configurable.

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
%{perl_vendorarch}/Crypt/Passwd.pm
%{perl_vendorarch}/auto/Crypt/Passwd

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.03-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.03-1
- Initial package.
