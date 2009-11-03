# $Id$
# Authority: dag
# Upstream: Jonathan Stowe <jns$gellyfish,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Sys-Lastlog

Summary: Perl module to provide an OO interface to lastlog files
Name: perl-Sys-Lastlog
Version: 1.6
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Sys-Lastlog/

Source: http://www.cpan.org/modules/by-module/Sys/Sys-Lastlog-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
perl-Sys-Lastlog is a Perl module to provide a moderately Object Oriented
Interface to lastlog files on some Unix-like systems.

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
%doc Changes MANIFEST MANIFEST.SKIP META.yml README examples/
%doc %{_mandir}/man3/Sys::Lastlog.3pm*
%dir %{perl_vendorarch}/Sys/
%{perl_vendorarch}/Sys/Lastlog.pm
%dir %{perl_vendorarch}/auto/Sys/
%{perl_vendorarch}/auto/Sys/Lastlog/

%changelog
* Fri Jun 12 2009 Christoph Maser <cmr@financial.com> - 1.6-1
- Updated to version 1.6.

* Sun Oct 07 2007 Dag Wieers <dag@wieers.com> - 1.5-1
- Initial package. (using DAR)
