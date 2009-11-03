# $Id$
# Authority: dries
# Upstream: Bj&#246;rn Wilmsmann <bjoern$wilmsmann,de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Statistics-Smoothing-SGT

Summary: Simple Good-Turing (SGT) smoothing implementation
Name: perl-Statistics-Smoothing-SGT
Version: 2.1.2
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Statistics-Smoothing-SGT/

Source: http://www.cpan.org/modules/by-module/Statistics/Statistics-Smoothing-SGT-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
A Simple Good-Turing (SGT) smoothing implementation.

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
%doc CHANGES README
%doc %{_mandir}/man3/Statistics::Smoothing::SGT*
%{perl_vendorlib}/Statistics/Smoothing/SGT.pm
%dir %{perl_vendorlib}/Statistics/Smoothing/

%changelog
* Wed May 02 2007 Dries Verachtert <dries@ulyssis.org> - 2.1.2-1
- Updated to release 2.1.2.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 2.1.0-1
- Initial package.
