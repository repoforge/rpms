# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Getopt-Long

Summary: Extended processing of command line options
Name: perl-Getopt-Long
Version: 2.35
Release: 1
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Getopt-Long/

Source: http://www.cpan.org/modules/by-module/Getopt/Getopt-Long-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
Requires: perl

%description
Extended processing of command line options 

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL PREFIX="%{buildroot}%{_prefix}" INSTALLDIRS="vendor"
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
%doc Announce CHANGES INSTALL MANIFEST README
%doc %{_mandir}/man3/*.3*
%dir %{perl_vendorlib}/Getopt/
%{perl_vendorlib}/Getopt/Long.pm
%{perl_vendorlib}/newgetopt.pl

%changelog
* Mon Jun 05 2006 Dag Wieers <dag@wieers.com> - 2.35-1
- Initial package. (using DAR)
