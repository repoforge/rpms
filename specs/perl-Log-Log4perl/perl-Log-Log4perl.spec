# $Id$

# Authority: dries
# Upstream: mailto:log4perl-devel$lists,sourceforge,net

%define real_name Log-Log4perl
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Perl port of log4j
Name: perl-Log-Log4perl
Version: 0.51
Release: 3
License: GPL
Group: Applications/CPAN
URL: http://log4perl.sourceforge.net/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/M/MS/MSCHILLI/Log-Log4perl-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl-Time-HiRes
Requires: perl-IPC-Shareable, perl-Log-Dispatch, perl-Log-Dispatch-FileRotate, perl-Time-HiRes

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
%{__perl} Makefile.PL INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall DESTDIR=%{buildroot}
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE README Changes
%{perl_vendorlib}/Log/Log4perl.pm
%{perl_vendorlib}/Log/Log4perl/Appender.pm
%{perl_vendorlib}/Log/Log4perl/Appender/DBI.pm
%{perl_vendorlib}/Log/Log4perl/Appender/File.pm
%{perl_vendorlib}/Log/Log4perl/Appender/Limit.pm
%{perl_vendorlib}/Log/Log4perl/Appender/Screen.pm
%{perl_vendorlib}/Log/Log4perl/Appender/Socket.pm
%{perl_vendorlib}/Log/Log4perl/Appender/Synchronized.pm
%{perl_vendorlib}/Log/Log4perl/Appender/TestArrayBuffer.pm
%{perl_vendorlib}/Log/Log4perl/Appender/TestBuffer.pm
%{perl_vendorlib}/Log/Log4perl/Appender/TestFileCreeper.pm
%{perl_vendorlib}/Log/Log4perl/Appender/ScreenColoredLevels.pm
%{perl_vendorlib}/Log/Log4perl/Config.pm
%{perl_vendorlib}/Log/Log4perl/Config
%{perl_vendorlib}/Log/Log4perl/DateFormat.pm
%{perl_vendorlib}/Log/Log4perl/FAQ.pm
%{perl_vendorlib}/Log/Log4perl/Filter.pm
%{perl_vendorlib}/Log/Log4perl/Filter
%{perl_vendorlib}/Log/Log4perl/JavaMap.pm
%{perl_vendorlib}/Log/Log4perl/JavaMap
%{perl_vendorlib}/Log/Log4perl/Layout.pm
%{perl_vendorlib}/Log/Log4perl/Layout
%{perl_vendorlib}/Log/Log4perl/Level.pm
%{perl_vendorlib}/Log/Log4perl/Logger.pm
%{perl_vendorlib}/Log/Log4perl/MDC.pm
%{perl_vendorlib}/Log/Log4perl/NDC.pm
%{perl_vendorlib}/Log/Log4perl/Util.pm
%{_mandir}/man3/Log::Log4perl.3pm.gz
%{_mandir}/man3/Log::Log4perl::Appender.3pm.gz
%{_mandir}/man3/Log::Log4perl::Appender::DBI.3pm.gz
%{_mandir}/man3/Log::Log4perl::Appender::File.3pm.gz
%{_mandir}/man3/Log::Log4perl::Appender::Limit.3pm.gz
%{_mandir}/man3/Log::Log4perl::Appender::Screen.3pm.gz
%{_mandir}/man3/Log::Log4perl::Appender::Socket.3pm.gz
%{_mandir}/man3/Log::Log4perl::Appender::Synchronized.3pm.gz
%{_mandir}/man3/Log::Log4perl::Appender::TestArrayBuffer.3pm.gz
%{_mandir}/man3/Log::Log4perl::Appender::TestBuffer.3pm.gz
%{_mandir}/man3/Log::Log4perl::Appender::TestFileCreeper.3pm.gz
%{_mandir}/man3/Log::Log4perl::Appender::ScreenColoredLevels.3pm.gz
%{_mandir}/man3/Log::Log4perl::Config*
%{_mandir}/man3/Log::Log4perl::DateFormat.3pm.gz
%{_mandir}/man3/Log::Log4perl::FAQ.3pm.gz
%{_mandir}/man3/Log::Log4perl::Filter*
%{_mandir}/man3/Log::Log4perl::JavaMap*
%{_mandir}/man3/Log::Log4perl::Layout*
%{_mandir}/man3/Log::Log4perl::Level.3pm.gz
%{_mandir}/man3/Log::Log4perl::Logger.3pm.gz
%{_mandir}/man3/Log::Log4perl::MDC.3pm.gz
%{_mandir}/man3/Log::Log4perl::NDC.3pm.gz
%{_mandir}/man3/Log::Log4perl::Util.3pm.gz

%files RRDs
%defattr(-, root, root, 0755)
%{perl_vendorlib}/Log/Log4perl/Appender/RRDs.pm
%doc %{_mandir}/man3/Log::Log4perl::Appender::RRDs.3pm*


%changelog
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
