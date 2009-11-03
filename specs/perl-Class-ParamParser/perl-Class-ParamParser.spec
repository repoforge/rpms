# $Id$
# Authority: dag
# Upstream: Darren Duncan <perl$DarrenDuncan,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Class-ParamParser

Summary: Provides complex parameter list parsing
Name: perl-Class-ParamParser
Version: 1.041
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-ParamParser/

Source: http://www.cpan.org/modules/by-module/Class/Class-ParamParser-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Provides complex parameter list parsing.

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
%doc ChangeLog MANIFEST ReadMe
%doc %{_mandir}/man3/Class::ParamParser.3pm*
%dir %{perl_vendorlib}/Class/
#%{perl_vendorlib}/Class/ParamParser/
%{perl_vendorlib}/Class/ParamParser.pm

%changelog
* Fri Nov 23 2007 Dag Wieers <dag@wieers.com> - 1.041-1
- Initial package. (using DAR)
