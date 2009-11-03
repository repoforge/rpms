# $Id$
# Authority: dag
# Upstream: Konstantin Ryabitsev <icon$linux,duke,edu>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

Summary: Log analyzer and parser
Name: epylog
Version: 1.0.3
Release: 1.2%{?dist}
License: GPL
Group: Applications/System
URL: http://linux.duke.edu/projects/epylog/

Source: http://linux.duke.edu/projects/epylog/download/epylog-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python-devel >= 2.2
BuildRequires: libxml2-devel, libxml2-python
Requires: libxml2-python, libxml2-devel

%description
Epylog is a syslog parser which runs periodically, looks at your logs,
processes some of the entries in order to present them in a more
comprehensible format, and then mails you the output. Epylog is written
specifically for large network clusters where a lot of machines (around
50 and upwards) log to the same loghost using syslog or syslog-ng. It is
an alternative to a similar package, called LogWatch.

%package -n perl-epylog
Summary: Perl module for writing external Epylog modules
Group: Development/Libraries
Requires: epylog, perl
Obsoletes: epylog-perl

%description -n perl-epylog
This package provides a perl module for epylog. It is useful for
writing epylog modules that use external module API. No modules shipping
with epylog by default use that API, so install this only if you are using
external perl modules, or intend to write some of your own.

%prep
%setup

%build
%configure \
	--with-lynx="%{_bindir}/links" \
	--with-python="%{__python}" \
	--with-python-dirs="%{python_sitelib}" \
	--with-site-perl="%{perl_vendorlib}"
%{__make}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog INSTALL LICENSE README
%doc %{_mandir}/man5/epylog.conf.5*
%doc %{_mandir}/man5/epylog-modules.5*
%doc %{_mandir}/man8/epylog.8*
%config(missingok) %{_sysconfdir}/cron.daily/epylog.cron
%config(noreplace) %{_sysconfdir}/epylog/
%{_datadir}/epylog/
%{_localstatedir}/lib/epylog/
%{python_sitelib}/epylog/
%{_sbindir}/epylog

%files -n perl-epylog
%defattr(-, root, root, 0755)
%doc %{_mandir}/man3/*
%{perl_vendorlib}/epylog.pm

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.0.3-1.2
- Rebuild for Fedora Core 5.

* Fri Apr 1 2005 Dag Wieers <dag@wieers.com> - 1.0.3-1
- Initial package. (Using DAR)
