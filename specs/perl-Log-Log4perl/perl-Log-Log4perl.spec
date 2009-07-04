# $Id$
# Authority: dries
# Upstream: Mike Schilli <m$perlmeister,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Log-Log4perl

Summary: Perl port of log4j
Name: perl-Log-Log4perl
Version: 1.23
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Log-Log4perl/
#URL: http://log4perl.sourceforge.net/

Source: http://www.cpan.org/modules/by-module/Log/Log-Log4perl-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Time::HiRes)
Requires: perl(IPC::Shareable), perl(Log::Dispatch), perl(Log::Dispatch::FileRotate), perl(Time::HiRes)

%description
Log::Log4perl is a Perl port of the widely popular log4j logging package. It
allows you to control the amount of logging messages generated very
effectively. You can bump up the logging level of certain components in your
software, using powerful inheritance techniques. You can redirect the
additional logging messages to an entirely different output (append to a
file, send by email etc.) -- and everything without modifying a single line
of source code.

%package RRDs
Summary: Rrdtool support
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: rrdtool

%description RRDs
Log::Log4perl is a Perl port of the widely popular log4j logging package. It
allows you to control the amount of logging messages generated very
effectively. You can bump up the logging level of certain components in your
software, using powerful inheritance techniques. You can redirect the
additional logging messages to an entirely different output (append to a
file, send by email etc.) -- and everything without modifying a single line
of source code.
This package contains the perl module and manpage for rrdtool support for
perl-Log-Log4perl.

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

### Clean up docs
find eg/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes LICENSE MANIFEST MANIFEST.SKIP META.yml README eg/
%doc %{_mandir}/man3/Log::Log4perl.3pm*
%doc %{_mandir}/man3/Log::Log4perl::*.3pm*
%dir %{perl_vendorlib}/Log/
%{perl_vendorlib}/Log/Log4perl/
%{perl_vendorlib}/Log/Log4perl.pm
%exclude %{_mandir}/man3/Log::Log4perl::Appender::RRDs.3pm*
%exclude %{perl_vendorlib}/Log/Log4perl/Appender/RRDs.pm

%files RRDs
%defattr(-, root, root, 0755)
%doc %{_mandir}/man3/Log::Log4perl::Appender::RRDs.3pm*
%{perl_vendorlib}/Log/Log4perl/Appender/RRDs.pm

%changelog
* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 1.23-1
- Updated to version 1.23.

* Wed Sep 17 2008 Dag Wieers <dag@wieers.com> - 1.18-1
- Updated to release 1.18.

* Wed Feb 20 2008 Dag Wieers <dag@wieers.com> - 1.15-1
- Updated to release 1.15.

* Sat Nov 24 2007 Dag Wieers <dag@wieers.com> - 1.14-1
- Updated to release 1.14.

* Sun Nov 11 2007 Dag Wieers <dag@wieers.com> - 1.13-1
- Updated to release 1.13.

* Mon Nov 05 2007 Dag Wieers <dag@wieers.com> - 1.12-1
- Updated to release 1.12.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 1.04-1
- Updated to release 1.04.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 1.02-1
- Updated to release 1.02.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.01-1
- Updated to release 1.01.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 0.52-1
- Updated to release 0.52.

* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 0.51-1
- Updated to release 0.51.

* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 0.50-1
- Updated to release 0.50.

* Sat Jun 12 2004 Dries Verachtert <dries@ulyssis.org> - 0.45-3
- better description for the subpackage

* Mon Jun 7 2004 Dries Verachtert <dries@ulyssis.org> - 0.45-2
- split package so rrdtool isn't always needed

* Sat Jun 5 2004 Dries Verachtert <dries@ulyssis.org> - 0.45-1
- Initial package.
