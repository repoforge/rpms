# $Id$
# Authority: dag
# Upstream: Tim Brody <tdb01r$ecs,soton,ac,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name URI-OpenURL
%define real_version 0.004006

Summary: Perl module to parse and construct OpenURL's (NISO Z39.88-2004)
Name: perl-URI-OpenURL
Version: 0.4.6
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/URI-OpenURL/

Source: http://www.cpan.org/modules/by-module/URI/URI-OpenURL-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-URI-OpenURL is a Perl module to parse and construct
OpenURL's (NISO Z39.88-2004).

This package contains the following Perl module:

    URI::OpenURL

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
%doc CHANGELOG MANIFEST META.yml README
%doc %{_mandir}/man3/URI::OpenURL.3pm*
%dir %{perl_vendorlib}/URI/
#%{perl_vendorlib}/URI/OpenURL/
%{perl_vendorlib}/URI/OpenURL.pm

%changelog
* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.4.6-1
- Initial package. (using DAR)
