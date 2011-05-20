# $Id$
# Authority: shuff
# Upstream: Chris Jones <cmsj$tenshu,net>
# ExcludeDist: el3 el4
# Rationale: needs python-configobj

%define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")

Summary: Arrange terminals in grids
Name: terminator
Version: 0.95
Release: 3%{?dist}
License: GPL
Group: User Interface/Desktops
URL: http://www.tenshu.net/terminator/ 

Source: http://launchpad.net/terminator/trunk/%{version}/+download/terminator-%{version}.tar.gz
Patch0: terminator-vte-el5-font-fix.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Buildarch: noarch
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: gtk2-devel
BuildRequires: intltool
BuildRequires: python-devel
BuildRequires: rpm-macros-rpmforge
Requires: desktop-file-utils
Requires: GConf2
Requires: gnome-python2-gconf
Requires: gtk2
Requires: python-configobj
Requires: vte
%{!?el6:Requires: python-configobj}
# uncomment this once python-keybinder is packaged
# %{?el6:Requires: python-keybinder}

%description
Terminator is inspired by programs such as gnome-multi-term, quadkonsole, etc.
in that the main focus is arranging terminals in grids (tabs is the most common
default method, which Terminator also supports).

Much of the behaviour of Terminator is based on GNOME Terminal, and we are
adding more features from that as time goes by, but we also want to extend out
in different directions with useful features for sysadmins and other users.

%prep
%setup
%{?el5:%patch0}
%{__sed} -i '/#! \?\/usr.*/d' terminatorlib/*.py


%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

%{__rm} -f %{buildroot}/%{_datadir}/icons/hicolor/icon-theme.cache
%{__rm} -f %{buildroot}/%{_datadir}/applications/%{name}.desktop

desktop-file-install --vendor "" \
    --remove-category X-Ubuntu-Gettext-Domain \
    --dir %{buildroot}%{_datadir}/applications \
    data/%{name}.desktop

%clean
%{__rm} -rf %{buildroot}

%post -p %{_bindir}/gtk-update-icon-cache

%postun -p %{_bindir}/gtk-update-icon-cache

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING INSTALL README
%doc %{_mandir}/man?/*
%{_bindir}/*
%{python_sitelib}/*
%{_datadir}/applications/*.desktop
%{_datadir}/locale/*/LC_MESSAGES/terminator.mo
%{_datadir}/pixmaps/*.png
%{_iconsbasedir}/*/*/*.png
%{_iconsbasedir}/*/*/*.svg

%changelog
* Fri May 20 2011 Steve Huff <shuff@vecna.org> - 0.95-3
- Included Mike Miller's VTE font fix for el5 (bug#690191)
- Captured build dependency on intltool.

* Tue Dec 07 2010 Steve Huff <shuff@vecna.org> - 0.95-2
- Captured Python dependencies more precisely.

* Fri Dec 03 2010 Steve Huff <shuff@vecna.org> - 0.95
- Initial package.
