# $Id$
# Authority: dag
# Upstream: Marc Lehmann <pcg$goof,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name ExtUtils-PkgConfig

Summary: Perl module that implements a simplistic interface to pkg-config
Name: perl-ExtUtils-PkgConfig
Version: 1.10
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/ExtUtils-PkgConfig/

Source: http://www.cpan.org/modules/by-module/ExtUtils/ExtUtils-PkgConfig-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 2:5.8.0
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: pkgconfig
Requires: perl >= 2:5.8.0

%description
This module is a simplistic Perl interface to the pkg-config command-line
utility, for use in the Makefile.PLs used to build Perl modules which wrap
the libraries about which pkg-config knows.

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
%doc Changes MANIFEST MANIFEST.SKIP META.yml README
%doc %{_mandir}/man3/ExtUtils::PkgConfig.3pm*
%dir %{perl_vendorlib}/ExtUtils/
#%{perl_vendorlib}/ExtUtils/PkgConfig/
%{perl_vendorlib}/ExtUtils/PkgConfig.pm

%changelog
* Wed Feb 20 2008 Dag Wieers <dag@wieers.com> - 1.10-1
- Updated to release 1.10.

* Sat Jan 26 2008 Dag Wieers <dag@wieers.com> - 1.09-1
- Updated to release 1.09.

* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 1.08-1
- Updated to release 1.08.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.07-1
- Updated to release 1.07.

* Thu Mar 18 2004 Dag Wieers <dag@wieers.com> - 1.03-0
- Updated to release 1.03.

* Sat Oct 11 2003 Dag Wieers <dag@wieers.com> - 1.01-0
- Initial package. (using DAR)
