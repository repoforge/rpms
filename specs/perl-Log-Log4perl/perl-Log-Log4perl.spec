# $Id: $

# Authority: dries
# Upstream: mailto:log4perl-devel@lists.sourceforge.net

%define real_name Log-Log4perl

Summary: Perl port of log4j
Name: perl-Log-Log4perl
Version: 0.45
Release: 1
License: GPL
Group: Applications/CPAN
URL: http://log4perl.sourceforge.net/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/M/MS/MSCHILLI/Log-Log4perl-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
Requires: perl-IPC-Shareable

%description
Log::Log4perl is a Perl port of the widely popular log4j logging package. It
allows you to control the amount of logging messages generated very
effectively. You can bump up the logging level of certain components in your
software, using powerful inheritance techniques. You can redirect the
additional logging messages to an entirely different output (append to a
file, send by email etc.) -- and everything without modifying a single line
of source code. 

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall DESTDIR=%{buildroot}
%{__rm} -f %{buildroot}%{_libdir}/perl5/*/i386-linux-thread-multi/perllocal.pod
%{__rm} -f %{buildroot}%{_libdir}/perl5/*/*/i386-linux-thread-multi/auto/Log/Log4perl/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE README Changes
%doc %{_mandir}/man?/*
%{_libdir}/perl5/vendor_perl/*/Log/Log4perl.pm
%{_libdir}/perl5/vendor_perl/*/Log/Log4perl

%changelog
* Sat Jun 5 2004 Dries Verachtert <dries@ulyssis.org> - 0.45-1
- Initial package.

