# $Id$
# Authority: dag
# Upstream: Lars Lindner <llando$gmx,de>
# Upstream: Nathan J. Conrad <t98502$users,sourceforge,net>

Summary: RSS/RDF feed reader
Name: liferea
Version: 0.5.2
Release: 0.c
License: GPL
Group: Applications/Internet
URL: http://liferea.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/liferea/liferea-%{version}c.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: GConf2-devel >= 2.2, gtkhtml2-devel, libxml2-devel >= 2.5.10
BuildRequires: gettext

%description
Liferea (Linux Feed Reader) is an RSS/RDF feed reader. 
It's intended to be a clone of the Windows-only FeedReader. 
It can be used to maintain a list of subscribed feeds, 
browse through their items, and show their contents 
using GtkHTML.

%prep
%setup -n %{name}-%{version}c

%{__cat} <<'EOF' >liferea.sh
#!/bin/bash

[ -f "$MOZILLA_FIVE_HOME/chrome/comm.jar" ] || export MOZILLA_FIVE_HOME="%{_libdir}/mozilla-1.6"
[ -f "$MOZILLA_FIVE_HOME/chrome/comm.jar" ] || export MOZILLA_FIVE_HOME="%{_libdir}/mozilla-1.7"
[ -f "$MOZILLA_FIVE_HOME/chrome/comm.jar" ] || export MOZILLA_FIVE_HOME="%{_libdir}/mozilla"

export LD_LIBRARY_PATH="$MOZILLA_FIVE_HOME:$LD_LIBRARY_PATH"
export MOZ_PLUGIN_PATH="$MOZ_PLUGIN_PATH:%{_libdir}/mozilla/plugins:$MOZILLA_FIVE_HOME/plugins"

exec %{_bindir}/liferea-bin $@
EOF

%build
%configure \
	--x-libraries="%{_prefix}/X11R6/%{_lib}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%{__install} -D -m0755 liferea.sh %{buildroot}%{_bindir}/liferea

desktop-file-install --vendor gnome --delete-original \
	--add-category X-Red-Hat-Base                 \
	--dir %{buildroot}%{_datadir}/applications    \
	%{buildroot}%{_datadir}/applications/liferea.desktop

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/liferea/
%{_datadir}/pixmaps/*.png
%{_libdir}/liferea/*.so*
%exclude %{_libdir}/liferea/*.la

%changelog
* Mon Aug 02 2004 Dag Wieers <dag@wieers.com> - 0.5.2-0.c
- Updated to release 0.5.2c.

* Sun Jul 24 2004 Dag Wieers <dag@wieers.com> - 0.5.2-0.b
- Updated to release 0.5.2b.

* Thu Jul 01 2004 Dag Wieers <dag@wieers.com> - 0.5.1-1
- Updated to release 0.5.1.

* Sun Jun 20 2004 Dag Wieers <dag@wieers.com> - 0.5.0-1
- Updated to release 0.5.0.

* Sun May 23 2004 Dag Wieers <dag@wieers.com> - 0.4.9-1
- Updated to release 0.4.9.

* Tue May 11 2004 Dag Wieers <dag@wieers.com> - 0.4.8-2
- Added patch for building on RH90 and RHEL3. (Nathan Conrad)

* Fri May 07 2004 Dag Wieers <dag@wieers.com> - 0.4.8-1
- Initial package. (using DAR)
