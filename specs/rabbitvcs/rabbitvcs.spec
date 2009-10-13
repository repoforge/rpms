# $Id$
# Authority: shuff
# Upstream: Bruce van der Kooij <brucevdkooij$gmail,com>

## ExcludeDist: el3 el4

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')
%define python_version %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')
%define nautilus_extensiondir %(pkg-config --variable=extensiondir libnautilus-extension)

Summary: Nautilus integration for Subversion
Name: rabbitvcs
Version: 0.12
Release: 1
License: GPL
Group: Development/Libraries
URL: http://rabbitvcs.org

Source: http://rabbitvcs.googlecode.com/files/rabbitvcs-%{version}.tar.gz
Patch0: rabbitvcs-0.12_nautilusold.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#BuildArch: noarch
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: nautilus-python-devel = 0.5.0
BuildRequires: pysvn
BuildRequires: neon-devel
BuildRequires: pygtk2-devel
BuildRequires: python-devel
BuildRequires: subversion-devel >= 1.6.5
Requires: meld
Requires: nautilus-python = 0.5.0
Requires: neon 
Requires: pygtk2 
Requires: pysvn 
Requires: python 
Requires: python-configobj >= 4.6.0
Requires: subversion >= 1.6.5
Requires: %{_iconsbasedir}

Conflicts: nautilussvn
Obsoletes: nautilussvn

%description
TortoiseSVN-like GUI integration for Subversion (and other VCS) and Nautilus.

%prep
%setup
%patch0 -p1

# statuschecker.py cannot work with RHEL5
%{__rm} -f rabbitvcs/statuschecker.py
%{__rm} -rf rabbitvcs/dbus
%{__rm} -rf rabbitvcs/data/icons/hicolor/scalable/actions/rabbitvcs-dbus.svg

%build
CFLAGS="%{optflags}" %{__python} setup.py build


%install
%{__rm} -rf %{buildroot}
CFLAGS="%{optflags}" %{__python} setup.py install --root="%{buildroot}" --prefix="%{_prefix}"

# you do not know where to put the documents, i will handle it
%{__rm} -rf %{buildroot}%{_defaultdocdir}/%{name}

# update-notifier is just for Ubuntu
%{__rm} -rf %{buildroot}%{_datadir}/%{name}

%clean
%{__rm} -rf %{buildroot}

%post
/usr/bin/gtk-update-icon-cache -f /usr/share/icons/hicolor >/dev/null 2>&1

%postun
/usr/bin/gtk-update-icon-cache -f /usr/share/icons/hicolor >/dev/null 2>&1

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING MAINTAINERS 
%{python_sitearch}/*
%{_bindir}/*
%dir %{nautilus_extensiondir}
%{nautilus_extensiondir}/*
%dir %{_iconsbasedir}/scalable/actions/
%{_iconsbasedir}/scalable/actions/*
%dir %{_iconsbasedir}/scalable/emblems/
%{_iconsbasedir}/scalable/emblems/*
%{_iconsscaldir}/*
%dir %{_datadir}/locale/*/LC_MESSAGES/
%{_datadir}/locale/*/LC_MESSAGES/*

%changelog
* Thu Oct 08 2009 Steve Huff <shuff@vecna.org> - 0.12-1
- Initial package.

