# $Id$
# Authority: dag
# Upstream: Tom Insam <tom$jerakeen,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name URI-Title-iTMS

Summary: Perl module to get titles from itms:// urls
Name: perl-URI-Title-iTMS
Version: 0.5
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/URI-Title-iTMS/

Source: http://www.cpan.org/modules/by-module/URI/URI-Title-iTMS-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-URI-Title-iTMS is a Perl module to get titles from itms:// urls.

This package contains the following Perl module:

    URI::Title::iTMS

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
%doc %{_mandir}/man3/URI::Title::iTMS.3pm*
%dir %{perl_vendorlib}/URI/
%dir %{perl_vendorlib}/URI/Title/
#%{perl_vendorlib}/URI/Title/iTMS/
%{perl_vendorlib}/URI/Title/iTMS.pm

%changelog
* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.5-1
- Initial package. (using DAR)
