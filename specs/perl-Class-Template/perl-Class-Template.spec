# $Id$
# Authority: dag
# Upstream: Dean Roehrich <roehrich$cray,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Class-Eroot
%define real_version 19960603

Summary: Struct/member template builder
Name: perl-Class-Template
Version: 0.0.19960603
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-Eroot/

Source: http://www.cpan.org/modules/by-module/Class/Class-Eroot-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Struct/member template builder.

%prep
%setup -n %{real_name}

%build
#%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
#%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
#%{__make} pure_install
%{__install} -Dp -m0644 Eroot.pm %{buildroot}%{perl_vendorlib}/Class/Eroot.pm
%{__install} -Dp -m0644 Template.pm %{buildroot}%{perl_vendorlib}/Class/Template.pm

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README ex.pl
#%doc %{_mandir}/man3/Class::Template.3pm*
%dir %{perl_vendorlib}/Class/
#%{perl_vendorlib}/Class/Template/
%{perl_vendorlib}/Class/Eroot.pm
%{perl_vendorlib}/Class/Template.pm

%changelog
* Fri Nov 23 2007 Dag Wieers <dag@wieers.com> - 0.0.19960603-1
- Initial package. (using DAR)
