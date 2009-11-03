# $Id$
# Authority: dag
# Upstream: Michael Robinton <michael$bizsystems,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name File-SafeDo

Summary: Safer do file for perl
Name: perl-File-SafeDo
Version: 0.11
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/File-SafeDo/

Source: http://www.cpan.org/modules/by-module/File/File-SafeDo-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Safer do file for perl.

%prep
%setup -n File-SafeDO-%{version}

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
%doc Changes MANIFEST README
%doc %{_mandir}/man3/File::SafeDO.3pm*
%dir %{perl_vendorlib}/File/
#%{perl_vendorlib}/File/SafeDO/
%{perl_vendorlib}/File/SafeDO.pm

%changelog
* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 0.11-1
- Initial package. (using DAR)
