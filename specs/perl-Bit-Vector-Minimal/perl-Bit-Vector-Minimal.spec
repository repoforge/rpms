# $Id$
# Authority: dries
# Upstream: Tony Bowden <tony$tmtm,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Bit-Vector-Minimal

Summary: Object-oriented wrapper around vec()
Name: perl-Bit-Vector-Minimal
Version: 1.3
Release: 1.2%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Bit-Vector-Minimal/

Source: http://www.cpan.org/modules/by-module/Bit/Bit-Vector-Minimal-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This is a much simplified, lightweight version of Bit::Vector, and wraps
Perl's (sometimes confusing) "vec" function in an object-oriented
abstraction.

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
%{perl_vendorlib}/Bit/

%changelog
* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.3-1
- Updated to release 1.3.

* Fri Dec 10 2004 Dries Verachtert <dries@ulyssis.org> - 1.1-1
- Initial package.
