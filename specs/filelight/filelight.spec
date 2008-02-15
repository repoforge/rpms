# $Id$
# Authority: dag
# Upstream: Max Howell <filelight$methylblue,com>

Summary: Graphical disk usage statistics
Name: filelight
Version: 0.6.4
Release: 1.2
License: GPL
Group: Applications/System
URL: http://www.methylblue.com/filelight/

Source: http://www.methylblue.com/filelight/packages/filelight-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: qt-devel >= 3.1, kdelibs-devel >= 3.1, gcc-c++

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
%configure  LDFLAGS="$LDFLAGS -L/usr/X11R6/%{_lib}"
%{__make} %{?_smp_mflags} RPM_OPT_FLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%doc %{_docdir}/HTML/en/filelight/
%config %{_datadir}/config/filelightrc
%{_bindir}/filelight
%{_datadir}/applnk/Utilities/filelight.desktop
%{_datadir}/apps/filelight/
%{_datadir}/icons/crystalsvg/*/apps/filelight.png

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.6.4-1.2
- Rebuild for Fedora Core 5.

* Mon Aug 22 2005 Dag Wieers <dag@wieers.com> - 0.6.4-1
- Initial package. (using DAR)
