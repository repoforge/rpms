# $Id$
# Authority: dag
# Upstream: Jeffrey Friedl <jfriedl$yahoo,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Yahoo-Search
%define real_version 1.010013

Summary: Perl module named Yahoo-Search
Name: perl-Yahoo-Search
Version: 1.10.13
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Yahoo-Search/

Source: http://www.cpan.org/modules/by-module/Yahoo/Yahoo-Search-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Yahoo-Search is a Perl module.

This package contains the following Perl module:

    Yahoo::Search

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
%doc %{_mandir}/man3/Yahoo::Search.3pm*
%doc %{_mandir}/man3/Yahoo::Search::Request.3pm*
%doc %{_mandir}/man3/Yahoo::Search::Response.3pm*
%doc %{_mandir}/man3/Yahoo::Search::Result.3pm*
%doc %{_mandir}/man3/Yahoo::Search::XML.3pm*
%dir %{perl_vendorlib}/Yahoo/
%{perl_vendorlib}/Yahoo/Search/
%{perl_vendorlib}/Yahoo/Search.pm

%changelog
* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 1.10.13-1
- Initial package. (using DAR)
