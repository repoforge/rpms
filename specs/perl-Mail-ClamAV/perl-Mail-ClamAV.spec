# $Id$
# Authority: dag
# Upstream: Scott Beck <sbeck$gossamer-threads,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Mail-ClamAV

Summary: Perl module with bindings for the clamav virus scanner
Name: perl-Mail-ClamAV
Version: 0.29
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Mail-ClamAV/

Source: http://www.cpan.org/modules/by-module/Mail/Mail-ClamAV-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: bzip2-devel
BuildRequires: clamav-devel >= 0.95.1
BuildRequires: gmp-devel
BuildRequires: perl
BuildRequires: perl-Inline
BuildRequires: perl(Parse::RecDescent)
BuildRequires: zlib-devel
Requires: perl

%description
Mail-ClamAV is a Perl module with bindings for the clamav virus scanner.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes INSTALL MANIFEST META.yml README
%doc %{_mandir}/man3/Mail::ClamAV.3pm*
%dir %{perl_vendorarch}/auto/Mail/
%{perl_vendorarch}/auto/Mail/ClamAV/
%dir %{perl_vendorarch}/Mail/
%{perl_vendorarch}/Mail/ClamAV.pm

%changelog
* Thu Jul 23 2009 Christoph Maser <cmr@financial.com> - 0.29-1
- Updated to version 0.29.

* Wed May 28 2008 Dag Wieers <dag@wieers.com> - 0.22-1
- Updated to release 0.22.

* Tue Jan 15 2008 Dries Verachtert <dries@ulyssis.org> - 0.21-1
- Updated to release 0.21.

* Thu Dec 20 2007 Dag Wieers <dag@wieers.com> - 0.20-2
- Rebuild against clamav 0.92.

* Wed May 02 2007 Dag Wieers <dag@wieers.com> - 0.20-1
- Initial package. (using DAR)
