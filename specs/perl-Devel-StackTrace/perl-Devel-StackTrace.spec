# $Id$
# Authority: dag
# Upstream: Dave Rolsky <autarch$urth,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Devel-StackTrace

Summary: Stack trace and stack trace frame objects
Name: perl-Devel-StackTrace
Version: 1.21
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Devel-StackTrace/

Source: http://www.cpan.org/modules/by-module/Devel/Devel-StackTrace-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.006
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Module::Build)
Requires: perl >= 0:5.006

%description
Devel-StackTrace module for perl.  Simple objects to deal with stack traces.
The parent object, Devel::StackTrace, holds a number of
Devel::StackTraceFrame objects (which have the same information as is
returned from caller()).  You can step through these frames forwards
and backwards as you want or retrieve specific frames.

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
%doc Changes LICENSE MANIFEST META.yml README SIGNATURE
%doc %{_mandir}/man3/Devel::StackTrace.3pm*
%dir %{perl_vendorlib}/Devel/
#%{perl_vendorlib}/Devel/StackTrace/
%{perl_vendorlib}/Devel/StackTrace.pm

%changelog
* Mon Jul  6 2009 Christoph Maser <cmr@financial.com> - 1.21-1
- Updated to version 1.21.

* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 1.1902-1
- Updated to release 1.1902.

* Mon Jun 23 2008 Dag Wieers <dag@wieers.com> - 1.1901-1
- Updated to release 1.1901.

* Mon May 05 2008 Dag Wieers <dag@wieers.com> - 1.18-1
- Updated to release 1.18.

* Tue Feb 19 2008 Dag Wieers <dag@wieers.com> - 1.16-1
- Updated to release 1.16.

* Mon Jun 18 2007 Dries Verachtert <dries@ulyssis.org> - 1.15-1
- Updated to release 1.15.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 1.13-1
- Updated to release 1.13.

* Sat Nov 05 2005 Dries Verachtert <dries@ulyssis.org> - 1.12-1
- Upgraded to version 1.12.

* Thu Mar 31 2005 Dag Wieers <dag@wieers.com> - 1.11
- Initial package. (using DAR)
