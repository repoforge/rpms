# $Id$
# Authority: dag
# Upstream: Olaf Alders <olaf$wundersolutions,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name URI-ParseSearchString-More

Summary: Perl module to extract search strings from more referrers
Name: perl-URI-ParseSearchString-More
Version: 0.04
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/URI-ParseSearchString-More/

Source: http://www.cpan.org/modules/by-module/URI/URI-ParseSearchString-More-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-URI-ParseSearchString-More is a Perl module to extract search strings
from more referrers.

This package contains the following Perl module:

    URI::ParseSearchString::More

%prep
#setup -n %{real_name}-%{version}
%setup -n uri-parsesearchstring-more

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
%doc 
%doc %{_mandir}/man3/URI::ParseSearchString::More.3pm*
%dir %{perl_vendorlib}/URI/
%dir %{perl_vendorlib}/URI/ParseSearchString/
#%{perl_vendorlib}/URI/ParseSearchString/More/
%{perl_vendorlib}/URI/ParseSearchString/More.pm

%changelog
* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.04-1
- Initial package. (using DAR)
