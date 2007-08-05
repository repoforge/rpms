# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Devel-StackTrace

Summary: Devel-StackTrace module for perl
Name: perl-Devel-StackTrace
Version: 1.15
Release: 1
License: GPL or Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/perl-Devel-StackTrace/

Source: http://www.cpan.org/modules/by-module/Devel/Devel-StackTrace-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
Devel-StackTrace module for perl.  Simple objects to deal with stack traces.
The parent object, Devel::StackTrace, holds a number of
Devel::StackTraceFrame objects (which have the same information as is
returned from caller()).  You can step through these frames forwards
and backwards as you want or retrieve specific frames.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL PREFIX="%{buildroot}%{_prefix}" INSTALLDIRS="vendor"
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
%doc Changes LICENSE README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/Devel/
%{perl_vendorlib}/Devel/StackTrace.pm

%changelog
* Mon Jun 18 2007 Dries Verachtert <dries@ulyssis.org> - 1.15-1
- Updated to release 1.15.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 1.13-1
- Updated to release 1.13.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.12-1.2
- Rebuild for Fedora Core 5.

* Sat Nov 05 2005 Dries Verachtert <dries@ulyssis.org> - 1.12-1
- Upgraded to version 1.12.

* Thu Mar 31 2005 Dag Wieers <dag@wieers.com> - 1.11
- Initial package. (using DAR)
