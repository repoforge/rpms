# Authority: dag

Summary: A DJ software emulating an analog mixer with two playback devices.
Name: mixxx
Version: 1.2.1
Release: 0
License: GPL
Group: Applications/Multimedia
URL: http://mixxx.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://prdownloads.sourceforge.net/mixxx/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: glibc-devel, XFree86-devel, qt3-devel
BuildRequires: audiofile-devel, libmad-devel, portaudio
BuildRequires: fftw-devel

%description
Mixxx is DJ software emulating an analog mixer with two playback devices.

%prep
%setup

%build
%{?rhfc1:export QTDIR="/usr/lib/qt-3.1"}
%{?rhel3:export QTDIR="/usr/lib/qt-3.1"}
%{?rh90:export QTDIR="/usr/lib/qt3"}
%{?rh80:export QTDIR="/usr/lib/qt3"}
%{?rh73:export QTDIR="/usr/lib/qt2"}
%{?rh62:export QTDIR="/usr/lib/qt-2.1.0"}
cd src
qmake -makefile -unix
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir} \
			%{buildroot}%{_datadir}/mixxx/
%{__install} -m0755 src/mixxx %{buildroot}%{_bindir}
%{__cp} -auvx src/keyboard/ %{buildroot}%{_datadir}/mixxx/
%{__cp} -auvx src/midi/ %{buildroot}%{_datadir}/mixxx/
%{__cp} -auvx src/skins/ %{buildroot}%{_datadir}/mixxx/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING LICENCE README *.txt
%{_bindir}/*
%{_datadir}/mixxx/

%changelog
* Sun Jan 04 2004 Dag Wieers <dag@wieers.com> - 1.2.1-0
- Updated to release 1.2.1.

* Thu Oct 09 2003 Dag Wieers <dag@wieers.com> - 1.0.1-0
- Initial package. (using DAR)
