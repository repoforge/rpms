# $Id$
# Authority: dag
# Upstream: Salvador Fandiño García <salva$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name URI-sftp

Summary: Perl module to add support for SFTP uris to URI package
Name: perl-URI-sftp
Version: 0.01
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/URI-sftp/

Source: http://www.cpan.org/modules/by-module/URI/URI-sftp-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-URI-sftp is a Perl module to add support for SFTP uris to URI package.

This package contains the following Perl module:

    URI::sftp

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
%doc %{_mandir}/man3/URI::sftp.3pm*
%dir %{perl_vendorlib}/URI/
#%{perl_vendorlib}/URI/sftp/
%{perl_vendorlib}/URI/sftp.pm

%changelog
* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.01-1
- Initial package. (using DAR)
