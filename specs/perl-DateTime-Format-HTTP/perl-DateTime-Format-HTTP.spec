# $Id$
# Authority: dag
# Upstream: Dave Rolsky <autarch$urth,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DateTime-Format-HTTP

Summary: Perl module that implements date conversion routines.
Name: perl-DateTime-Format-HTTP
Version: 0.38
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DateTime-Format-HTTP/

Source: http://www.cpan.org/modules/by-module/DateTime/DateTime-Format-HTTP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Module::Build)
Requires: perl

%description
DateTime-Format-HTTP is a Perl module that implements date conversion routines.

This package contains the following Perl module:

    DateTime::Format::HTTP

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Build.PL
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
%doc CREDITS Changes MANIFEST META.yml README
%doc %{_mandir}/man3/DateTime::Format::HTTP.3pm*
%dir %{perl_vendorlib}/DateTime/
%dir %{perl_vendorlib}/DateTime/Format/
%{perl_vendorlib}/DateTime/Format/HTTP.pm

%changelog
* Tue Jul  7 2009 Christoph Maser <cmr@financial.com> - 0.38-1
- Updated to version 0.38.

* Mon Apr 30 2007 Dag Wieers <dag@wieers.com> - 0.37-1
- Initial package. (using DAR)
