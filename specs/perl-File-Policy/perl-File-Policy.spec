# $Id$
# Authority: dag
# Upstream: BBC <cpan$bbc,co,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name File-Policy

Summary: Site policy for file I/O functions
Name: perl-File-Policy
Version: 1.005
Release: 1%{?dist}
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/File-Policy/

Source: http://www.cpan.org/modules/by-module/File/File-Policy-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Site policy for file I/O functions.

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

### Clean up docs
find samples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING Changes MANIFEST MANIFEST.SKIP META.yml README samples/
%doc %{_mandir}/man3/File::Policy.3pm*
%doc %{_mandir}/man3/File::Policy::*.3pm*
%doc %{_mandir}/man3/File::Slurp::WithinPolicy.3pm*
%dir %{perl_vendorlib}/File/
%{perl_vendorlib}/File/Policy/
%{perl_vendorlib}/File/Policy.pm
%dir %{perl_vendorlib}/File/Slurp/
#%{perl_vendorlib}/File/Slurp/WithinPolicy/
%{perl_vendorlib}/File/Slurp/WithinPolicy.pm

%changelog
* Fri Nov 23 2007 Dag Wieers <dag@wieers.com> - 1.005-1
- Initial package. (using DAR)
