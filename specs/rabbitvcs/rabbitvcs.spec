# $Id$
# Authority: shuff
# Upstream: Bruce van der Kooij <brucevdkooij$gmail,com>

## ExcludeDist: el3 el4

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')
%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(0)')
%define nautilus_extensiondir %(pkg-config --variable=extensiondir libnautilus-extension)
%define gedit_extensiondir %{_libdir}/gedit-2/plugins

Summary: Nautilus integration for Subversion
Name: rabbitvcs
Version: 0.13.1
Release: 1%{?dist}
License: GPL
Group: Development/Libraries
URL: http://rabbitvcs.org

Source: http://rabbitvcs.googlecode.com/files/rabbitvcs-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
# BuildArch: noarch

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: python-nautilus-devel = 0.5.0
BuildRequires: neon-devel
BuildRequires: dbus-python
BuildRequires: pygobject2-devel
BuildRequires: pygtk2-devel
BuildRequires: python-devel
BuildRequires: python-svn
BuildRequires: subversion-devel >= 1.6.5
Requires: meld
Requires: neon 
Requires: dbus-python
Requires: pygobject2
Requires: pygtk2 
Requires: python 
Requires: python-configobj >= 4.6.0
Requires: python-svn 
Requires: subversion >= 1.6.5
Requires: %{_iconsbasedir}

Conflicts: nautilussvn
Obsoletes: nautilussvn

%description
TortoiseSVN-like GUI integration for Subversion (and other VCS) and Nautilus.

%package nautilus
Summary: Nautilus integration for RabbitVCS
Group: Development/Tools

Requires: %{name} = %{version}-%{release}
Requires: python-nautilus = 0.5.0

%description nautilus
Install this package to use RabbitVCS with the Nautilus file manager.

%package gedit
Summary: Nautilus integration for Gedit
Group: Development/Tools

Requires: %{name} = %{version}-%{release}
Requires: gedit

%description gedit
Install this package to use RabbitVCS with the Gedit text editor.

%prep
%setup -n rabbitvcs-%{version}

%build
CFLAGS="%{optflags}" %{__python} setup.py build

# rename to avoid collision
%{__mv} clients/cli/README clients/cli/README.cli

%install
%{__rm} -rf %{buildroot}
CFLAGS="%{optflags}" %{__python} setup.py install --root="%{buildroot}" --prefix="%{_prefix}"

# install command-line extension
%{__install} -m0755 -d %{buildroot}%{_bindir}
%{__install} -m0755 clients/cli/rabbitvcs %{buildroot}%{_bindir}

# install nautilus extension
%{__install} -m0755 -d %{buildroot}%{nautilus_extensiondir}/python
%{__install} -m0755 clients/nautilusold/RabbitVCS.py %{buildroot}%{nautilus_extensiondir}/python

# install Gedit extension
%{__install} -m0755 -d %{buildroot}%{gedit_extensiondir}
%{__install} -m0755 clients/gedit/rabbitvcs* %{buildroot}%{gedit_extensiondir}

# you do not know where to put the documents, i will handle it
%{__rm} -rf %{buildroot}%{_defaultdocdir}/%{name}

# update-notifier is just for Ubuntu
%{__rm} -f %{buildroot}%{_datadir}/%{name}/*.update-notifier
%{__rm} -f %{buildroot}%{_datadir}/%{name}/do-rabbitvcs-restart-nautilus

%clean
%{__rm} -rf %{buildroot}

%post
/usr/bin/gtk-update-icon-cache -f /usr/share/icons/hicolor >/dev/null 2>&1

%postun
/usr/bin/gtk-update-icon-cache -f /usr/share/icons/hicolor >/dev/null 2>&1

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING MAINTAINERS README
%doc clients/cli/README.cli
%{_bindir}/*
%{python_sitelib}/*
%dir %{_iconsbasedir}/scalable/actions/
%{_iconsbasedir}/scalable/actions/*
%dir %{_iconsbasedir}/scalable/emblems/
%{_iconsbasedir}/scalable/emblems/*
%{_iconsscaldir}/*
%dir %{_datadir}/locale/*/LC_MESSAGES/
%{_datadir}/locale/*/LC_MESSAGES/*
%{_datadir}/rabbitvcs

%files nautilus
%doc clients/nautilusold/README
%dir %{nautilus_extensiondir}
%{nautilus_extensiondir}/*

%files gedit
%doc clients/gedit/README
%dir %{gedit_extensiondir}
%{gedit_extensiondir}/*

%changelog
* Sun Mar 28 2010 Caghan Demirci <caghand@superonline.com> - 0.13.1-1
- Updated to version 0.13.1.
- Split out some clients into separate packages.

* Tue Dec 01 2009 Steve Huff <shuff@vecna.org> - 0.12.1-1
- Updated to version 0.12.1.
- Now source directly from the old-distros tarball, no more patching.

* Thu Oct 08 2009 Steve Huff <shuff@vecna.org> - 0.12-1
- Initial package.

