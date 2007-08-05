# $Id$
# Authority: dag

# ExcludeDist: el4

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Bit-Vector

Summary: Efficient bit vector, set of integers and "big int" math library
Name: perl-Bit-Vector
Version: 6.4
Release: 2
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Bit-Vector/

Source: http://www.cpan.org/modules/by-module/Bit/Bit-Vector-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
Efficient bit vector, set of integers and "big int" math library.

%prep
%setup -n %{real_name}-%{version}
%{__chmod} a-x examples/*.pl

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
%doc Artistic.txt CHANGES.txt CREDITS.txt GNU_LGPL.txt GNU_GPL.txt INSTALL.txt MANIFEST README.txt
%doc examples/
%doc %{_mandir}/man3/*.3*
%dir %{perl_vendorarch}/auto/Bit/
%{perl_vendorarch}/auto/Bit/Vector/
%dir %{perl_vendorarch}/Bit/
%{perl_vendorarch}/Bit/Vector.pm
%{perl_vendorarch}/Bit/Vector.pod
%{perl_vendorarch}/Bit/Vector/

%changelog
* Sun Jun 04 2006 Dag Wieers <dag@wieers.com> - 6.4-2
- Fixed a problem on FC2 and FC3.

* Mon May 29 2006 Dag Wieers <dag@wieers.com> - 6.4-1
- Initial package. (using DAR)
