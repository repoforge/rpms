# $Id$
# Authority: dag
# Upstream: <unison-users$groups,yahoo,com>

%define desktop_vendor rpmforge


%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}

Summary: File-synchronization tool
Name: unison
Version: 2.13.16
Release: 1%{?dist}
License: GPL
Group: Applications/File
URL: http://www.cis.upenn.edu/~bcpierce/unison/

Source: http://www.cis.upenn.edu/~bcpierce/unison/download/releases/stable/unison-%{version}.tar.gz
Source1: unison.png
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

### emacs is needed for etags
BuildRequires: ocaml, emacs
#BuildRequires: tetex-latex, lablgtk >= 2.4.0, gtk2-devel
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}

%description
Unison is a file-synchronization tool. It allows two replicas of a collection
of files and directories to be stored on different hosts (or different disks
on the same host), modified separately, and then brought up to date by
propagating the changes in each replica to the other.

%prep
%setup

%{__cat} <<EOF >unison.desktop
[Desktop Entry]
Name=Unison File Synchronizer
GenericName=File Synchronizer
Exec=unison
Type=Application
Comment=Replicate files over different hosts or disks
Terminal=false
Icon=unison.png
StartupNotify=true
Encoding=UTF-8
EOF

%build
%{__make} %{?_smp_mflags} NATIVE="true" #UISTYLE="gtk2"

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 unison %{buildroot}%{_bindir}/unison
%{__install} -Dp -m0644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/unison.png

%if %{?_without_freedesktop:1}0
    %{__install} -Dp -m0644 unison.desktop %{buildroot}%{_datadir}/gnome/apps/Utilities/unison.desktop
%else
    %{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
    desktop-file-install \
        --vendor %{desktop_vendor}                 \
        --add-category X-Red-Hat-Base              \
        --dir %{buildroot}%{_datadir}/applications \
        unison.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CONTRIB COPYING NEWS README *.txt
%{_bindir}/unison
%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-unison.desktop}
%{?_without_freedesktop:%{_datadir}/gnome/apps/Utilities/unison.desktop}
%{_datadir}/pixmaps/unison.png

%changelog
* Fri Dec 02 2005 Dag Wieers <dag@wieers.com> - 2.13.16-1
- Updated to release 2.13.16.

* Thu Aug 11 2005 Dag Wieers <dag@wieers.com> - 2.12.0-1
- Initial package. (using DAR)
