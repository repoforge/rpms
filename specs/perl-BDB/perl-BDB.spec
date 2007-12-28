# $Id$
# Authority: dag
# Upstream: Marc Lehmann <pcg$goof,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name BDB

Summary: Asynchronous Berkeley DB access
Name: perl-BDB
Version: 1.42
Release: 1
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/BDB/

Source: http://www.cpan.org/authors/id/M/ML/MLEHMANN/BDB-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: db4 >= 4.4
BuildRequires: perl

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
* Thu Dec 27 2007 Dag Wieers <dag@wieers.com> - 1.42-1
- Initial package. (using DAR)
