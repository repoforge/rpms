# $Id: _template.spec 219 2004-04-09 06:21:45Z dag $
# Authority: dag
# Upstream: Eric Gerbier <gerbier@users.sf.net>

%define dfi %(which desktop-file-install &>/dev/null; echo $?)

%define real_version 2.1-0

Summary: File integrity checker
Name: afick
Version: 2.1
Release: 1
License: GPL
Group: Applications/System
URL: http://afick.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/afick/afick-%{real_version}.tgz
#Source: afick.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch

%description
afick is a portable file integrity checker
(it only needs standard perl to work).
it will be run daily by cron to detect new/deleted/modified files
It works by first (init) making an image of strategic directories attributes,
and then compare the disk status with this image.
A Graphical interface is available in afick-gui package.

%package gui
Summary: Graphical frontend for afick
Group: Applications/System
Requires: %{name} >= %{version}-%{release}, perl-Tk

%description gui
afick-gui is perl/tk tool for afick software
It can be used to launch afick with differents options
and to have a graphical view of results
It comes with menu for integration in kde/gnome ...

%prep
%setup -n %{name}-%{real_version}

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m0755 afick.pl %{buildroot}%{_bindir}/afick
%{__install} -D -m0755 afick-tk.pl %{buildroot}%{_bindir}/afick-tk

%{__install} -D -m0644 afick.conf %{buildroot}%{_sysconfdir}/afick.conf
%{__install} -D -m0644 afick.cron %{buildroot}%{_sysconfdir}/cron.daily/afick
%{__install} -D -m0644 afick.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/afick

%{__install} -D -m0644 afick.1 %{buildroot}%{_mandir}/man1/afick.1
%{__install} -D -m0644 afick-tk.1 %{buildroot}%{_mandir}/man1/afick-tk.1
%{__install} -D -m0644 afick.conf.5 %{buildroot}%{_mandir}/man1/afick.conf.5

%{__install} -D -m0644 afick.png %{buildroot}%{_datadir}/pixmaps/afick.png

%{__install} -d -m0755 %{buildroot}%{_localstatedir}/lib/afick/archive/
%{__install} -d -m0755 %{buildroot}%{_localstatedir}/log/afick/

%{__install} -D -m0644 afick.gnome %{buildroot}%{_datadir}/gnome/apps/System/afick.desktop

%if %{dfi}
%else
        %{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
        desktop-file-install --vendor gnome --delete-original \
                --add-category X-Red-Hat-Base                 \
                --dir %{buildroot}%{_datadir}/applications    \
                %{buildroot}%{_datadir}/gnome/apps/System/afick.desktop
%endif

%post
#if [ $1 -eq 1 ]; then
#	%{_bindir}/afick -i
#fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS Changelog COPYING COPYRIGHT INSTALL linux.conf NEWS README TODO *.html
%doc %{_mandir}/man?/afick.*
%config(noreplace) %{_sysconfdir}/afick.conf
%config(noreplace) %{_sysconfdir}/cron.daily/afick
%config(noreplace) %{_sysconfdir}/logrotate.d/afick
%{_bindir}/afick
%{_localstatedir}/lib/afick/
%{_localstatedir}/log/afick/

%files gui 
%defattr(-, root, root, 0755)
%doc Changelog-gui
%doc %{_mandir}/man?/afick-tk.*
%{_bindir}/afick-tk
%{_datadir}/pixmaps/*.png
%if %{dfi}
        %{_datadir}/gnome/apps/System/*.desktop
%else
        %{_datadir}/applications/*.desktop
%endif

%changelog
* Sun Apr 11 2004 Dag Wieers <dag@wieers.com> - 2.1-1
- Initial package. (using DAR)
