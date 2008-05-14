# $Id$
# Authority: dries
# Upstream: Rocco Caputo <rcaputo$cpan,org>

# ExcludeDist: el3

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name POE

Summary: Portable multitasking and networking framework for Perl
Name: perl-POE
Version: 1.0002
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/POE/

Source: http://www.cpan.org/modules/by-module/POE/POE-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
Provides: perl(POE::Resource::Controls)

%description
POE is a networking and multitasking (some say cooperative threading)
framework for Perl.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}" --default
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES HISTORY MANIFEST MANIFEST.SKIP META.yml README TODO examples/
%doc %{_mandir}/man3/POE.3pm*
%doc %{_mandir}/man3/POE::*.3pm*
%{perl_vendorlib}/POE/
%{perl_vendorlib}/POE.pm

%changelog
* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 1.0002-1
- Updated to release 1.0002.

* Thu Nov 15 2007 Dag Wieers <dag@wieers.com> - 0.9999-1
- Updated to release 0.9999.

* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.38-1
- Updated to release 0.38.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.37-1
- Updated to release 0.37.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.34-1
- Updated to release 0.34.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 0.33-1
- Updated to release 0.33.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.3202-1
- Updated to release 0.3202.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 0.3101-1
- Updated to release 0.3101.

* Thu Apr 28 2005 Dries Verachtert <dries@ulyssis.org> - 0.31-1
- Updated to release 0.31.

* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 0.3009-1
- Updated to release 0.3009.

* Fri Dec 10 2004 Dries Verachtert <dries@ulyssis.org> - 0.3003-1
- Initial package.
