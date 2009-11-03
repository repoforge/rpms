# $Id$
# Authority: dag
# Upstream: Scott Walters <scott$illogics,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Sys-Mmap

Summary: Perl module to use mmap to map in a file as a Perl variable
Name: perl-Sys-Mmap
Version: 0.13
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Sys-Mmap/

Source: http://www.cpan.org/modules/by-module/Sys/Sys-Mmap-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
perl-Sys-Mmap is a Perl module to use mmap to map in a file as a Perl variable.

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
%doc Artistic Changes Copying MANIFEST META.yml README
%doc %{_mandir}/man3/Sys::Mmap.3pm*
%dir %{perl_vendorarch}/Sys/
%{perl_vendorarch}/Sys/Mmap.pm
%dir %{perl_vendorarch}/auto/Sys/
%{perl_vendorarch}/auto/Sys/Mmap/

%changelog
* Sun Oct 07 2007 Dag Wieers <dag@wieers.com> - 0.13-1
- Initial package. (using DAR)
