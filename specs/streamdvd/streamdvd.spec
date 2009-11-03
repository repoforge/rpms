# $Id$
# Authority: dag

%define real_name StreamDVD

Summary: Tool to backup DVDs
Name: streamdvd
Version: 0.4
Release: 2%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://www.badabum.de/streamdvd.html

Source: http://www.badabum.de/down/streamdvd-%{version}.tar.gz
Patch0: streamdvd-0.4-makefile.patch
Patch1: streamdvd-0.4-streamdvd.patch
Patch2: streamdvd-0.4-lsdvd.patch
Patch3: streamdvd-0.4-gui.patch
Patch4: streamdvd-0.4-gcc41.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, libdvdread-devel >= 0.9.2, perl
Requires: lsdvd

Obsoletes: streamdvd-streamanalyze <= %{version}-%{release}
Provides: streamdvd-streamanalyze = %{version}-%{release}

%description
StreamDVD is a fast tool to backup Video DVDs 'on the fly', there will be
no ripping, demultiplexing, recoding, remultiplexing ....

You can select the wanted title, chapters, video, audio and subpicture
streams and also a resize factor and StreamDVD will write a 'ready to
author' vob file to stdout. 

%package gui
Summary: Graphical user interface for streamdvd
Group: User Interface/X
Requires: %{name} = %{version}-%{release}
Requires: dvdauthor >= 0.6.5, mkisofs >= 1.15, dvd+rw-tools >= 5.13.4.7.4
Requires: perl(Tk), perl(Tk::BrowseEntry), perl(Tk::Photo), perl(Tk::JPEG)

%description gui
Graphical user interface for streamdvd

%prep
%setup -n %{real_name}-%{version}
%patch0
%patch1
%patch2
%patch3
%patch4 -p1

%{__perl} -pi.orig -e 's|(Tk::JPEG)::Lite|$1|' Gui/StreamDVD/Gui.pm

%build
%{__make} %{?_smp_mflags} gui CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir}
%{__make} install INSTALLDIR="%{buildroot}%{_bindir}"

%{__install} -d -m0755 %{buildroot}%{perl_vendorarch}/StreamDVD/
%{__install} -Dp -m0644 Gui/StreamDVD/*.pm %{buildroot}%{perl_vendorarch}/StreamDVD/
%{__install} -Dp -m0755 Gui/StreamDVD.pl %{buildroot}%{_bindir}/StreamDVD

### Clean up buildroot
%{__rm} rf %{buildroot}%{_bindir}/lsdvd

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README
%doc contrib/StreamAnalyze/README contrib/StreamAnalyze/COPYING
%doc contrib/lsdvd/AUTHORS contrib/lsdvd/COPYING contrib/lsdvd/README
%{_bindir}/streamanalyze
%{_bindir}/streamdvd

%files gui
%defattr(-, root, root, 0755)
%doc Gui/README
%{_bindir}/StreamDVD
%{perl_vendorarch}/StreamDVD/

%changelog
* Sun Apr 01 2007 Dag Wieers <dag@wieers.com> - 0.4-2
- Added Livna patches.

* Fri Dec 03 2004 Dag Wieers <dag@wieers.com> - 0.4-1
- Initial package. (using DAR)
