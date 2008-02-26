# $Id$
# Authority: dag
# Upstream: Jan Krynicky <Jenda$Krynicky,cz>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Config-IniHash
%define real_version 3.00

Summary: Perl module for reading and writing INI files
Name: perl-Config-IniHash
Version: 3.00.00
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Config-IniHash/

Source: http://www.cpan.org/modules/by-module/Config/Config-IniHash-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Config-IniHash is a Perl module for reading and writing INI files.

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
%doc %{_mandir}/man3/Config::IniHash.3pm*
%dir %{perl_vendorlib}/Config/
%{perl_vendorlib}/Config/IniHash.pm

%changelog
* Sun Feb 24 2008 Dag Wieers <dag@wieers.com> - 3.00.00-1
- Updated to release 3.00.00.

* Fri Aug 03 2007 Dag Wieers <dag@wieers.com> - 2.8-1
- Initial package. (using DAR)
