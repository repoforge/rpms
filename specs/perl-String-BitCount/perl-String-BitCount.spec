# $Id$
# Authority: dries
# Upstream: Winfried Koenig <w,koenig$acm,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name String-BitCount

Summary: Count number of "1" bits in strings
Name: perl-String-BitCount
Version: 1.13
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/String-BitCount/

Source: http://www.cpan.org/modules/by-module/String/String-BitCount-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
The String::BitCount module for perl5 may be used to determine the number
of 'one bits' in strings and to show the number of bits in each byte of a
string. Only code points in the range 0x00 .. 0xFF are allowed.

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
%{perl_vendorlib}/String/BitCount.pm

%changelog
* Sat Apr  2 2005 Dries Verachtert <dries@ulyssis.org> - 1.13-1
- Initial package.
