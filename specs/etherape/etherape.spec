# $Id$
# Authority: dag

%{?dist: %{expand: %%define %dist 1}}

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}

%define desktop_vendor rpmforge

Summary: Graphical network viewer modeled after etherman
Name: etherape
Version: 0.9.1
Release: 1
License: GPL
Group: Applications/System
URL: http://etherape.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/etherape/etherape-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libpcap, gcc-c++, pkgconfig, libglade2-devel, libgnomeui-devel
BuildRequires: gettext

%description
Etherape is a graphical network monitor for Unix modeled after
etherman. Featuring ether, ip and tcp modes, it displays network
activity graphically. Hosts and links change in size with traffic. 
Color coded protocols display. It supports ethernet, ppp and slip 
devices. It can filter traffic to be shown, and can read traffic 
from a file as well as live from the network. 

%prep
%setup

#%{__perl} -pi.orig -e 's|(\${exec_prefix})/lib|$1/%{_lib}|g' configure
%{?fc3:%{__perl} -pi.orig -e 's|net/bpf.h|pcap-bpf.h|' configure src/*.c src/*.h}
%{?fc2:%{__perl} -pi.orig -e 's|net/bpf.h|pcap-bpf.h|' configure src/*.c src/*.h}

%build
export LDFLAGS="-L%{_libdir} -L/%{_lib}"
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%if %{!?_without_freedesktop:1}0
        %{__install} -d -m0755 %{buildroot}%{_datadir}/applications
        desktop-file-install --vendor %{desktop_vendor}   \
		--delete-original                         \
                --add-category X-Red-Hat-Base              \
                --add-category Application                 \
                --add-category Network                     \
                --dir %{buildroot}%{_datadir}/applications \
                %{buildroot}%{_datadir}/gnome/apps/Applications/etherape.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING FAQ NEWS OVERVIEW README* TODO html/*.html
%doc %{_mandir}/man1/etherape.1*
%config %{_sysconfdir}/etherape/
%{_bindir}/etherape
%{_datadir}/etherape/
%{_datadir}/pixmaps/etherape.png
%{?_without_freedesktop:%{_datadir}/gnome/apps/Applications/etherape.desktop}
%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-etherape.desktop}

%changelog
* Wed Dec 22 2003 Dag Wieers <dag@wieers.com> - 0.9.1-1
- Updated to release 0.9.1.

* Tue Apr 29 2003 Dag Wieers <dag@wieers.com> - 0.9.0-0
- Initial package. (using DAR)
