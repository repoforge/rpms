# $Id$
# Authority: dries
# Upstream: Tom Fawcett <fawcett$nynexst,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Statistics-LTU

Summary: Linear Threshold Units
Name: perl-Statistics-LTU
Version: 2.8
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Statistics-LTU/

Source: http://search.cpan.org/CPAN/authors/id/T/TO/TOMFA/Statistics-LTU-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
An implementation of Linear Threshold Units.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
#%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Statistics/LTU.p*
%{perl_vendorlib}/Statistics/weather.pl

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 2.8-1
- Initial package.
