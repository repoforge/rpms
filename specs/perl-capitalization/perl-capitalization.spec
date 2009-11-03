# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name capitalization

summary: no capitalization on method names
Name: perl-capitalization
Version: 0.03
Release: 1%{?dist}
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/capitalization/

#Source: http://www.cpan.org/modules/by-module/capitalization/capitalization-%{version}.tar.gz
Source: http://www.cpan.org/authors/id/M/MI/MIYAGAWA/capitalization-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
Requires: perl

%description
capitalization.pm allows you to use familiar style on method naming.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST
%doc %{_mandir}/man3/*.3*
%{perl_vendorlib}/capitalization.pm

%changelog
* Sun Jul 11 2004 Dag Wieers <dag@wieers.com> - 2.57-1
- Initial package. (using DAR)
