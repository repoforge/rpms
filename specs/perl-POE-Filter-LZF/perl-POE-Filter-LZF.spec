# $Id$
# Authority: dries
# Upstream: Chris Williams <chris$bingosnet,co,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name POE-Filter-LZF

Summary: POE filter wrapped around Compress::LZF
Name: perl-POE-Filter-LZF
Version: 1.5
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/POE-Filter-LZF/

Source: http://search.cpan.org//CPAN/authors/id/B/BI/BINGOS/POE-Filter-LZF-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
A POE filter wrapped around Compress::LZF.

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
%{perl_vendorlib}/POE/Filter/LZF.pm

%changelog
* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 1.5-1
- Updated to release 1.5.

* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 1.4-1
- Initial package.
