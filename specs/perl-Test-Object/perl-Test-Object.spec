# $Id$
# Authority: dag
# Upstream: Adam Kennedy <cpan@ali.as>

### EL6 ships with perl-Test-Object-0.07-6.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-Object

Summary: Thoroughly testing objects via registered handlers
Name: perl-Test-Object
Version: 0.07
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-Object/

Source: http://www.cpan.org/modules/by-module/Test/Test-Object-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.005
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl >= 0:5.005

%description
Thoroughly testing objects via registered handlers.

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
%doc Changes LICENSE MANIFEST META.yml README
%doc %{_mandir}/man3/Test::Object.3pm*
%dir %{perl_vendorlib}/Test/
%{perl_vendorlib}/Test/Object/
%{perl_vendorlib}/Test/Object.pm

%changelog
* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 0.07-1
- Initial package. (using DAR)
