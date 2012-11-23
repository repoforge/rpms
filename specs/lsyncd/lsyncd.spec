# $Id$
# Authority: yury
# Upstream: Axel Kittenberger <axkibe$gmail,com>

Summary:        Live syncing (mirroring) daemon
Name:           lsyncd
Version:        2.1.3
Release:        1%{?dist}
License:        GPL
Group:          Applications/File
URL:            http://code.google.com/p/lsyncd/

Source0:        https://%{name}.googlecode.com/files/%{name}-%{version}.tar.gz
Source1:        %{name}.service
Source2:        %{name}.init
Source3:        %{name}.sysconfig
Source4:        %{name}.logrotate

BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

# Use systemd unit files on Fedora 15 and above.
%if 0%{?fedora} >= 15 || 0%{?rhel} >= 7
  %global _with_systemd 1
%endif

BuildRequires:  lua-devel >= 5.1.3
BuildRequires:  prelink
BuildRequires:  asciidoc
%if 0%{?_with_systemd}
BuildRequires: systemd-units
%endif

Requires: lua
Requires: rsync
%if 0%{?_with_systemd}
Requires: systemd
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units
%else
Requires: chkconfig
%endif

%description
Lsyncd(1) watches a local directory trees event monitor interface
(inotify). It aggregates and combines events for a few seconds and
then spawns one (or more) process(es) to synchronize the changes.
By default this is rsync(1). Lsyncd is thus a light-weight live mirror
solution that is comparatively easy to install not requiring new
filesystems or blockdevices and does not hamper local filesystem
performance.

%prep
%setup -q

%build
%configure
%{__make} %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR="%{buildroot}"

%if 0%{?_with_systemd}
# install systemd service files
%{__install} -p -D -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
%else
%{__install} -p -D -m 0755 %{SOURCE2} %{buildroot}%{_initrddir}/%{name}
%endif
%{__install} -p -D -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/sysconfig/%{name}
%{__install} -p -D -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}

%clean
rm -rf %{buildroot}

%post
%if 0%{?_with_systemd}
if [ $1 -eq 1 ] ; then
    # Initial installation
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi
%else
if [ $1 -eq 1 ]; then
    /sbin/chkconfig --add %{name}
fi
%endif

%preun
%if 0%{?_with_systemd}
if [ $1 -eq 0 ] ; then
    /bin/systemctl --no-reload disable lsyncd.service > /dev/null 2>&1 || :
    /bin/systemctl stop lsyncd.service > /dev/null 2>&1 || :
fi
%else
if [ $1 -eq 0 ]; then
    /sbin/service %{name} stop &>/dev/null || :
    /sbin/chkconfig --del %{name}
fi
%endif

%postun
%if 0%{?_with_systemd}
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
    /bin/systemctl try-restart lsyncd.service >/dev/null 2>&1 || :
fi
%else
if [ $1 -ge 1 ]; then
    /sbin/service %{name} condrestart &>/dev/null || :
fi
%endif

%files
%defattr(-,root,root,0755)
%doc ChangeLog COPYING examples
%doc %{_mandir}/man1/lsyncd.1.gz
%{_bindir}/lsyncd
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%if 0%{?_with_systemd}
%{_unitdir}/%{name}.service
%else
%{_initrddir}/%{name}
%endif
%exclude %{_docdir}/lsyncd

%changelog
* Wed Nov 05 2012 Troxor Zero <troxor0@yahoo.com> - 2.1.2-1
- Updated to release 2.1.2
- Added a systemd service file
- Added a logrotate config file

* Wed Mar 30 2011 Yury V. Zaytsev <yury@shurup.com> - 2.0.4-1
- Updated to release 2.0.4 (thanks to Aleksandar Ivanisevic!)

* Tue Mar 22 2011 Yury V. Zaytsev <yury@shurup.com> - 2.0.2-2
- Added an init script (thanks to Aleksandar Ivanisevic!)

* Tue Feb 22 2011 Yury V. Zaytsev <yury@shurup.com> - 2.0.2-1
- Updated to release 2.0.2 (thanks to Aleksandar Ivanisevic!)

* Thu Mar 27 2008 Dag Wieers <dag@wieers.com> - 1.0-1
- Initial package. (using DAR)
