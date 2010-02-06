# $Id$
# Authority: dries
# Upstream: Steffen Ullrich <Steffen_Ullrich$genua,de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-SIP

Summary: Framework for SIP and Voice Over IP
Name: perl-Net-SIP
Version: 0.56
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-SIP/

Source: http://search.cpan.org/CPAN/authors/id/S/SU/SULLR/Net-SIP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Net::DNS) >= 0.56
BuildRequires: perl(Time::HiRes)
Requires: perl(Net::DNS) >= 0.56

%filter_from_requires /^perl*/d
%filter_setup

%description
Framework SIP (Voice Over IP, RFC3261).

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}
%{__make} test

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find samples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc BUGS COPYRIGHT Changes INSTALL MANIFEST META.yml README THANKS TODO samples/
%doc %{_mandir}/man3/Net::SIP.3pm*
%doc %{_mandir}/man3/Net::SIP::*.3pm*
%dir %{perl_vendorlib}/Net/
%{perl_vendorlib}/Net/SIP/
%{perl_vendorlib}/Net/SIP.pm
%{perl_vendorlib}/Net/SIP.pod

%changelog
* Sat Feb  6 2010 Christoph Maser <cmr@financial.com> - 0.56-1
- Updated to version 0.56.

* Wed Feb  3 2010 Christoph Maser <cmr@financial.com> - 0.55-1
- Updated to version 0.55.

* Tue Sep  8 2009 Christoph Maser <cmr@financial.com> - 0.54-1
- Updated to version 0.54.

* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 0.53-1
- Updated to version 0.53.

* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 0.45-1
- Updated to release 0.45.

* Mon Mar 03 2008 Dag Wieers <dag@wieers.com> - 0.44-1
- Updated to release 0.44.

* Mon Feb 25 2008 Dag Wieers <dag@wieers.com> - 0.43-1
- Updated to release 0.43.

* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 0.41-1
- Updated to release 0.41.

* Tue Dec 04 2007 Dag Wieers <dag@wieers.com> - 0.40-1
- Updated to release 0.40.

* Thu Nov 15 2007 Dag Wieers <dag@wieers.com> - 0.39-1
- Updated to release 0.39.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.23-1
- Initial package.
