# $Id$
# Authority: dries
# Upstream: Vipul Ved Prakash <mail$vipul,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Tie-EncryptedHash

Summary: Hashes (and objects based on hashes) with encrypting fields
Name: perl-Tie-EncryptedHash
Version: 1.24
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Tie-EncryptedHash/

Source: http://www.cpan.org/modules/by-module/Tie/Tie-EncryptedHash-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Hashes (and objects based on hashes) with encrypting fields.

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
%doc Changes
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Tie/EncryptedHash.pm

%changelog
* Thu Jun 11 2009 Christoph Maser <cmr@financial.com> - 1.24-1
- Updated to version 1.24.

* Thu Jun 11 2009 Christoph Maser <cmr@financial.com> - 1.8-1
- Updated to version 1.8.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.21-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.21-1
- Initial package.
