# $Id$
# Authority: dag
# Upstream: Brian Cassidy <bricas@cpan.org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Config-Any

Summary: Load configuration from different file formats, transparently
Name: perl-Config-Any
Version: 0.23
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Config-Any/

Source: http://search.cpan.org/CPAN/authors/id/B/BR/BRICAS/Config-Any-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Module::Pluggable) >= 3.01
BuildRequires: perl(Test::More)
BuildRequires: perl >= 5.6.0
Requires: perl(Module::Pluggable) >= 3.01
Requires: perl >= 5.6.0

%filter_from_requires /^perl*/d
%filter_setup

%description
Load configuration from different file formats, transparently.

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
%doc %{_mandir}/man3/Config::Any.3pm*
%doc %{_mandir}/man3/Config::Any::*.3pm*
%dir %{perl_vendorlib}/Config/
%{perl_vendorlib}/Config/Any/
%{perl_vendorlib}/Config/Any.pm

%changelog
* Wed Apr 25 2012 David Hrbáč <david@hrbac.cz> - 0.23-1
- new upstream release

* Fri Jun 03 2011 David Hrbáč <david@hrbac.cz> - 0.21-1
- new upstream release

* Fri Oct 29 2010 Christoph Maser <cmaser@gmx.de> - 0.20-1
- Updated to version 0.20.

* Thu Dec 31 2009 Christoph Maser <cmr@financial.com> - 0.18-1
- Updated to version 0.18.

* Wed Jul 15 2009 Christoph Maser <cmr@financial.com> - 0.17-1
- Updated to version 0.17.

* Thu Dec 18 2008 Dag Wieers <dag@wieers.com> - 0.16-1
- Updated to release 0.16.

* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 0.14-1
- Updated to release 0.14.

* Sat May 03 2008 Dag Wieers <dag@wieers.com> - 0.12-1
- Updated to release 0.12.

* Tue Feb 19 2008 Dag Wieers <dag@wieers.com> - 0.11-1
- Updated to release 0.11.

* Fri Dec 14 2007 Dag Wieers <dag@wieers.com> - 0.10-1
- Updated to release 0.10.

* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 0.08-1
- Updated to release 0.08.

* Fri Aug 03 2007 Dag Wieers <dag@wieers.com> - 0.07-1
- Initial package. (using DAR)
