# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Convert-BinHex

Summary: Extract data from Macintosh BinHex files
Name: perl-Convert-BinHex
Version: 1.119
Release: 2.2%{?dist}
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Convert-BinHex/

Source: http://www.cpan.org/modules/by-module/Convert/Convert-BinHex-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker) >= 0:5.00503
Requires: perl >= 0:5.00503

%description
Convert-BinHex is a set of Perl classes to extract data from Macintosh
BinHex files.

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
%doc COPYING MANIFEST README*
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/Convert/
%{perl_vendorlib}/Convert/BinHex.pm

%changelog
* Fri Jan 13 2006 Dag Wieers <dag@wieers.com> - 1.119-2
- Cosmetic cleanup.

* Sun Mar 06 2005 Dag Wieers <dag@wieers.com> - 1.119-1
- Initial package. (using DAR)
