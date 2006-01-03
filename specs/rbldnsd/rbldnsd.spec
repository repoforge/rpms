# $Id$
# Authority: nac

%define         pkghome    /var/lib/rbldns

Summary:        Small and fast DNS server for serving blacklist zones.
Name:           rbldnsd
Version:        0.995
Release:        1
License:        GPL
Group:          System Environment/Daemons
Source:         http://www.corpit.ru/mjt/rbldnsd/%{name}_%{version}.tar.gz
URL:            http://www.corpit.ru/mjt/rbldnsd.html  
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
Prereq:         /sbin/chkconfig, /sbin/nologin, shadow-utils

%description

rbldnsd is a small and fast DNS daemon which is especially made to serve
DNSBL zones. This daemon was inspired by Dan J. Bernstein's rbldns program
found in the djbdns package.

rbldnsd is extremely fast - it outperforms both bind and djbdns greatly. It
has very small memory footprint.

The daemon can serve both IP-based (ordb.org, dsbl.org etc) and name-based
(rfc-ignorant.org) blocklists. Unlike DJB's rbldns, it has ability to specify
individual values for every entry, can serve as many zones on a single IP
address as you wish, and, finally, it is a real nameserver: it can reply
to DNS metadata requests. The daemon keeps all zones in memory for faster
operations, but its memory usage is very efficient, especially for repeated
TXT values which are stored only once.

%prep
%setup

%build
CFLAGS="$RPM_OPT_FLAGS" CC="${CC:-%__cc}" ./configure 
%{__make} %{_smp_mflags}

%install
%{__rm} -rf %{buildroot}

%{__install} -d %{buildroot}%{_sbindir}     \
    %{buildroot}%{_mandir}/man8             \
    %{buildroot}%{_sysconfdir}/rc.d/init.d/ \
    %{buildroot}%{_sysconfdir}/sysconfig/   \
    %{buildroot}%{_var}/lib/rbldns          \
    %{buildroot}%{_var}/lib/rbldns/log      \
    %{buildroot}%{_var}/lib/rbldns/work     \

%{__install} -m555 rbldnsd %{buildroot}%{_sbindir}
%{__install} -m444 rbldnsd.8 %{buildroot}%{_mandir}/man8
%{__install} -m664 debian/rbldnsd.default \
    %{buildroot}%{_sysconfdir}/sysconfig/rbldnsd
%{__install} -m555 debian/rbldnsd.init \
    %{buildroot}%{_sysconfdir}/rc.d/init.d/rbldnsd

%clean
%{__rm} -rf %{buildroot}

%pre
if [ $1 -eq 1 ]; then
	if ! getent passwd rbldns ; then
    		useradd -r -d %{pkghome} -M -c "rbldns Daemon" -s /sbin/nologin rbldns
    		#chown root:root %{pkghome}
	fi
fi

%post
if [ $1 -eq 1 ]; then
	/sbin/chkconfig --add rbldnsd
fi

%preun
if [ $1 -eq 0 ]; then
   /etc/init.d/rbldnsd stop || :
   /sbin/chkconfig --del rbldnsd
fi

%files
%defattr(-, root, root, 0755)
%doc README.user NEWS TODO debian/changelog CHANGES-0.81
%{_sbindir}/rbldnsd
%{_mandir}/man8/rbldnsd.8*
%config(noreplace) %{_sysconfdir}/sysconfig/rbldnsd
%{_sysconfdir}/rc.d/init.d/rbldnsd                  
%{_var}/lib/rbldns
%attr(0775,rbldns,rbldns) %{_var}/lib/rbldns/log
%attr(0775,rbldns,rbldns) %{_var}/lib/rbldns/work

%changelog
* Tue Jan 03 2006 Dries Verachtert <dries@ulyssis.org> - 0.995-1
- Updated to release 0.995.

* Sat Apr 16 2005 Wil Cooley <wcooley@nakedape.cc> - 0.994-0.b
- Initial package creation, adapted from the included spec.
