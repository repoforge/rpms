# $Id$
# Authority: dfateyev
# Upstream: Pavel V. Cherenkov <pcherenkov$gmail,com>

%define		major_version 1.0
%define		minor_version 21
%define		rel_version 2

Name:		udpxy
Version:	%{major_version}.%{minor_version}
Release:	1%{?dist}
Summary:	UDP-to-HTTP multicast traffic relay daemon

Group:		Applications/Internet
License:	GPLv3+
URL:		http://sourceforge.net/projects/udpxy/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}.%{major_version}.%{minor_version}-%{rel_version}-prod.tgz
Source1:	udpxy.init
Source2:	udpxy.sysconfig
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

Requires: chkconfig
Requires: initscripts

%description
udpxy is a UDP-to-HTTP multicast traffic relay daemon:
it forwards UDP traffic from a given multicast subscription
to the requesting HTTP client.

%prep
%setup -n %{name}-%{major_version}.%{minor_version}-%{rel_version}

%{__chmod} a-x CHANGES

%build
%{__make} debug %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}

%{__make} install INSTALLROOT=%{buildroot}/usr

# fix 'udpxrec' symbolic link issue
%{__ln_s} -f %{_bindir}/udpxy %{buildroot}/%{_bindir}/udpxrec

%{__mkdir} -p %{buildroot}/%{_sysconfdir}/sysconfig %{buildroot}/%{_initrddir}
%{__install} -p -m755 %{SOURCE1} %{buildroot}/%{_initrddir}/%{name}
%{__install} -p -m644 %{SOURCE2} %{buildroot}/%{_sysconfdir}/sysconfig/%{name}

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/chkconfig --add udpxy
:

%preun
if [ "$1" -eq 0 ]; then
   /sbin/service udpxy stop &> /dev/null
   /sbin/chkconfig --del udpxy
fi
:

%files
%defattr(-,root,root,-)
%doc README CHANGES gpl.txt udpxy-manual-RU.rtf
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%{_initrddir}/%{name}
%{_bindir}/%{name}
%{_bindir}/udpxrec

%changelog
* Fri Mar 16 2012 Denis Fateyev <denis@fateyev.com> - 1.0.21-1
- Initial rpm release
