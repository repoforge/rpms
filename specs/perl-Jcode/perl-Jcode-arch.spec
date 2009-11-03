# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Jcode

Summary: Jcode (Japanese Charset Handler) module for perl
Name: perl-Jcode
Version: 2.05
Release: 1%{?dist}
License: GPL or Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Jcode/

Source: http://search.cpan.org/CPAN/authors/id/D/DA/DANKOGAI/Jcode-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 2:5.8.0
Requires: perl >= 2:5.8.0

%description
Jcode (Japanese Charset Handler) module for perl.

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

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST README
%doc %{_mandir}/man3/*.3*
%{perl_vendorarch}/Jcode.pm
%{perl_vendorarch}/Jcode/
%dir %{perl_vendorarch}/auto/
%dir %{perl_vendorarch}/auto/Jcode/
%dir %{perl_vendorarch}/auto/Jcode/Unicode/
%{perl_vendorarch}/auto/Jcode/Unicode/Unicode.bs
%{perl_vendorarch}/auto/Jcode/Unicode/Unicode.so

%changelog
* Mon May 29 2006 Dag Wieers <dag@wieers.com> - 2.05-1
- Updated to release 2.05.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 2.03-1
- Updated to release 2.03.

* Wed Jan 21 2004 Dag Wieers <dag@wieers.com> - 0.83-0
- Initial package. (using DAR)
