# $Id$
# Authority: dries
# Upstream: Winfried Koenig <w,koenig$acm,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name String-Parity

Summary: Generate and test even, odd, mark and space parity on arbitrary strings
Name: perl-String-Parity
Version: 1.31
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/String-Parity/

Source: http://www.cpan.org/modules/by-module/String/String-Parity-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
The String::Parity module for perl5 may be used to generate and test
even, odd, mark and space parity on arbitrary strings.

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
%{perl_vendorlib}/String/Parity.pm

%changelog
* Sat Apr  2 2005 Dries Verachtert <dries@ulyssis.org> - 1.31-1
- Initial package.
