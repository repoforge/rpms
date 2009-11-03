# $Id$
# Authority: dag
# Upstream: Pierre Smolarek <smolarek$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Yahoo-Music-Ratings

Summary: Perl module that implements a method for retrieving a Yahoo! Music members song ratings
Name: perl-Yahoo-Music-Ratings
Version: 2.00
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Yahoo-Music-Ratings/

Source: http://www.cpan.org/modules/by-module/Yahoo/Yahoo-Music-Ratings-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Yahoo-Music-Ratings is a Perl module that implements a method for
retrieving a Yahoo! Music members song ratings.

This package contains the following Perl module:

    Yahoo::Music::Ratings

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
%doc %{_mandir}/man3/Yahoo::Music::Ratings.3pm*
%dir %{perl_vendorlib}/Yahoo/
%dir %{perl_vendorlib}/Yahoo/Music/
%{perl_vendorlib}/Yahoo/Music/Ratings.pm

%changelog
* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 2.00-1
- Initial package. (using DAR)
