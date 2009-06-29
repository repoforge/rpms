# $Id$
# Authority: cmr
# Upstream: Jos Boumans <kane$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Config-Auto

Summary: Perl module named Config-Auto
Name: perl-Config-Auto
Version: 0.20
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Config-Auto/

Source: http://www.cpan.org/modules/by-module/Config/Config-Auto-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Config-Auto is a Perl module.

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
%doc %{_mandir}/man3/Config::Auto.3pm*
%dir %{perl_vendorlib}/Config/
#%{perl_vendorlib}/Config/Auto/
%{perl_vendorlib}/Config/Auto.pm

%changelog
* Mon Jun 29 2009 Unknown - 0.20-1
- Initial package. (using DAR)
