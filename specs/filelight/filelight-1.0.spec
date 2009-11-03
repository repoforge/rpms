# $Id$
# Authority: dag
# Upstream: Max Howell <filelight$methylblue,com>

Summary: Graphical disk usage statistics
Name: filelight
Version: 1.0
Release: 0.rc1%{?dist}
License: GPL
Group: Applications/System
URL: http://www.methylblue.com/filelight/

Source: http://www.methylblue.com/filelight/packages/filelight-%{version}-rc1.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: qt-devel >= 3.2, kdelibs-devel >= 3.2, gcc-c++, autoconf, automake, gettext

%description
Filelight graphically represents a file system as a set of concentric
segmented-rings, indicating where diskspace is being used. Segments
expanding from the center represent files (including directories),
with each segment's size being proportional to the file's size and
directories having child segments.

%prep
%setup

%build
source "/etc/profile.d/qt.sh"
%configure #--with-pic
%{__make} %{?_smp_mflags} RPM_OPT_FLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
#find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

#files -f %{name}.lang
%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
#%doc %{_docdir}/HTML/en/filelight/
%config %{_datadir}/config/filelightrc
%{_bindir}/filelight
%{_datadir}/applications/kde/filelight.desktop
%{_datadir}/apps/filelight/
%{_datadir}/icons/crystalsvg/*/actions/view_filelight.png
%{_datadir}/icons/hicolor/*/apps/filelight.png
%{_datadir}/services/filelight_part.desktop
%{_libdir}/kde3/libfilelight.la
%{_libdir}/kde3/libfilelight.so


%changelog
* Thu Sep 14 2006 Dag Wieers <dag@wieers.com> - 1.0-0.rc1
- Updated to release 1.0-rc1.

* Mon Aug 22 2005 Dag Wieers <dag@wieers.com> - 1.0-0.beta1
- Updated to release 1.0-beta1.

* Mon Aug 22 2005 Dag Wieers <dag@wieers.com> - 0.6.4-1
- Initial package. (using DAR)
