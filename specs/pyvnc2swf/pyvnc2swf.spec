# $Id$
# Authority: dag
# Upstream: <vnc2swf-users$lists,sourceforge,net>
# Upstream: Yusuke Shinyama <yusuke$cs,nyu,edu>

Summary: Flash movie recording tool for VNC
Name: pyvnc2swf
Version: 0.9.3
Release: 1%{?dist}
Summary: A VNC session recorder to Flash movie
License: GPL
Group: User Interface/Desktops
URL: http://www.unixuser.org/~euske/vnc2swf/

Source: http://www.unixuser.org/~euske/vnc2swf/pyvnc2swf-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python-devel >= 2.4
Requires: python >= 2.4, python-game >= 1.6
BuildArch: noarch

%description
pyvnc2swf is a screen recorder for Flash movie. It captures
screen motion through  VNC protocol and converts it into a
Shockwave Flash (SWF) file.

%prep
%setup

%{__cat} <<'EOF' >pyvnc2swf.sh
#!/bin/sh
PYTHONPATH=${PYTHONPATH-}${PYTHONPATH+:}%{_datadir}/pyvnc2swf %{__python} %{_datadir}/pyvnc2swf/vnc2swf.py $@
EOF

%{__cat} <<'EOF' >pyvnc2swf-edit.sh
#!/bin/sh
PYTHONPATH=${PYTHONPATH-}${PYTHONPATH+:}%{_datadir}/pyvnc2swf %{__python} %{_datadir}/pyvnc2swf/edit.py $@
EOF

%{__cat} <<'EOF' >pyvnc2swf-play.sh
#!/bin/sh
PYTHONPATH=${PYTHONPATH-}${PYTHONPATH+:}%{_datadir}/pyvnc2swf %{__python} %{_datadir}/pyvnc2swf/play.py $@
EOF

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 pyvnc2swf.sh %{buildroot}%{_bindir}/pyvnc2swf
%{__install} -Dp -m0755 pyvnc2swf-edit.sh %{buildroot}%{_bindir}/pyvnc2swf-edit
%{__install} -Dp -m0755 pyvnc2swf-play.sh %{buildroot}%{_bindir}/pyvnc2swf-play
%{__install} -Dp -m0755 bin/recordwin.sh %{buildroot}%{_bindir}/recordwin

%{__install} -d -m0755 %{buildroot}%{_datadir}/pyvnc2swf/
%{__install} -m0644 pyvnc2swf/*.py %{buildroot}%{_datadir}/pyvnc2swf/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0775)
%doc LICENCE.TXT *.txt docs/*.html
%{_bindir}/pyvnc2swf
%{_bindir}/pyvnc2swf-edit
%{_bindir}/pyvnc2swf-play
%{_bindir}/recordwin
%{_datadir}/pyvnc2swf/

%changelog
* Thu May 10 2007 Dag Wieers <dag@wieers.com> - 0.9.3-1
- Updated to release 0.9.3.

* Sun Nov 12 2006 Dag Wieers <dag@wieers.com> - 0.9.1-1
- Updated to release 0.9.1.

* Sun Nov 12 2006 Dag Wieers <dag@wieers.com> - 0.5.0-2
- Removed ming requirement.

* Fri Nov 11 2005 Dries Verachtert <dries@ulyssis.org> - 0.5.0-1
- Updated to release 0.5.0.

* Tue Mar 15 2005 Dag Wieers <dag@wieers.com> - 0.4.2-2
- Build against newer ming.

* Thu Mar 10 2005 Dag Wieers <dag@wieers.com> - 0.4.2-2
- Updated to release 0.4.2.

* Fri May 14 2004 Dag Wieers <dag@wieers.com> - 0.4.1-1
- Initial package. (using DAR)
