# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name GDTextUtil

Summary: Text utilities for use with GD
Name: perl-GD-Text-Util
Version: 0.86
Release: 1
License: LGPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/GDTextUtil/

Source: http://www.cpan.org/modules/by-module/GDTextUtil/GDTextUtil-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.8.0
Requires: perl >= 0:5.8.0

%description
Text utilities for use with GD.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean 
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST README *LICENSE
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/GD/
%{perl_vendorlib}/GD/Text/
%{perl_vendorlib}/GD/Text.pm

%changelog
* Sat Apr 02 2005 Dag Wieers <dag@wieers.com> - 0.86-1
- Cosmetic cleanup.
- Fixed BuildArch, now noarch.

* Mon Mar 15 2004 Dag Wieers <dag@wieers.com> - 0.86-0
- Initial package. (using DAR)
