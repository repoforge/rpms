# $Id$
# Authority: dag
# Upstream: J. J. Merelo-Guervós <jmerelo (at) geneura,ugr,es>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name YAML-YuyuPress
%define real_version 1.9

Summary: Perl module that implements a tool for making presentations out of YAML files
Name: perl-YAML-YuyuPress
Version: 0.05
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/YAML-YuyuPress/

Source: http://www.cpan.org/modules/by-module/YAML/YAML-YuyuPress-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-YAML-YuyuPress is a Perl module that implements a tool for making
presentations out of YAML files

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
%doc %{_mandir}/man3/YAML::Yuyu.3pm*
%doc %{_mandir}/man3/YAML::YuyuPress.3pm*
%{_bindir}/yuyucheck
%{_bindir}/yuyugen
%{_bindir}/yuyupress
%dir %{perl_vendorlib}/YAML/
%{perl_vendorlib}/YAML/Yuyu.pm
%{perl_vendorlib}/YAML/YuyuPress.pm
%dir %{perl_vendorlib}/tmpl/
%{perl_vendorlib}/tmpl/normal.tmpl

%changelog
* Thu Feb 21 2008 Dag Wieers <dag@wieers.com> - 0.05-1
- Updated to release 0.05.

* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.04-1
- Initial package. (using DAR)
