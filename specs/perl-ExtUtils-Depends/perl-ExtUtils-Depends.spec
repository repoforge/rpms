# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name ExtUtils-Depends

Summary: ExtUtils-Depends module for perl
Name: perl-ExtUtils-Depends
Version: 0.301
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/ExtUtils-Depends/

Source: http://www.cpan.org/modules/by-module/ExtUtils/ExtUtils-Depends-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 2:5.8.0
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl >= 2:5.8.0

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/ExtUtils::Depends.3pm*
%dir %{perl_vendorlib}/ExtUtils/
#%{perl_vendorlib}/ExtUtils/Depends/
%{perl_vendorlib}/ExtUtils/Depends.pm

%changelog
* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 0.301-1
- Updated to release 0.301.

* Mon May 05 2008 Dag Wieers <dag@wieers.com> - 0.300-1
- Updated to release 0.300.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.205-1
- Updated to release 0.205.

* Thu Mar 18 2004 Dag Wieers <dag@wieers.com> - 0.202-0
- Updated to release 0.202.

* Sat Oct 11 2003 Dag Wieers <dag@wieers.com> - 0.103-0
- Updated to release 0.103.

* Sun Jul 20 2003 Dag Wieers <dag@wieers.com> - 0.102-0
- Initial package. (using DAR)
