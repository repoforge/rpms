# $Id$
# Authority: dries
# Upstream: <vkleinde$yahoo,de>

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(0)')

Summary: GUI for yum
Name: guyum
Version: 0.4.1
Release: 1%{?dist}
License: GPL
Group: System Environment/Base
URL: http://www.guyum.de/

Source: http://dl.sf.net/guyum/guyum-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk2-devel

%description
GuYum is a GUI for Yum. It has a multi-tabbed search interface. Repositories 
can be enabled/disabled per search request. It is written in C with GTK+.

%prep
%setup
%{__cat} <<'EOF' >guyum.sh
#!/bin/sh
python /usr/share/guyum/gymain.py
EOF

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"
%{__install} -Dp -m0755 guyum.sh %{buildroot}%{_bindir}/guyum.sh

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%{_sysconfdir}/pam.d/guyum
%{_sysconfdir}/security/console.apps/guyum
%{_bindir}/guyum.sh
%{_datadir}/guyum/
%{_datadir}/applications/*guyum.desktop
%{python_sitelib}/guyum/

%changelog
* Wed Oct  3 2007 Dries Verachtert <dries@ulyssis.org> - 0.4.1-1
- Updated to release 0.4.1.

* Fri Apr 20 2007 Dries Verachtert <dries@ulyssis.org> - 0.3.1-1
- Initial package.
