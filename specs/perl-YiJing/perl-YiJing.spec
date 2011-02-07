# $Id$
# Authority: dag
# Upstream: <cpan$audreyt,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name YiJing

Summary: The Book of Hacking
Name: perl-YiJing
Version: 0.10
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/YiJing/

Source: http://search.cpan.org/CPAN/authors/id/A/AU/AUDREYT/YiJing-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 5.005
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl >= 5.005

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup


%description
The Book of Hacking.

This package contains the following Perl module:

    YiJing

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
%doc MANIFEST README SIGNATURE
%doc %{_mandir}/man3/YiJing.3pm*
%doc %{_mandir}/man3/YiJing::0x0c.3pm*
%doc %{_mandir}/man3/YiJing::0x11.3pm*
%doc %{_mandir}/man3/YiJing::0x29.3pm*
%doc %{_mandir}/man3/YiJing::0x38.3pm*
%doc %{_mandir}/man3/YiJing::0x3b.3pm*
%doc %{_mandir}/man3/YiJing::0x3f.3pm*
%{perl_vendorlib}/YiJing/
%{perl_vendorlib}/YiJing.pm

%changelog
* Mon Feb  7 2011 Christoph Maser <cmaser@gmx.de> - 0.10-1
- Updated to version 0.10.

* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.02-1
- Initial package. (using DAR)
