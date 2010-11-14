# $Id$
# Authority: dag

# Tag: rft

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define real_name PyTone

Summary: Music Jukebox with a Curses Based GUI
Name: pytone
Version: 2.3.0
Release: 0.pre1%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://www.luga.de/pytone/

Source: http://www.luga.de/pytone/download/PyTone-%{version}-pre1.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python, python-devel
Requires: python, python-ao, python-mad, python-ogg, python-vorbis
#Requires: python-xmms, python-eyed3

%description
PyTone is a music jukebox written in Python with a curses based GUI.
While providing advanced features like crossfading and multiple
players, special emphasis is put on ease of use, turning PyTone into
an ideal jukebox system for use at parties.

%prep
%setup -n %{real_name}-%{version}-pre1

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
%{__python} setup.py install --root="%{buildroot}"
%find_lang %{real_name}

%{__install} -Dp -m0755 pytone.sh %{buildroot}%{_bindir}/pytone
%{__install} -Dp -m0755 pytonectl.sh %{buildroot}%{_bindir}/pytonectl

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
* Tue Aug 23 2005 Dag Wieers <dag@wieers.com> - 2.3.0-0.pre1
- Updated to release 2.3.0-pre1.

* Tue Aug 23 2005 Dag Wieers <dag@wieers.com> - 2.2.4-1
- Updated to release 2.2.4.

* Sun May 08 2005 Dag Wieers <dag@wieers.com> - 2.2.3-1
- Initial package. (using DAR)
