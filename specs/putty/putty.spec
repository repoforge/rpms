# $Id$
# Authority: dag
# Upstream: <putty@projects.tartarus.org>

%define dfi %(which desktop-file-install &>/dev/null; echo $?)

Summary: Graphical SSH, Telnet and Rlogin client
Name: putty
Version: 0.54
Release: 1
License: MIT
Group: Applications/Internet
URL: http://www.chiark.greenend.org.uk/~sgtatham/putty/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source0: http://the.earth.li/~sgtatham/putty/latest/putty-%{version}.tar.gz
Source1: putty.png
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk+-devel

%description
Putty is a SSH, Telnet & Rlogin client for Linux.

%prep
%setup

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=Putty Terminal Client
Comment=Log on to remote systems using SSH, Telnet or Rlogin
Exec=putty
Icon=putty.png
Terminal=false
Type=Application
StartupNotify=false
Categories=GNOME;Application;Network;
EOF

./mkfiles.pl

### FIXME: Disable missing pscp.1 and psftp.1. (Please fix upstream)
%{__perl} -pi.orig -e '
		s|-O2|%{optflags}|g;
		s|/usr/local|%{_prefix}|g;
		s|^(\t\$\(INSTALL_DATA\) -m 644 ps.+)$|#$1|;
	' unix/Makefile.gtk

%build
%{__make} %{?_smp_mflags} -C unix -f Makefile.gtk

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir} \
			%{buildroot}%{_mandir}/man1/ \
			%{buildroot}%{_datadir}/applications/ \
			%{buildroot}%{_datadir}/pixmaps/
%makeinstall -C unix -f Makefile.gtk

%if %{dfi}
	%{__install} -d -m0755 %{buildroot}%{_datadir}/gnome/apps/Network/
	%{__install} -m0644 %{name}.desktop %{buildroot}%{_datadir}/gnome/apps/Network/
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor gnome                \
		--add-category X-Red-Hat-Base              \
		--dir %{buildroot}%{_datadir}/applications \
		%{name}.desktop
%endif

%{__install} -m644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHECKLST.txt LICENCE MODULE README*
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_datadir}/pixmaps/*.png
%if %{dfi}
        %{_datadir}/gnome/apps/Network/*.desktop
%else
        %{_datadir}/applications/*.desktop
%endif

%changelog
* Sun Apr 04 2004 Dag Wieers <dag@wieers.com> - 0.54-1
- Disabled StartupNotify in desktop-file. (Gavin Henry)

* Mon Feb 16 2004 Dag Wieers <dag@wieers.com> - 0.54-0
- Updated to release 0.54.

* Mon Nov 24 2003 Dag Wieers <dag@wieers.com> - 0.53-0.20030821
- Initial package. (using DAR)
