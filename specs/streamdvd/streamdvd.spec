# $Id$
# Authority: dag

%define real_name StreamDVD

Summary: Tool to backup DVDs
Name: streamdvd
Version: 0.4
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://www.badabum.de/streamdvd.html

Source: http://www.badabum.de/down/streamdvd-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libdvdread-devel >= 0.9.2

%description
StreamDVD is a fast tool to backup Video DVDs. You can select the desired
title, chapters, video, audio and subpicture streams and also a resize
factor and StreamDVD will write a 'ready to author' vob file to stdout.

%prep
%setup -n %{real_name}-%{version}

%build
%{__make} %{?_smp_mflags} \
	CFLAGS="%{optflags}"
%{__make} %{?_smp_mflags} -C contrib/StreamAnalyze \
	CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 streamdvd %{buildroot}%{_bindir}/streamdvd
%{__install} -Dp -m0755 contrib/StreamAnalyze/streamanalyze %{buildroot}%{_bindir}/streamanalyze

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README
%{_bindir}/streamanalyze
%{_bindir}/streamdvd

%changelog
* Fri Dec 03 2004 Dag Wieers <dag@wieers.com> - 0.4-1
- Initial package. (using DAR)
