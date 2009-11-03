# $Id$
# Authority: dag
# Upstream: Audrey Tang <audreyt@audreyt.org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name PerlIO-eol

Summary: PerlIO layer for normalizing line endings
Name: perl-PerlIO-eol
Version: 0.14
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/PerlIO-eol/

Source: http://www.cpan.org/modules/by-module/PerlIO/PerlIO-eol-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 1:5.7.3
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl >= 1:5.7.3

%description
PerlIO layer for normalizing line endings.

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
%doc Changes MANIFEST MANIFEST.SKIP META.yml README SIGNATURE
%doc %{_mandir}/man3/PerlIO::eol.3pm*
%dir %{perl_vendorarch}/PerlIO/
%{perl_vendorarch}/PerlIO/eol.pm
%dir %{perl_vendorarch}/auto/PerlIO/
%{perl_vendorarch}/auto/PerlIO/eol/

%changelog
* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 0.14-1
- Initial package. (using DAR)
