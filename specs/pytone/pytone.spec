# $Id$
# Authority: dag
# Upstream: Joerg Lehmann <joerg@luga.de>
# Upstream: <pytone-users@luga.de>

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define real_name PyTone

Summary: Music Jukebox with a Curses Based GUI
Name: pytone
Version: 3.0.2
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://www.luga.de/pytone/

Source: http://www.luga.de/pytone/download/PyTone-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python, python-devel, python-sqlite2, libao-devel
Requires: python, python-ao, python-mad, python-ogg, python-sqlite2, python-vorbis
#Requires: python-xmms, python-eyed3

%description
PyTone is a music jukebox written in Python with a curses based GUI.
While providing advanced features like crossfading and multiple
players, special emphasis is put on ease of use, turning PyTone into
an ideal jukebox system for use at parties.

%prep
%setup -n %{real_name}-%{version}

%{__cat} <<'EOF' >pytone.sh
#!/bin/sh
exec %{__python} %{python_sitearch}/pytone/pytone.py $@
EOF

%{__cat} <<'EOF' >pytonectl.sh
#!/bin/sh
exec %{__python} %{python_sitearch}/pytone/pytonectl.py $@
EOT

%build
export CFLAGS="%{optflags}"
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --root="%{buildroot}" --prefix="%{_prefix}"
%find_lang %{real_name}

%{__install} -Dp -m0755 pytone.sh %{buildroot}%{_bindir}/pytone
%{__install} -Dp -m0755 pytonectl.sh %{buildroot}%{_bindir}/pytonectl
%{__install} -Dp -m0644 conf/pytonerc %{buildroot}%{_sysconfdir}/pytonerc

%clean
%{__rm} -rf %{buildroot}

%files -f %{real_name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README THANKS TODO
%config(noreplace) %{_sysconfdir}/pytonerc
%{_bindir}/pytone
%{_bindir}/pytonectl
%{python_sitearch}/pytone/

%changelog
* Sat Jun 06 2009 Dag Wieers <dag@wieers.com> - 3.0.2-1
- Updated to release 3.0.2.

* Thu Aug 16 2007 Dag Wieers <dag@wieers.com> - 3.0.1-1
- Updated to release 3.0.1.

* Sat Aug 12 2006 Dag Wieers <dag@wieers.com> - 2.3.1-1
- Updated to release 2.3.0.

* Wed Sep 14 2005 Dag Wieers <dag@wieers.com> - 2.3.0-1
- Updated to release 2.3.0.

* Tue Aug 23 2005 Dag Wieers <dag@wieers.com> - 2.2.4-1
- Updated to release 2.2.4.

* Sun May 08 2005 Dag Wieers <dag@wieers.com> - 2.2.3-1
- Initial package. (using DAR)
