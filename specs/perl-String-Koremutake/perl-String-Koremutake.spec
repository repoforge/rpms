# $Id$
# Authority: dag
# Upstream: Leon Brocard C<acme$astray,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name String-Koremutake

Summary: Convert to/from Koremutake Memorable Random Strings
Name: perl-String-Koremutake
Version: 0.30
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/String-Koremutake/

Source: http://www.cpan.org/modules/by-module/String/String-Koremutake-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Convert to/from Koremutake Memorable Random Strings.

This package contains the following Perl module:

    String::Koremutake

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
%doc CHANGES MANIFEST META.yml README
%doc %{_mandir}/man3/String::Koremutake.3pm*
%dir %{perl_vendorlib}/String/
#%{perl_vendorlib}/String/Koremutake/
%{perl_vendorlib}/String/Koremutake.pm

%changelog
* Mon Nov 05 2007 Dag Wieers <dag@wieers.com> - 0.30-1
- Initial package. (using DAR)
