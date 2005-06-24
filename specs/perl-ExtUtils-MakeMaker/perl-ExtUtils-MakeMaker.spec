# $Id$
# Authority: dag

# ExclusiveDist: el2 rh7 rh9 el3

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name ExtUtils-MakeMaker

Summary: Create a module Makefile 
Name: perl-ExtUtils-MakeMaker
Version: 6.17
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/ExtUtils-MakeMaker/

Source: http://www.cpan.org/modules/by-module/ExtUtils/ExtUtils-MakeMaker-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This is a CPAN distribution of the venerable MakeMaker module.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

#%{__install} -d -m0755 %{buildroot}%{_mandir}
#%{__mv} -f %{buildroot}%{_prefix}/man/man3/ %{buildroot}%{_mandir}

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST NOTES README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/ExtUtils/
%{_bindir}/instmodsh
%{perl_vendorlib}/ExtUtils/

%changelog
* Sat Apr 02 2005 Dag Wieers <dag@wieers.com> - 6.17-1
- Initial package. (using DAR)
