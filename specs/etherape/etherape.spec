# $Id$
# Authority: dag

%define dfi %(which desktop-file-install &>/dev/null; echo $?)

Summary: Graphical network viewer modeled after etherman
Name: etherape
Version: 0.9.0
Release: 1
License: GPL
Group: Applications/System
URL: http://etherape.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/etherape/etherape-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: libpcap

%description
Etherape is a graphical network monitor for Unix modeled after
etherman. Featuring ether, ip and tcp modes, it displays network
activity graphically. Hosts and links change in size with traffic. 
Color coded protocols display. It supports ethernet, ppp and slip 
devices. It can filter traffic to be shown, and can read traffic 
from a file as well as live from the network. 

%prep
%setup

%build
%configure \
	--disable-dependency-tracking
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%if %{dfi}
%else
        %{__install} -d -m0755 %{buildroot}%{_datadir}/applications
        desktop-file-install --vendor gnome --delete-original \
                --add-category X-Red-Hat-Base                 \
                --add-category Application                    \
                --add-category Network                        \
                --dir %{buildroot}%{_datadir}/applications    \
                %{buildroot}%{_datadir}/gnome/apps/Applications/%{name}.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING FAQ NEWS OVERVIEW README* TODO html/*.html
%doc %{_mandir}/man?/*
%config %{_sysconfdir}/etherape/
%{_bindir}/*
%{_datadir}/etherape/
%{_datadir}/pixmaps/*
%if %{dfi}
        %{_datadir}/gnome/apps/Applications/*.desktop
%else
        %{_datadir}/applications/*.desktop
%endif

%changelog
* Tue Apr 29 2003 Dag Wieers <dag@wieers.com> - 0.9.0-0
- Initial package. (using DAR)
