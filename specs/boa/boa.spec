# $Id$
# Authority: matthias

### FIXME: Fails to build on FC1 because of tetex (! Undefined control sequence.)
# ExcludeDist: fc1

%define rcver rc20
%define webroot /var/www/boa

Summary: The boa web server
Name: boa
Version: 0.94.14
Release: %{?rcver:0.%{rcver}.}1%{?dist}
Group: System Environment/Daemons
License: GPL
URL: http://www.boa.org/
Source0: http://www.boa.org/%{name}-%{version}%{?rcver}.tar.bz2
Source1: boa.init
Source2: boa.sysconfig
Source10: index.html
Source11: boa_logo_pasi2.png
Source12: button-freshrpms.png
Patch0: boa-0.94.14rc17-config.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: /etc/mime.types
BuildRequires: tetex, texinfo
%{!?_without_gzip:Requires: gzip}
%{!?_without_gzip:BuildRequires: gzip}
Provides: webserver

%description
Boa is a single-tasking HTTP server. That means that unlike traditional web
servers, it does not fork for each incoming connection, nor does it fork many
copies of itself to handle multiple connections. It internally multiplexes
all of the ongoing HTTP connections, and forks only for CGI programs (which
must be separate processes), automatic directory generation, and automatic
file gunzipping.
The primary design goals of Boa are speed and security. Security, in the sense
of "can't be subverted by a malicious user," not "fine grained access control
and encrypted communications". Boa is not intended as a feature-packed server.

Available rpmbuild rebuild options :
--with : debug access poll
--without : gzip sendfile


%prep
%setup -n %{name}-%{version}%{?rcver}
%patch0 -p1 -b .config


%build
%configure \
    %{!?_with_debug:      --disable-debug} \
    %{?_with_access:      --enable-access-control} \
    %{?_with_poll:        --with-poll} \
    %{?_without_gzip  :   --disable-gunzip} \
    %{?_without_sendfile: --disable-sendfile}
%{__make} %{?_smp_mflags}
%{__make} -C docs


%install
%{__rm} -rf %{buildroot}
# Manual install is still mandatory
%{__install} -Dp -m0755 src/boa %{buildroot}%{_sbindir}/boa
%{__install} -Dp -m0755 src/boa_indexer %{buildroot}%{_libdir}/boa/boa_indexer
%{__install} -Dp -m0644 docs/boa.8 %{buildroot}%{_mandir}/man8/boa.8
%{__install} -Dp -m0644 examples/boa.conf %{buildroot}%{_sysconfdir}/boa/boa.conf
%{__install} -Dp -m0644 contrib/redhat/boa.logrotate \
    %{buildroot}%{_sysconfdir}/logrotate.d/boa
%{__install} -Dp -m0755 %{SOURCE1} %{buildroot}%{_sysconfdir}/rc.d/init.d/boa
%{__install} -Dp -m0755 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/boa

%{__mkdir_p} %{buildroot}/%{webroot}/html
%{__mkdir_p} %{buildroot}/%{_localstatedir}/log/boa

# Install the default index.html file and images
%{__install} -p -m0644 %{SOURCE10} %{SOURCE11} %{SOURCE12} \
    %{buildroot}%{webroot}/html/


%clean
%{__rm} -rf %{buildroot}


%pre
/usr/sbin/groupadd -r www 2>/dev/null || :
/usr/sbin/useradd -s /bin/false -c "Boa web server user" \
    -d %{webroot} -M -r -g www boa 2>/dev/null || :

%post
/sbin/chkconfig --add boa

%preun
if [ $1 -eq 0 ]; then
    /sbin/service boa stop >/dev/null || :
    /sbin/chkconfig --del boa
fi

%postun
if [ $1 -ge 1 ]; then
    /sbin/service boa condrestart >/dev/null || :
fi


%files
%defattr(-, root, root, 0755)
%doc COPYING CREDITS docs/*.{html,png,txt} examples/ README
%dir %{_sysconfdir}/boa/
%config(noreplace) %{_sysconfdir}/boa/boa.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/boa
%config(noreplace) %{_sysconfdir}/sysconfig/boa
%{_sysconfdir}/rc.d/init.d/boa
%dir %{_libdir}/boa/
%{_libdir}/boa/boa_indexer
%{_sbindir}/boa
%{webroot}/
%dir %{_localstatedir}/log/boa/
%{_mandir}/man8/*


%changelog
* Fri Nov  5 2004 Matthias Saou <http://freshrpms.net/> - 0.94.14-0.rc20.1
- Minor spec tweaks.

* Thu Jul 15 2004 Matthias Saou <http://freshrpms.net/> - 0.94.14-0.rc20.1
- Update to 0.94.14rc20.

* Tue Nov 11 2003 Matthias Saou <http://freshrpms.net/> - 0.94.14-0.rc17.2
- Rebuild for Fedora Core 1.

* Wed Oct 22 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Initial package.

