# $Id$
# Authority: dries
# Upstream: Dave Rolsky <autarch$urth,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Log-Dispatch

Summary: Dispatches messages to one or more outputs
Name: perl-Log-Dispatch
Version: 2.24
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Log-Dispatch/

Source: http://www.cpan.org/modules/by-module/Log/Log-Dispatch-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
# From yaml build_requires
BuildRequires: perl(File::Temp)
BuildRequires: perl(Test::More)
# From yaml requires
BuildRequires: perl(Params::Validate) >= 0.15
#BuildRequires: perl(Sys::Syslog) >= 0.16   # el4/el5 ship an old version in perl-core
BuildRequires: perl(Sys::Syslog)

%description
Log::Dispatch is a suite of OO modules for logging messages to
multiple outputs, each of which can have a minimum and maximum log
level.  It is designed to be easily subclassed, both for creating a
new dispatcher object and particularly for creating new outputs.

It also allows both global (dispatcher level) and local (logging
object) message formatting callbacks which allows greater flexibility
and should reduce the need for subclassing.

Subclassing is only needed to send a message to a different output,
not to change the message format.

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
%doc Changes LICENSE MANIFEST META.yml README SIGNATURE
%doc %{_mandir}/man3/Log::Dispatch.3pm*
%doc %{_mandir}/man3/Log::Dispatch::*.3pm*
%dir %{perl_vendorlib}/Log/
%{perl_vendorlib}/Log/Dispatch/
%{perl_vendorlib}/Log/Dispatch.pm

%changelog
* Mon Sep 14 2009 Christoph Maser <cmr@financial.com> - 2.24-1
- Updated to version 2.24.

* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 2.22-1
- Updated to version 2.22.

* Wed Feb 20 2008 Dag Wieers <dag@wieers.com> - 2.21-1
- Updated to release 2.21.

* Tue Nov 13 2007 Dag Wieers <dag@wieers.com> - 2.20-1
- Updated to release 2.20.

* Mon Jun 18 2007 Dries Verachtert <dries@ulyssis.org> - 2.18-1
- Updated to release 2.18.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 2.17-1
- Updated to release 2.17.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 2.11-1
- Updated to release 2.11.

* Sat Jun 5 2004 Dries Verachtert <dries@ulyssis.org> - 2.10-1
- Initial package.
