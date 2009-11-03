# $Id$
# Authority: dag
# Upstream: Ian Guthrie <IGuthrie$aol,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Filesys-Statvfs

Summary: Perl module for statvfs() and fstatvfs()
Name: perl-Filesys-Statvfs
Version: 0.82
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Filesys-Statvfs/

Source: http://www.cpan.org/modules/by-module/Filesys/Filesys-Statvfs-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
perl-Filesys-Statvfs is a Perl module for statvfs() and fstatvfs().

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
%doc %{_mandir}/man3/Filesys::Statvfs.3pm*
%dir %{perl_vendorarch}/Filesys/
%{perl_vendorarch}/Filesys/Statvfs.pm
%dir %{perl_vendorarch}/auto/Filesys/
%{perl_vendorarch}/auto/Filesys/Statvfs/

%changelog
* Sun Oct 07 2007 Dag Wieers <dag@wieers.com> - 0.82-1
- Initial package. (using DAR)
