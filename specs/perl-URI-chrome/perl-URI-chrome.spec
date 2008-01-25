# $Id$
# Authority: dag
# Upstream: Toru Yamaguchi <zigorou@cpan.org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name URI-chrome

Summary: Mozilla chrome uri
Name: perl-URI-chrome
Version: 0.01
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/URI-chrome/

Source: http://www.cpan.org/modules/by-module/URI/URI-chrome-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Carp::Clan)

%description
Mozilla chrome uri.

This package contains the following Perl module:

    URI::chrome

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
%doc %{_mandir}/man3/URI::chrome.3pm*
%dir %{perl_vendorlib}/URI/
#%{perl_vendorlib}/URI/chrome/
%{perl_vendorlib}/URI/chrome.pm

%changelog
* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.01-1
- Initial package. (using DAR)
