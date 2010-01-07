# $Id$
# Authority: dag
# Upstream: Steffen Beyer <sb$engelschall,com>

# ExcludeDist: el4

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Bit-Vector

Summary: Efficient bit vector, set of integers and "big int" math library
Name: perl-Bit-Vector
Version: 7.1
Release: 1%{?dist}
License: Artistic/GPL/LGPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Bit-Vector/

Source: http://search.cpan.org/CPAN/authors/id/S/ST/STBEY/Bit-Vector-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Carp::Clan) >= 5.3
#BuildRequires: perl(Storable) >= 2.21
BuildRequires: perl(Storable)
Requires: perl(Carp::Clan) >= 5.3
#Requires: perl(Storable) >= 2.21
Requires: perl(Storable)

%filter_from_requires /^perl*/d
%filter_setup


%description
Efficient bit vector, set of integers and "big int" math library.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Artistic.txt CHANGES.txt CREDITS.txt GNU_GPL.txt GNU_LGPL.txt INSTALL.txt MANIFEST README.txt examples/
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/auto/Bit/
%{perl_vendorarch}/auto/Bit/Vector/
%dir %{perl_vendorarch}/Bit/
%{perl_vendorarch}/Bit/Vector.pm
%{perl_vendorarch}/Bit/Vector.pod
%{perl_vendorarch}/Bit/Vector/

%changelog
* Thu Jan  7 2010 Christoph Maser <cmr@financial.com> - 7.1-1
- Updated to version 7.1.

* Sun Jun 04 2006 Dag Wieers <dag@wieers.com> - 6.4-2
- Fixed a problem on FC2 and FC3.

* Mon May 29 2006 Dag Wieers <dag@wieers.com> - 6.4-1
- Initial package. (using DAR)
