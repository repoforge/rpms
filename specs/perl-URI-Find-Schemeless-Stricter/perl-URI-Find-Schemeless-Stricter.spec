# $Id$
# Authority: dag
# Upstream: Tony Bowden <tony$tmtm,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name URI-Find-Schemeless-Stricter

Summary: Perl module to find schemeless URIs in arbitrary text
Name: perl-URI-Find-Schemeless-Stricter
Version: 1.03
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/URI-Find-Schemeless-Stricter/

Source: http://www.cpan.org/modules/by-module/URI/URI-Find-Schemeless-Stricter-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-URI-Find-Schemeless-Stricter is a Perl module to find schemeless URIs
in arbitrary text.

This package contains the following Perl module:

    URI::Find::Schemeless::Stricter

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
%doc Changes MANIFEST MANIFEST.SKIP META.yml README
%doc %{_mandir}/man3/URI::Find::Schemeless::Stricter.3pm*
%dir %{perl_vendorlib}/URI/
%dir %{perl_vendorlib}/URI/Find/
%dir %{perl_vendorlib}/URI/Find/Schemeless/
#%{perl_vendorlib}/URI/Find/Schemeless/Stricter/
%{perl_vendorlib}/URI/Find/Schemeless/Stricter.pm

%changelog
* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 1.03-1
- Initial package. (using DAR)
