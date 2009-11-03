# $Id$
# Authority: dag
# Upstream: Nick Cleaton <nick$cleaton,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Lchown

Summary: Perl module to use the lchown(2) system call
Name: perl-Lchown
Version: 1.00
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Lchown/

Source: http://www.cpan.org/authors/id/N/NC/NCLEATON/Lchown-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
perl-Lchown is a Perl module to use the lchown(2) system call.

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
%doc %{_mandir}/man3/Lchown.3pm*
%{perl_vendorarch}/Lchown.pm
%{perl_vendorarch}/auto/Lchown/

%changelog
* Sun Oct 07 2007 Dag Wieers <dag@wieers.com> - 1.00-1
- Initial package. (using DAR)
