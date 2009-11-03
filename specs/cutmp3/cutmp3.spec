# $Id$
# Authority: dag

Summary: Command line MP3 editor
Name: cutmp3
Version: 1.8.6
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://www.puchalla-online.de/cutmp3.html

Source: http://www.puchalla-online.de/cutmp3-%{version}.tar.bz2
Patch0: cutmp3-1.8.6-makefile.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: readline-devel, ncurses-devel

%description
cutmp3 is a small and fast command line MP3 editor.  It lets you select
sections of an MP3 interactively or via a timetable and save them to
separate files without quality loss.  It uses mpg123 for playback and
works with VBR files and even with files bigger than 2GB.  Other
features are configurable silence seeking and ID3 tag (v1.1) seeking,
which are useful for concatenated mp3s.

%prep
%setup
%patch0

%build
%{__make} %{?_smp_mflags} CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_datadir}/apps/konqueror/servicemenus
%{__make} install DESTDIR="%{buildroot}" prefix="%{_prefix}" kdedir="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc BUGS Changelog COPYING README* USAGE
%doc %{_mandir}/man1/cutmp3.1*
%{_bindir}/cutmp3
%{_datadir}/apps/konqueror/servicemenus/cutmp3.desktop

%changelog
* Mon Dec 11 2006 Dag Wieers <dag@wieers.com> - 1.8.6-1
- Initial package. (using DAR)
