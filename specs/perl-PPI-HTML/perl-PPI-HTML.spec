# $Id$
# Authority: dag
# Upstream: Adam Kennedy <cpan$ali,as>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name PPI-HTML

Summary: PPI-HTML module for perl
Name: perl-PPI-HTML
Version: 1.07
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/PPI-HTML/

Source: http://www.cpan.org/modules/by-module/PPI/PPI-HTML-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl

%description
PPI-HTML module for perl.

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
%doc %{_mandir}/man3/PPI::HTML.3pm*
%{_bindir}/ppi2html
%dir %{perl_vendorlib}/PPI/
%{perl_vendorlib}/PPI/HTML/
%{perl_vendorlib}/PPI/HTML.pm

%changelog
* Tue May 01 2007 Dag Wieers <dag@wieers.com> - 1.07-1
- Initial package. (using DAR)
