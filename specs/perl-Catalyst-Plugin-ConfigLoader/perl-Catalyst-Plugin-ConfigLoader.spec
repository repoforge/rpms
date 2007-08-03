# $Id$
# Authority: dag
# Upstream: Brian Cassidy <bricas$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Catalyst-Plugin-ConfigLoader

Summary: Perl module to load config files of various types
Name: perl-Catalyst-Plugin-ConfigLoader
Version: 0.14
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Catalyst-Plugin-ConfigLoader/

Source: http://www.cpan.org/modules/by-module/Catalyst/Catalyst-Plugin-ConfigLoader-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Catalyst-Plugin-ConfigLoader is a Perl module to load config files
of various types.

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
%doc 
%doc %{_mandir}/man3/Catalyst::Plugin::ConfigLoader.3pm*
#%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/Catalyst/
%dir %{perl_vendorlib}/Catalyst/Plugin/
#%{perl_vendorlib}/Catalyst/Plugin/ConfigLoader/
%{perl_vendorlib}/Catalyst/Plugin/ConfigLoader.pm

%changelog
* Fri Aug 03 2007 Dag Wieers <dag@wieers.com> - 0.14-1
- Initial package. (using DAR)
