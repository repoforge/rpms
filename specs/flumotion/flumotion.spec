# $Id$

Summary: Flumotion - the Fluendo Streaming Server
Name: flumotion
Version: 0.1.1
Release: 0.3
Group: Applications/Internet
License: GPL
URL: http://www.fluendo.com/
Source: http://www.fluendo.com/downloads/flumotion-%{version}.tar.bz2
Patch0: flumotion-0.1.1-overlay.patch
Patch1: flumotion-0.1.1-firewire.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires(post): openssl
Requires: python >= 2.3
Requires: gstreamer >= 0.8.5
Requires: gstreamer-python >= 0.7.93
Requires: python-twisted >= 1.3.0
Requires: pygtk2 >= 2.4.0
Requires: python-imaging
BuildRequires: pkgconfig
BuildRequires: gstreamer-devel >= 0.8.5, gstreamer-python >= 0.7.93
BuildRequires: python, python-devel >= 2.3, python-twisted >= 1.3.0
BuildRequires: pygtk2-devel >= 2.4.0
BuildRequires: epydoc
BuildArch: noarch

%description
Fluendo Streaming Server.


%prep
%setup -q
%patch0 -p0 -b .overlay
%patch1 -p0 -b .firewire


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__mkdir_p} %{buildroot}%{_sysconfdir}/flumotion/managers/default/flows
%{__mkdir_p} %{buildroot}%{_sysconfdir}/flumotion/workers

# Install init script
%{__install} -D -m 0755 doc/redhat/init.d/flu-manager \
    %{buildroot}%{_sysconfdir}/rc.d/init.d/flu-manager
%{__install} -D -m 0755 doc/redhat/init.d/flu-worker \
    %{buildroot}%{_sysconfdir}/rc.d/init.d/flu-worker

# Install sysconfig files
%{__install} -D -m 0644 doc/redhat/sysconfig/flumotion-manager \
    %{buildroot}%{_sysconfdir}/sysconfig/flumotion-manager
%{__install} -D -m 0644 doc/redhat/sysconfig/flumotion-worker \
    %{buildroot}%{_sysconfdir}/sysconfig/flumotion-worker

# Create a .flumotion in the new home
# FIXME: needs to be done more gracefully
%{__mkdir_p} %{buildroot}%{_datadir}/flumotion/.flumotion

# Create log directory
%{__mkdir_p} %{buildroot}%{_var}/log/flumotion


%clean
%{__rm} -rf %{buildroot}


%pre
/usr/sbin/useradd -s /sbin/nologin -r -d %{_datadir}/flumotion -M -r \
    flumotion >/dev/null 2>&1 || :

%post
/sbin/chkconfig --add flu-manager
/sbin/chkconfig --add flu-worker
# Generate a default .pem certificate
PEM_FILE="%{_sysconfdir}/flumotion/managers/default/default.pem"
if ! test -e ${PEM_FILE}; then
    sh %{_datadir}/ssl/certs/make-dummy-cert ${PEM_FILE}
    chgrp flumotion ${PEM_FILE}
    chmod 640 ${PEM_FILE}
fi

# If we have no .xml file in the default manager, create one
# The default account is user/test (only listens on localhost, don't panic!)
if ! ls %{_sysconfdir}/flumotion/managers/default/*.xml >/dev/null 2>&1; then
    cat > %{_sysconfdir}/flumotion/managers/default/planet.xml << EOF
<planet>

  <manager>
    <component name="manager-bouncer" type="htpasswdcrypt">
      <data><![CDATA[
user:PSfNpHTkpTx1M
]]></data>
    </component>
  </manager>

</planet>
EOF
fi

%preun
if [ $1 -eq 0 ]; then
    /sbin/service flu-manager stop >/dev/null 2>&1
    /sbin/service flu-worker stop >/dev/null 2>&1
    /sbin/chkconfig --del flu-manager
    /sbin/chkconfig --del flu-worker
fi


%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING README AUTHORS
%doc conf/ doc/reference/html/
%{_sysconfdir}/rc.d/init.d/flu-manager
%{_sysconfdir}/rc.d/init.d/flu-worker
%attr(0750, flumotion, flumotion) %{_sysconfdir}/flumotion/
%config(noreplace) %{_sysconfdir}/sysconfig/flumotion-manager
%config(noreplace) %{_sysconfdir}/sysconfig/flumotion-worker
%{_bindir}/flumotion-admin
%{_bindir}/flumotion-manager
%{_bindir}/flumotion-tester
%{_bindir}/flumotion-worker
%{_libdir}/flumotion/
%{_datadir}/flumotion/
%dir %attr(0750, flumotion, flumotion) %{_datadir}/flumotion/.flumotion
%dir %attr(0750, flumotion, flumotion) %{_var}/log/flumotion/


%changelog
* Tue Oct 26 2004 Matthias Saou <http://freshrpms.net/> 0.1.1-0
- Update to 0.1.1.
- Added Johan's quick overlay fix.

* Thu Oct 21 2004 Matthias Saou <http://freshrpms.net/> 0.1.0-0
- Picked up, minor changes.

* Mon Jun 07 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- first package

