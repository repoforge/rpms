# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Date-Pcalc

Summary: Gregorian calendar date calculations
Name: perl-Date-Pcalc
Version: 1.2
Release: 1
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Date-Pcalc/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://search.cpan.org/CPAN/authors/id/S/ST/STBEY/Date-Pcalc-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
Requires: perl

%description
Gregorian calendar date calculations

%prep
%setup -n %{real_name}-%{version} 

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL \
	PREFIX="%{buildroot}%{_prefix}" \
	INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib}
%{__rm} -rf %{buildroot}%{perl_vendorarch}

%clean 
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc *.html *.txt
%doc %{_mandir}/man3/Date::Pcalc.3pm*
%{perl_vendorlib}/Date/Pcalc.pm

%changelog
* Sat Aug 07 2004 Dag Wieers <dag@wieers.com> - 1.2-1
- Initial package. (using DAR)
