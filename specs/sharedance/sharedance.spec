# $Id$
# Authority: matthias

Summary: Ephemeral key/data pair storing daemon
Name: sharedance
Version: 0.6
Release: 4%{?dist}
License: GPL
Group: System Environment/Daemons
URL: http://sharedance.pureftpd.org/
Source0: http://download.pureftpd.org/pub/sharedance/sharedance-%{version}.tar.bz2
Source1: sharedance.init
Source2: sharedance.sysconfig
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: libevent-devel

%description
Sharedance is a high-performance server that centralize ephemeral key/data
pairs on remote hosts, without the overhead and the complexity of an SQL
database.
It was mainly designed to share caches and sessions between a pool of web
servers. Access to a sharedance server is trivial through a simple PHP API
and it is compatible with the expectations of PHP 4 and 5 session handlers.


%prep
%setup


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot} _doc
%makeinstall
# Init script
%{__install} -D -p -m 0755 %{SOURCE1} \
    %{buildroot}%{_sysconfdir}/rc.d/init.d/sharedance
# Sysconfig file
%{__install} -D -p -m 0755 %{SOURCE2} \
    %{buildroot}%{_sysconfdir}/sysconfig/sharedance
# Default directory to store content
%{__mkdir_p} %{buildroot}%{_var}/lib/sharedance
# Include php scripts in %%doc but not the Makefile* files
%{__mkdir_p} _doc/php
%{__install} -p -m 0644 php/*.php _doc/php/


%clean
%{__rm} -rf %{buildroot}


%pre
/usr/sbin/useradd -r -s /sbin/nologin -d %{_var}/lib/sharedance \
    -c "Sharedance" sharedance &>/dev/null || :

%post
if [ $1 -eq 1 ]; then
    /sbin/chkconfig --add sharedance
fi

%preun
if [ $1 -eq 0 ]; then
    /sbin/service sharedance stop &>/dev/null || :
    /sbin/chkconfig --del sharedance
fi

%postun
if [ $1 -eq 0 ]; then
    /bin/rm -rf %{_var}/lib/sharedance &>/dev/null || :
    /usr/sbin/userdel sharedance &>/dev/null || :
else
    /sbin/service sharedance condrestart &>/dev/null || :
fi


%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README _doc/php/
%{_sysconfdir}/rc.d/init.d/sharedance
%config(noreplace) %{_sysconfdir}/sysconfig/sharedance
%{_sbindir}/sharedanced
%attr(0750, sharedance, sharedance) %dir %{_var}/lib/sharedance/


%changelog
* Sun Mar 25 2007 Dag Wieers <dag@wieers.com> - 0.6-4
- Rebuild against libevent-1.1a on EL5.

* Wed Mar 07 2007 Dag Wieers <dag@wieers.com> - 0.6-3
- Rebuild against libevent-1.3b.

* Fri Jan 12 2007 Matthias Saou <http://freshrpms.net/> 0.6-2
- Initial RPM release.

