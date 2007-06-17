# $Id$

# Authority: dag

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name ExtUtils-Depends

Summary: ExtUtils-Depends module for perl
Name: perl-ExtUtils-Depends
Version: 0.205
Release: 1.2
License: LGPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/ExtUtils-Depends/

Source: http://www.cpan.org/modules/by-module/ExtUtils/ExtUtils-Depends-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.8.0, perl(ExtUtils::MakeMaker)
Requires: perl >= 0:5.8.0

%description
This module tries to make it easy to build Perl extensions that use functions
and typemaps provided by other perl extensions. This means that a perl
extension is treated like a shared library that provides also a C and an XS
interface besides the perl one.  This works as long as the base extension is
loaded with the RTLD_GLOBAL flag (usually done with a sub dl_load_flags {0x01}
in the main .pm file) if you need to use functions defined in the module.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL \
	PREFIX="%{buildroot}%{_prefix}" \
	INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST README
%doc %{_mandir}/man?/*
%{perl_vendorlib}/ExtUtils/Depends.pm

%changelog
* Mon Apr 10 2006 Dries Verachtert <dries@ulyssis.org> - 0.205-1.2
- Rebuild for Fedora Core 5.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.205-1
- Updated to release 0.205.

* Thu Mar 18 2004 Dag Wieers <dag@wieers.com> - 0.202-0
- Updated to release 0.202.

* Sat Oct 11 2003 Dag Wieers <dag@wieers.com> - 0.103-0
- Updated to release 0.103.

* Sun Jul 20 2003 Dag Wieers <dag@wieers.com> - 0.102-0
- Initial package. (using DAR)
