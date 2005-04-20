# $Id$
# Authority: matthias

Summary: Fluendo Streaming Server
Name: flumotion
Version: 0.1.7
Release: 1
Group: Applications/Internet
License: GPL
URL: http://www.fluendo.com/
Source: http://www.flumotion.net/src/flumotion/flumotion-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires(post): openssl
Requires: python >= 2.3
Requires: gstreamer >= 0.8.5
Requires: gstreamer-python >= 0.7.93
Requires: python-twisted >= 1.3.0
Requires: pygtk2 >= 2.4.0
Requires: python-imaging
BuildRequires: gstreamer-devel >= 0.8.5, gstreamer-python >= 0.7.93
BuildRequires: python-devel >= 2.3, python-twisted >= 1.3.0
BuildRequires: pygtk2-devel >= 2.4.0
BuildRequires: epydoc
BuildRequires: gcc-c++
BuildArch: noarch

%description
Fluendo Streaming Server.


%prep
%setup -q


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__mkdir_p} %{buildroot}%{_sysconfdir}/flumotion/managers/default/flows
%{__mkdir_p} %{buildroot}%{_sysconfdir}/flumotion/workers

# Install init script
%{__install} -Dp -m 0755 doc/redhat/flumotion \
    %{buildroot}%{_sysconfdir}/rc.d/init.d/flumotion

# Create a .flumotion in the new home
# FIXME: needs to be done more gracefully
%{__mkdir_p} %{buildroot}%{_datadir}/flumotion/.flumotion

# Create log directory
%{__mkdir_p} %{buildroot}%{_var}/cache/flumotion
%{__mkdir_p} %{buildroot}%{_var}/log/flumotion
%{__mkdir_p} %{buildroot}%{_var}/run/flumotion


%clean
%{__rm} -rf %{buildroot}


%pre
/usr/sbin/useradd -s /sbin/nologin -r -d %{_datadir}/flumotion -M -r \
    flumotion &>/dev/null || :

%post
/sbin/chkconfig --add flumotion
# Generate a default .pem certificate
PEM_FILE="%{_sysconfdir}/flumotion/default.pem"
if ! test -e ${PEM_FILE}; then
    sh %{_datadir}/ssl/certs/make-dummy-cert ${PEM_FILE}
    chgrp flumotion ${PEM_FILE}
    chmod 640 ${PEM_FILE}
fi

# If we have no manager or worker configuration, create the defaults
# The default account is user/test (only listens on localhost, don't panic!)
#if ! (ls %{_sysconfdir}/flumotion/managers/*/*.xml || %{_sysconfdir}/flumotion/workers/*.xml) >/dev/null 2>&1; then
#    test -d %{_sysconfdir}/flumotion/managers/default || \
#        mkdir -p %{_sysconfdir}/flumotion/managers/default
#    cat > %{_sysconfdir}/flumotion/managers/default/planet.xml << EOF
#<planet>
#
#  <manager>
#    <component name="manager-bouncer" type="htpasswdcrypt">
#      <!-- user / test -->
#      <data><![CDATA[
#user:PSfNpHTkpTx1M
#]]></data>
#    </component>
#  </manager>
#
#</planet>
#EOF
#
#    cat > %{_sysconfdir}/flumotion/workers/default.xml << EOF
#<worker>
#
#  <manager>
#  </manager>
#
#  <authentication type="plaintext">
#    <username>user</username>
#    <password>test</password>
#  </authentication>
#
#</worker>
#EOF
#fi

%preun
if [ $1 -eq 0 ]; then
    /sbin/service flumotion stop >/dev/null 2>&1
    /sbin/chkconfig --del flumotion
fi

%postun
if [ $1 -eq 0 ]; then
    %{__rm} -rf %{_var}/lock/flumotion/
    %{__rm} -rf %{_var}/run/flumotion/
fi


%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING README AUTHORS
%doc conf/ doc/reference/html/
%{_sysconfdir}/rc.d/init.d/flumotion
%attr(0750, flumotion, flumotion) %{_sysconfdir}/flumotion/
%{_bindir}/flumotion-admin
%{_bindir}/flumotion-manager
%{_bindir}/flumotion-tester
%{_bindir}/flumotion-worker
%{_sbindir}/flumotion
%{_libdir}/flumotion/
%{_datadir}/applications/flu-admin.desktop
%{_datadir}/flumotion/
%{_datadir}/pixmaps/flumotion.png
%dir %attr(0750, flumotion, flumotion) %{_datadir}/flumotion/.flumotion
%{_libdir}/pkgconfig/flumotion.pc
%dir %attr(0750, flumotion, flumotion) %{_var}/cache/flumotion/
%dir %attr(0750, flumotion, flumotion) %{_var}/log/flumotion/
%dir %attr(0750, flumotion, flumotion) %{_var}/run/flumotion/


%changelog
* Sat Apr  9 2005 Matthias Saou <http://freshrpms.net/> 0.1.7-1
- Update to 0.1.7.

* Thu Feb 24 2005 Matthias Saou <http://freshrpms.net/> 0.1.6-3
- Update to 0.1.6.
- Don't create the default manager & worker for now, it's annoying on updates.

* Sun Dec 19 2004 Matthias Saou <http://freshrpms.net/> 0.1.4-0
- Update to 0.1.4.

* Mon Nov 29 2004 Matthias Saou <http://freshrpms.net/> 0.1.3.1-0
- Update to 0.1.3.1.

* Tue Oct 26 2004 Matthias Saou <http://freshrpms.net/> 0.1.1-0
- Update to 0.1.1.
- Added Johan's quick overlay fix.

* Thu Oct 21 2004 Matthias Saou <http://freshrpms.net/> 0.1.0-0
- Picked up, minor changes.

* Mon Jun 07 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- first package

