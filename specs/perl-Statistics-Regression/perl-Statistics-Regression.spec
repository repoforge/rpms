# $Id$
# Authority: cmr
# Upstream: Ivo Welch <ivo.welch@yale.edu>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Statistics-Regression

Summary: weighted linear regression package (line+plane fitting)
Name: perl-Statistics-Regression
Version: 0.53
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Statistics-Regression/

Source: http://www.cpan.org/modules/by-module/Statistics/Statistics-Regression-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.005
BuildRequires: perl(Test::More)
Requires: perl >= 0:5.005

%description
weighted linear regression package (line+plane fitting).

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
%doc %{_mandir}/man3/Statistics::Regression.3pm*
%dir %{perl_vendorlib}/Statistics/
#%{perl_vendorlib}/Statistics/Regression/
%{perl_vendorlib}/Statistics/Regression.pm

%changelog
* Thu Jul 16 2009 Unknown - 0.53-1
- Initial package. (using DAR)
