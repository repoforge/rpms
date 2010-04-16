# $Id$
# Authority: dag
# Upstream: Six Apart <cpan@sixapart.com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name TheSchwartz

Summary: Reliable job queue
Name: perl-TheSchwartz
Version: 1.10
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/TheSchwartz/

Source: http://search.cpan.org/CPAN/authors/id/S/SI/SIXAPART/TheSchwartz-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Data::ObjectDriver) >= 0.04
BuildRequires: perl(Digest::MD5)
BuildRequires: perl(ExtUtils::MakeMaker) 
BuildRequires: perl(Storable)
Requires: perl
Requires: perl(Data::ObjectDriver) >= 0.04
Requires: perl(Digest::MD5)
Requires: perl(Storable)

%filter_from_requires /^perl*/d
%filter_setup


%description
Reliable job queue.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"  --skipdeps
%{__make} %{?_smp_mflags}
# %{__make} %{?_smp_mflags} test

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find doc/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES MANIFEST MANIFEST.SKIP META.yml doc/
%doc %{_mandir}/man1/schwartzmon.1*
%doc %{_mandir}/man3/TheSchwartz.3pm*
%doc %{_mandir}/man3/TheSchwartz::*.3pm*
%{_bindir}/schwartzmon
%{perl_vendorlib}/TheSchwartz/
%{perl_vendorlib}/TheSchwartz.pm

%changelog
* Fri Apr 16 2010 Christoph Maser <cmr@financial.com> - 1.10-1
- Updated to version 1.10.

* Fri Jul 31 2009 Christoph Maser <cmr@financial.com> - 1.07-2
- Set AutoReq: no to get rid of DBD-driver deps

* Sun Jul 19 2009 Dag Wieers <dag@wieers.com> - 1.07-1
- Initial package. (using DAR)
