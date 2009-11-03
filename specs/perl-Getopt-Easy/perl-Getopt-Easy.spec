# $Id$
# Authority: dag
# Upstream: Jon Bjornstad <jon$icogitate,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Getopt-Easy

Summary: Parses command line options in a simple but capable way
Name: perl-Getopt-Easy
Version: 0.1
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Getopt-Easy/

Source: http://www.cpan.org/modules/by-module/Getopt/Getopt-Easy-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Parses command line options in a simple but capable way.

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Getopt::Easy.3pm*
%dir %{perl_vendorlib}/Getopt/
#%{perl_vendorlib}/Getopt/Easy/
%{perl_vendorlib}/Getopt/Easy.pm

%changelog
* Fri Nov 23 2007 Dag Wieers <dag@wieers.com> - 0.1-1
- Initial package. (using DAR)
