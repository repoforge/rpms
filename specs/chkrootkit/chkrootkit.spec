# $Id$

# Authority: dag

%define dfi %(which desktop-file-install &>/dev/null; echo $?)

Summary: Check locally for signs of a rootkit
Name: chkrootkit
Version: 0.43
Release: 2
License: COPYRIGHTED
Group: Applications/System
URL: http://www.chkrootkit.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source0: ftp://ftp.pangeia.com.br/pub/seg/pac/chkrootkit-%{version}.tar.gz
Source1: chkrootkit.png
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


%description
chkrootkit is a tool to locally check for signs of a rootkit.

%prep
%setup

%{__cat} <<EOF >chkrootkit.apps
USER=root
PROGRAM=%{_libdir}/chkrootkit-%{version}/chkrootkit.sh
SESSION=true
EOF

%{__cat} <<EOF >chkrootkit.pam
#%PAM-1.0
auth       sufficient	pam_rootok.so
auth       sufficient   pam_timestamp.so
auth       required	pam_stack.so service=system-auth
session	   required	pam_permit.so
session    optional	pam_xauth.so
session    optional     pam_timestamp.so
account    required	pam_permit.so
EOF

%{__cat} <<EOF >chkrootkit.sh
#!/bin/sh
cd %{_libdir}/chkrootkit-%{version}
exec %{_libdir}/chkrootkit-%{version}/chkrootkit
EOF

%{__cat} <<EOF >xchkrootkit.sh
#!/bin/sh
%{_bindir}/chkrootkit
echo "Press ENTER to exit"
read ENDSCRIPT
EOF

%{__cat} <<EOF >chkrootkit.desktop
[Desktop Entry]
Name=Chkrootkit Rootkit Detection
Comment=Check your system for rootkits
Icon=chkrootkit.png
Exec=xchkrootkit
Terminal=true
Type=Application
Encoding=UTF-8
Categories=Application;System;
EOF

%build
%{__make} sense

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir} \
			%{buildroot}%{_libdir}/chkrootkit-%{version}/ \
			%{buildroot}%{_sysconfdir}/security/console.apps/ \
			%{buildroot}%{_sysconfdir}/pam.d/ \
			%{buildroot}%{_datadir}/pixmaps/

%{__install} -m0644 chkrootkit.apps %{buildroot}%{_sysconfdir}/security/console.apps/chkrootkit
%{__install} -m0644 chkrootkit.pam %{buildroot}%{_sysconfdir}/pam.d/chkrootkit

%{__install} -m0755 xchkrootkit.sh %{buildroot}%{_bindir}/xchkrootkit
%{__ln_s} -f %{_bindir}/xchkrootkit %{buildroot}%{_bindir}/chkrootkitX
%{__ln_s} -f %{_bindir}/consolehelper %{buildroot}%{_bindir}/chkrootkit

%{__install} -m0755 check_wtmpx chkdirs chklastlog chkproc chkrootkit chkrootkit.sh chkwtmp ifpromisc strings-static %{buildroot}%{_libdir}/chkrootkit-%{version}/

%{__install} -m0644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/chkrootkit.png

%if %{dfi}
        %{__install} -d -m0755 %{buildroot}%{_datadir}/gnome/apps/Utilities/
        %{__install} -m0644 chkrootkit.desktop %{buildroot}%{_datadir}/gnome/apps/Utilities/
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor gnome                \
		--add-category X-Red-Hat-Base              \
		--dir %{buildroot}%{_datadir}/applications \
		chkrootkit.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ACKNOWLEDGMENTS COPYRIGHT README*
%config %{_sysconfdir}/pam.d/*
%config %{_sysconfdir}/security/console.apps/*
%{_bindir}/*
%{_libdir}/chkrootkit-%{version}/
%{_datadir}/pixmaps/*.png
%if %{dfi}
        %{_datadir}/gnome/apps/Utilities/*.desktop
%else
        %{_datadir}/applications/*.desktop
%endif

%changelog
* Fri Mar 12 2004 Dag Wieers <dag@wieers.com> - 0.43-2
- Change to chkrootkit-path on execution. (gh)

* Tue Mar 02 2004 Dag Wieers <dag@wieers.com> - 0.43-1
- Fixed to the normal chkrootkit script. (Clifford Snow)

* Fri Feb 27 2004 Dag Wieers <dag@wieers.com> - 0.43-0
- Updated to release 0.43.

* Fri Aug 15 2003 Dag Wieers <dag@wieers.com> - 0.41-0
- Initial package. (using DAR)
