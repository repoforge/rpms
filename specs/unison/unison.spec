# $Id$
# Authority: dag
# Upstream: <unison-users$groups,yahoo,com>

%define desktop_vendor rpmforge

Summary: File-synchronization tool
Name: unison
Version: 2.40.63
Release: 1%{?dist}
License: GPLv3
Group: Applications/File
URL: http://www.cis.upenn.edu/~bcpierce/unison/

Source: http://www.cis.upenn.edu/~bcpierce/unison/download/releases/stable/unison-%{version}.tar.gz
Source1: unison.png
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: desktop-file-utils
### emacs is needed for etags
BuildRequires: emacs
BuildRequires: ocaml
#BuildRequires: gtk2-devel
#BuildRequires: lablgtk >= 2.4.0
#BuildRequires: tetex-latex

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
%{__make}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 unison %{buildroot}%{_bindir}/unison
%{__install} -Dp -m0644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/unison.png

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install \
    --vendor %{desktop_vendor}                 \
    --add-category X-Red-Hat-Base              \
    --dir %{buildroot}%{_datadir}/applications \
    unison.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CONTRIB COPYING NEWS README *.txt
%{_bindir}/unison
%{_datadir}/applications/%{desktop_vendor}-unison.desktop
%{_datadir}/pixmaps/unison.png

%changelog
* Thu Aug 18 2011 Bjarne Saltbaek <arnebjarne72@hotmail.com> - 2.40.63-1
- Updated to release 2.40.63.

* Tue Jan 05 2010 Dag Wieers <dag@wieers.com> - 2.32.52-1
- Updated to release 2.32.52.

* Sun Feb 03 2008 Dag Wieers <dag@wieers.com> - 2.27.57-1
- Updated to release 2.27.57.

* Fri Dec 02 2005 Dag Wieers <dag@wieers.com> - 2.13.16-1
- Updated to release 2.13.16.

* Thu Aug 11 2005 Dag Wieers <dag@wieers.com> - 2.12.0-1
- Initial package. (using DAR)

