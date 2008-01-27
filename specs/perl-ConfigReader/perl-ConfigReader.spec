# $Id$
# Authority: dag
# Upstream: Andrew Wilcox <andrew_wilcox$gwi,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name ConfigReader

Summary: Read directives from a configuration file
Name: perl-ConfigReader
Version: 0.5
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/ConfigReader/

Source: http://www.cpan.org/modules/by-module/ConfigReader/ConfigReader-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Read directives from a configuration file.

%prep
%setup -n %{real_name}-%{version}

%build
#%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
#%{__make} %{?_smp_mflags}
pod2man ConfigReader.pod ConfigReader.3pm

%install
%{__rm} -rf %{buildroot}
#%{__make} pure_install
%{__install} -Dp -m0644 DirectiveStyle.pm %{buildroot}%{perl_vendorlib}/ConfigReader/DirectiveStyle.pm
%{__install} -Dp -m0644 Spec.pm %{buildroot}%{perl_vendorlib}/ConfigReader/Spec.pm
%{__install} -Dp -m0644 Values.pm %{buildroot}%{perl_vendorlib}/ConfigReader/Values.pm
%{__install} -Dp -m0644 ConfigReader.3pm %{buildroot}%{_mandir}/man3/ConfigReader.3pm

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING.LIB README
%doc %{_mandir}/man3/ConfigReader.3pm*
%{perl_vendorlib}/ConfigReader/
#%{perl_vendorlib}/ConfigReader.pm

%changelog
* Sat Jan 26 2008 Dag Wieers <dag@wieers.com> - 0.5-1
- Initial package. (using DAR)
