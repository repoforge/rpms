# $Id$
# Authority: dag

%define desktop_vendor rpmforge

Summary: Front-end to manage machine connections
Name: grcm
Version: 0.1.6
Release: 1
License: GPL
Group: Applications/Internet
URL: http://grcm.sourceforge.net/

Source: http://dl.sf.net/sourceforge/grcm/grcm-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: gnome-common
BuildRequires: libgnomeui-devel
Requires: openssh-clients

%description
Grcm, short for Gnome Remote Connection Manager, that provides an easy way to initiate connections to remote machines. It's primary goal is to provide a GUI to launch ssh, telnet and rdesktop type of applications, however it is highly configurable.

%prep
%setup

%build
#./autogen.sh --prefix="%{_prefix}"
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

desktop-file-install --delete-original         \
    --vendor %{desktop_vendor}                 \
    --add-category Application                 \
    --dir %{buildroot}%{_datadir}/applications \
    %{buildroot}%{_datadir}/gnome/apps/Internet/grcm.desktop

%{__rm} -f %{buildroot}%{_datadir}/pixmaps/grcm/Makefile*

%clean
%{__rm} -rf %{buildroot}

%files 
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%{_bindir}/grcm
%{_datadir}/applications/%{desktop_vendor}-grcm.desktop
%{_datadir}/gnome/help/grcm/
%{_datadir}/omf/grcm/
%{_datadir}/pixmaps/grcm/

%changelog
* Sun Jun 08 2008 Dag Wieers <dag@wieers.com> - 0.1.6-1
- Initial package. (using DAR)
