# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Convert-UUlib
%define real_version 1.12

Summary: Perl interface to the uulib library
Name: perl-Convert-UUlib
Version: 1.1200
Release: 1
License: GPL or Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Convert-UUlib/

Source: http://www.cpan.org/modules/by-module/Convert/Convert-UUlib-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker) 
Requires: perl >= 2:5.8.0

%description
A perl interface to the uulib library (a.k.a. uudeview/uuenview).

%prep
%setup -n %{real_name}-%{real_version}

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
%doc Changes COPYING* doc/* MANIFEST README
%doc %{_mandir}/man?/*
%{perl_vendorarch}/Convert/
%{perl_vendorarch}/auto/Convert/

%changelog
* Wed Jul 15 2009 Christoph Maser <cmr@financial.com> - 1.1200-1
- Updated to version 1.1200.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.051-1.2
- Rebuild for Fedora Core 5.

* Thu Mar 24 2005 Dag Wieers <dag@wieers.com> - 1.051-1
- Updated to release 1.051.

* Sun Feb 20 2005 Dag Wieers <dag@wieers.com> - 1.03-2
- Cosmetic changes.

* Wed Apr 28 2004 Dag Wieers <dag@wieers.com> - 1.03-1
- Updated to release 1.03.

* Thu Mar 18 2004 Dag Wieers <dag@wieers.com> - 1.01-0
- Updated to release 1.01.

* Mon Jul 14 2003 Dag Wieers <dag@wieers.com> - 0.31-0
- Updated to release 0.31.
- Initial package. (using DAR)
