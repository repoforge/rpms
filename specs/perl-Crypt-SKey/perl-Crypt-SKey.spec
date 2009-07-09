# $Id$
# Authority: dries
# Upstream: Ken Williams <ken$mathforum,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Crypt-SKey

Summary: Perl S/Key calculator
Name: perl-Crypt-SKey
Version: 0.10
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Crypt-SKey/

Source: http://www.cpan.org/modules/by-module/Crypt/Crypt-SKey-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module contains a simple S/Key calculator (as described in RFC 1760)
implemented in Perl. It exports the function "key" by default, and may
optionally export the function "compute".

%prep
%setup -n %{real_name}-%{version}

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
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Crypt/SKey.pm

%changelog
* Thu Jul  9 2009 Christoph Maser <cmr@financial.com> - 0.10-1
- Updated to version 0.10.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.07-1.2
- Rebuild for Fedora Core 5.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 0.07-1
- Updated to release 0.07.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.06-1
- Initial package.
