# $Id$
# Authority: dries
# Upstream: mailto:log4perl-devel$lists,sourceforge,net

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define real_name Log-Log4perl

Summary: Perl port of log4j
Name: perl-Log-Log4perl
Version: 1.04
Release: 1
License: GPL
Group: Applications/CPAN
URL: http://log4perl.sourceforge.net/

Source: http://www.cpan.org/modules/by-module/Log/Log-Log4perl-%{version}.tar.gz
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
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
		%{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes LICENSE README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/Log/
%{perl_vendorlib}/Log/Log4perl.pm
%{perl_vendorlib}/Log/Log4perl/
%exclude %{_mandir}/man3/Log::Log4perl::Appender::RRDs.3pm*
%exclude %{perl_vendorlib}/Log/Log4perl/Appender/RRDs.pm

%files RRDs
%defattr(-, root, root, 0755)
%doc %{_mandir}/man3/Log::Log4perl::Appender::RRDs.3pm*
%{perl_vendorlib}/Log/Log4perl/Appender/RRDs.pm


%changelog
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
