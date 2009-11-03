# $Id$
# Authority: dag
# Upstream: Steve Snodgrass <ssnodgra$pheran,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Unix-ConfigFile

Summary: Perl interface to various Unix configuration files
Name: perl-Unix-ConfigFile
Version: 0.06
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Unix-ConfigFile/

Source: http://www.cpan.org/modules/by-module/Unix/Unix-ConfigFile-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Unix-ConfigFile is a Perl interface to various Unix configuration files.

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

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST README examples/
%doc %{_mandir}/man3/Unix::AliasFile.3pm*
%doc %{_mandir}/man3/Unix::AutomountFile.3pm*
%doc %{_mandir}/man3/Unix::ConfigFile.3pm*
%doc %{_mandir}/man3/Unix::GroupFile.3pm*
%doc %{_mandir}/man3/Unix::PasswdFile.3pm*
%dir %{perl_vendorlib}/Unix/
%{perl_vendorlib}/Unix/AliasFile.pm
%{perl_vendorlib}/Unix/AutomountFile.pm
%{perl_vendorlib}/Unix/ConfigFile.pm
%{perl_vendorlib}/Unix/GroupFile.pm
%{perl_vendorlib}/Unix/PasswdFile.pm

%changelog
* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.06-1
- Initial package. (using DAR)
