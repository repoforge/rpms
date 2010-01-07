# $Id$
# Authority: dag
# Upstream: Marc Lehmann <schmorp@schmorp.de>
# db4 is too old on el4
# ExcludeDist: el4 el3

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name BDB

Summary: Asynchronous Berkeley DB access
Name: perl-BDB
Version: 1.87
Release: 1%{?dist}
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/BDB/

Source: http://search.cpan.org/CPAN/authors/id/M/ML/MLEHMANN/BDB-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: db4-devel >= 4.3
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(common::sense)
Requires: perl(common::sense)

%filter_from_requires /^perl*/d
%filter_setup



%description
Asynchronous Berkeley DB access.

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
find eg/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING Changes MANIFEST META.yml README eg/
%doc %{_mandir}/man3/BDB.3pm*
%{perl_vendorarch}/auto/BDB/
%{perl_vendorarch}/BDB.pm

%changelog
* Thu Jan  7 2010 Christoph Maser <cmr@financial.com> - 1.87-1
- Updated to version 1.87.

* Sat Aug 22 2009 Christoph Maser <cmr@financial.com> - 1.84-1
- Updated to version 1.84.

* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 1.801-1
- Updated to release 1.801.

* Sat May 03 2008 Dag Wieers <dag@wieers.com> - 1.45-1
- Updated to release 1.45.

* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 1.43-1
- Updated to release 1.43.

* Thu Dec 27 2007 Dag Wieers <dag@wieers.com> - 1.42-1
- Initial package. (using DAR)
