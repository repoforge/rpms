# $Id$
# Authority: dries
# Upstream: Hironori Yoshida <yoshida$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name WebService-YouTube

Summary: Interface to YouTube
Name: perl-WebService-YouTube
Version: 1.0.3
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/WebService-YouTube/

Source: http://www.cpan.org/modules/by-module/WebService/WebService-YouTube-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
An interface to YouTube.

%prep
%setup -n %{real_name}-%{version}

%build
export PERL_EXTUTILS_AUTOINSTALL="--skipdeps --skip"
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
export PERL_EXTUTILS_AUTOINSTALL="--skipdeps --skip"
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST MANIFEST.SKIP META.yml README examples/
%doc %{_mandir}/man3/WebService::YouTube.3pm*
%doc %{_mandir}/man3/WebService::YouTube::*.3pm*
%dir %{perl_vendorlib}/WebService/
%{perl_vendorlib}/WebService/YouTube/
%{perl_vendorlib}/WebService/YouTube.pm

%changelog
* Mon Jun  8 2009 Christoph Maser <cmr@financial.com> - 1.0.3-1
- Updated to version 1.0.3.

* Mon Nov 19 2007 Dag Wieers <dag@wieers.com> - 1.0.2-1
- Updated to release 1.0.2.

* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.04-1
- Updated to release 0.04.

* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.02-1
- Initial package.
