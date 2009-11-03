# $Id$

# Authority: dries
# Upstream: Michael Robinton <michael$bizsystems,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Crypt-License

Summary: Crypt License module
Name: perl-Crypt-License
Version: 2.04
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Crypt-License/

Source: http://www.cpan.org/modules/by-module/Crypt/Crypt-License-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module set provides tools to effectively obfuscate perl source
code and allow it to be decoded and executed based on host server, user,
expiration date and other parameters. Further, decoding and execution can be
set for a system wide key as well as a unique user key.

In addition, there are a set of utilities that provide email notification of
License expiration and indirect use of the encrypted modules by other
standard modules that may reside on the system. i.e. sub-process calls by
Apache-AuthCookie while not in user space.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README makeCert.pl
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Crypt/License.pm
%{perl_vendorlib}/Crypt/License/*

%changelog
* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 2.04-1
- Updated to release 2.04.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 2.03-1.2
- Rebuild for Fedora Core 5.

* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 2.03-1
- Updated to release 2.03.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 2.02-1
- Initial package.
