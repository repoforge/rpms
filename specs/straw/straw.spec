# $Id$

# Authority: dag
# Upstream: Juri Pakaste <juri@iki.fi>

### FIXME: Makefiles don't allow -jX (parallel compilation)
# Distcc: 0

Summary: desktop news aggregator for GNOME
Name: straw
Version: 0.22.1
Release: 1
License: GPL
Group: Applications/Internet
URL: http://www.nongnu.org/straw/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://savannah.nongnu.org/download/straw/straw.pkg/%{version}/straw-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: python >= 2.2, gtk2 >= 2.0, libglade2 >= 2.0
BuildRequires: python-adns, python-bsddb3, libxml2-python >= 1.99.13
BuildRequires: pyorbit, pygtk2 >= 1.99.13, pygtk2-libglade
BuildRequires: gnome-python2-gtkhtml2, gnome-python2-gconf, gnome-python2-gnomevfs

Requires: python >= 2.2, gtk2 >= 2.0, libglade2 >= 2.0
Requires: libxml2-python >= 1.99.13, python-adns, python-bsddb3, mx
Requires: gnome-python2-gconf, gnome-python2-gnomevfs, pyorbit, pygtk2 >= 1.99.13

%description
Straw is a desktop news aggregator for the GNOME environment. Its aim
is to be a faster, easier and more accessible way to read news and
blogs than the traditional browser.

%prep
%setup

%build
#%{__make} %{?_smp_mflags}
python setup.py build

%install
%{__rm} -rf %{buildroot}
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
python setup.py install \
	--prefix="%{buildroot}%{_prefix}" \
	--sysconfdir="%{buildroot}%{_sysconfdir}"
%find_lang %{name}

desktop-file-install --vendor gnome --delete-original \
	--add-category X-Red-Hat-Base                 \
	--dir %{buildroot}%{_datadir}/applications    \
	%{buildroot}%{_datadir}/applications/*.desktop

%post
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas &>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%config %{_sysconfdir}/gconf/schemas/*.schemas
%{_bindir}/*
%{_libdir}/python*/site-packages/straw/
%{_datadir}/straw/
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.png

%changelog
* Sat Feb 28 2004 Dag Wieers <dag@wieers.com> - 0.22.1-1
- RH9 and RHFC1 ship with mx, change dependency. (Gary Peck)

* Wed Feb 25 2004 Dag Wieers <dag@wieers.com> - 0.22.1-0
- Updated to release 0.22.1.

* Wed Feb 18 2004 Dag Wieers <dag@wieers.com> - 0.22-0
- Updated to release 0.22.

* Sat Dec 20 2003 Dag Wieers <dag@wieers.com> - 0.21.1-1
- Added missing python dependencies. (Pavels)

* Sun Nov 23 2003 Dag Wieers <dag@wieers.com> - 0.21.1-0
- Updated to release 0.21.1.

* Sat Nov 01 2003 Dag Wieers <dag@wieers.com> - 0.19.2-0
- Updated to release 0.19.2.

* Thu Aug 21 2003 Dag Wieers <dag@wieers.com> - 0.19.1-0
- Updated to release 0.19.1.

* Sun Aug 17 2003 Dag Wieers <dag@wieers.com> - 0.19-0
- Updated to release 0.19.

* Sun Aug 03 2003 Dag Wieers <dag@wieers.com> - 0.18.1-0
- Updated to release 0.18.1.
- Added warning for threaded pygtk2.

* Thu Feb 20 2003 Dag Wieers <dag@wieers.com> - 0.16-0
- Initial package. (using DAR)
