# $Id$
# Authority: dag
# Upstream: Juri Pakaste <juri$iki,fi>

### FIXME: Makefiles don't allow -jX (parallel compilation)
# Distcc: 0


Summary: desktop news aggregator for GNOME
Name: straw
Version: 0.21.1
Release: 2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.gnome.org/projects/straw/

Source: http://savannah.nongnu.org/download/straw/straw.pkg/%{version}/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python >= 2.2, gtk2 >= 2.0, libglade2 >= 2.0
BuildRequires: adns, libxml2-python >= 1.99.13
#BuildRequires: pyorbit, pygtk2 >= 1.99.13

Requires: python >= 2.2, gtk2 >= 2.0, libglade2 >= 2.0
Requires: libxml2-python >= 1.99.13, python-adns, python-bsddb3, mx

%{?fc1:Requires: pyorbit, pygtk2 >= 1.99.13, gnome-python2-gnomevfs, gnome-python2-gconf}
%{?el3:Requires: pyorbit, pygtk2 >= 1.99.13, gnome-python2-gnomevfs, gnome-python2-gconf}
%{?rh9:Requires: pyorbit, pygtk2 >= 1.99.13, gnome-python2-gnomevfs, gnome-python2-gconf}
%{?rh8:Requires: orbit-python, pygtk2 >= 1.99.12, gnome-python2-gconf}

%description
Straw is a desktop news aggregator for the GNOME environment. Its aim
is to be a faster, easier and more accessible way to read news and
blogs than the traditional browser.

%prep
%setup

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_datadir}/pixmaps/
%makeinstall \
	PREFIX="%{buildroot}%{_prefix}" \
	SYSCONFDIR="%{buildroot}%{_sysconfdir}"
%find_lang %{name}

desktop-file-install --vendor gnome --delete-original \
	--add-category X-Red-Hat-Base                 \
	--dir %{buildroot}%{_datadir}/applications    \
	%{buildroot}%{_datadir}/applications/*.desktop

#%post
#%{__cat} <<EOF
#WARNING: You need to have a special pygtk2 version that enables threading
#to make straw work. (This is not shipped with Red Hat)
#However, the next release of straw will not have this special requirement.
#EOF

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%config %{_sysconfdir}/gconf/schemas/*.schemas
%{_bindir}/*
%{_libdir}/python2.2/site-packages/straw/
%{_datadir}/straw/
%{_datadir}/applications/*
%{_datadir}/pixmaps/*

%changelog
* Mon Mar 01 2004 Dag Wieers <dag@wieers.com> - 0.21.1-2
- Changed dependency from python-mx-base to mx. (Raphael Clifford)

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
