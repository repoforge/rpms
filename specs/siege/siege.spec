# $Id$
# Authority: dag
# Upstream: Jeffrey Fulmer <jeff$joedog,org>

Name: siege
Version: 3.0.1
Release: 1%{?dist}
Summary: HTTP regression testing and benchmarking utility

Group: Development/Tools
License: GPLv2+
URL: http://www.joedog.org/JoeDog/Siege
Source0: ftp://ftp.joedog.org/pub/siege/beta/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: openssl-devel

%description
Siege is an HTTP regression testing and benchmarking utility. 
It was designed to let web developers measure the performance of their code 
under duress, to see how it will stand up to load on the internet. 
Siege supports basic authentication, cookies, HTTP and HTTPS protocols. 
It allows the user hit a web server with a configurable number of concurrent 
simulated users. Those users place the web-server "under siege."

%prep
%setup -c

cd %{name}-%{version}

# better default for log file (Bug 644631)
%{__sed} -i.orig doc/siegerc.in -e 's/^# logfile = *$/logfile = ${HOME}\/siege.log/'

%build
cd %{name}-%{version}

%configure --sysconfdir=/etc/siege
%{__make} %{?_smp_mflags}


%install
cd %{name}-%{version}
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_sysconfdir}/siege
%{__make} install DESTDIR=%{buildroot}

%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc %{name}-%{version}/AUTHORS
%doc %{name}-%{version}/ChangeLog
%doc %{name}-%{version}/COPYING
%doc %{name}-%{version}/KNOWNBUGS
%doc %{name}-%{version}/MACHINES
%doc %{name}-%{version}/NEWS
%doc %{name}-%{version}/PLATFORM
%doc %{name}-%{version}/README
%doc %{name}-%{version}/README.https
%{_bindir}/bombardment
%{_bindir}/siege
%{_bindir}/siege.config
%{_bindir}/siege2csv.pl
%{_mandir}/man1/bombardment.1.gz
%{_mandir}/man1/siege.1.gz
%{_mandir}/man1/siege.config.1.gz
%{_mandir}/man1/siege2csv.1.gz
%{_mandir}/man5/urls_txt.5.gz
%{_mandir}/man7/layingsiege.7.gz
%dir %{_sysconfdir}/siege
%config(noreplace) %{_sysconfdir}/siege/urls.txt
%config(noreplace) %{_sysconfdir}/siege/siegerc


%changelog
* Sun Jun 16 2013 Denis Fateyev <denis@fateyev.com> - 3.0.1-1
- Update to version 3.0.1, synced with fedora spec

* Thu Feb 16 2012 David Hrbáč <david@hrbac.cz> - 2.72-1
- new upstream release

* Tue Feb 14 2012 David Hrbáč <david@hrbac.cz> - 2.71-1
- new upstream release

* Mon Jul 02 2007 Dag Wieers <dag@wieers.com> - 2.66-1
- Initial package. (using DAR)
