# $Id$
# Authority: dag
# Upstream: Xavier Noria <FXN$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Algorithm-Combinatorics

Summary: Efficient generation of combinatorial sequences
Name: perl-Algorithm-Combinatorics
Version: 0.25
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Algorithm-Combinatorics/

Source: http://www.cpan.org/modules/by-module/Algorithm/Algorithm-Combinatorics-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
Efficient generation of combinatorial sequences.

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Algorithm::Combinatorics.3pm*
%dir %{perl_vendorarch}/auto/Algorithm/
%{perl_vendorarch}/auto/Algorithm/Combinatorics/
%dir %{perl_vendorarch}/Algorithm/
%{perl_vendorarch}/Algorithm/Combinatorics.pm

%changelog
* Tue Dec 04 2007 Dag Wieers <dag@wieers.com> - 0.25-1
- Updated to release 0.25.

* Sun Oct 07 2007 Dag Wieers <dag@wieers.com> - 0.24-1
- Initial package. (using DAR)
