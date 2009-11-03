# $Id$
# Authority: dag
# Upstream: Peter Sergeant <cpan$clueball,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name URI-Sequin

Summary: Perl module to extract information from the URLs of Search-Engines
Name: perl-URI-Sequin
Version: 1.2
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/URI-Sequin/

Source: http://www.cpan.org/modules/by-module/URI/URI-Sequin-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-URI-Sequin is a Perl module to extract information from the URLs
of Search-Engines.

This package contains the following Perl module:

    URI::Sequin

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
%doc CHANGES MANIFEST README
%doc %{_mandir}/man3/URI::Sequin.3pm*
%dir %{perl_vendorlib}/URI/
#%{perl_vendorlib}/URI/Sequin/
%{perl_vendorlib}/URI/Sequin.pm

%changelog
* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 1.2-1
- Initial package. (using DAR)
