# $Id$
# Authority: dag
# Upstream: Adam Kennedy <cpan$ali,as>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name URI-ToDisk

Summary: An object for mapping a URI to an on-disk storage directory
Name: perl-URI-ToDisk
Version: 1.12
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/URI-ToDisk/

Source: http://www.cpan.org/modules/by-module/URI/URI-ToDisk-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.005
BuildRequires: perl(Clone) >= 0.13
BuildRequires: perl(File::Spec) >= 0.80
BuildRequires: perl(List::Util) >= 1.11
BuildRequires: perl(Params::Util) >= 0.10
BuildRequires: perl(Test::More) >= 0.47
BuildRequires: perl(URI)
Requires: perl >= 0:5.005

%description
perl-URI-ToDisk is a Perl module for mapping a URI to
an on-disk storage directory.

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
%doc %{_mandir}/man3/URI::ToDisk.3pm*
%dir %{perl_vendorlib}/URI/
#%{perl_vendorlib}/URI/ToDisk/
%{perl_vendorlib}/URI/ToDisk.pm

%changelog
* Mon Nov 19 2007 Dag Wieers <dag@wieers.com> - 1.12-1
- Updated to release 1.12.

* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 1.09-1
- Initial package. (using DAR)
