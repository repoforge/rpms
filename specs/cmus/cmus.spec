# $Id$
# Authority: shuff
# Upstream: Gregory Petrosyan <gregory.petrosyan$gmail,com>
# ExcludeDist: el3 el4

%{?el5:%define _without_pulseaudio 1}

Summary: console music player
Name: cmus
Version: 2.4.1
Release: 1%{?dist}
Group: Applications/Multimedia
License: GPLv2+
URL: http://cmus.sourceforge.net/

Source: http://downloads.sourceforge.net/cmus/cmus-v%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: alsa-lib-devel >= 1.0.11
BuildRequires: faad2-devel
BuildRequires: ffmpeg-devel
BuildRequires: flac-devel
BuildRequires: libao-devel
BuildRequires: libmad-devel
BuildRequires: libmodplug-devel
BuildRequires: libmp4v2-devel
BuildRequires: libmpcdec-devel
BuildRequires: libvorbis-devel
BuildRequires: ncurses-devel
BuildRequires: wavpack-devel
%{!?_without_pulseaudio:BuildRequires: pulseaudio-libs-devel}

%description
cmus is a small and fast text mode music player for Linux and many
other UNIX-like operating systems.

%prep
%setup -n %{name}-v%{version}

%build
./configure \
    prefix=%{_prefix} \
    bindir=%{_bindir} \
    datadir=%{_datadir} \
    libdir=%{_libdir} \
    mandir=%{_mandir} \
    exampledir=%{_datadir}/%{name}/examples \
    CFLAGS="%{optflags}" \
    CONFIG_ARTS=n \
    CONFIG_PULSE=%{?_without_pulseaudio:n}%{!?_without_pulseaudio:y} \
    CONFIG_ROAR=n \
    CONFIG_SUN=n
%{__make} %{?_smp_mflags} V=2

%install
rm -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}

mv %{buildroot}%{_datadir}/%{name}/examples .
chmod -x examples/*

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README TODO contrib/ examples/
%doc %{_mandir}/man?/*
%{_bindir}/cmus
%{_bindir}/cmus-remote
%{_libdir}/cmus
%{_datadir}/cmus

%changelog
* Fri May 27 2011 Johannes Weißl <jargon@molb.org> - 2.4.1-1
- New upstream release

* Mon Apr 25 2011 Johannes Weißl <jargon@molb.org> - 2.4.0-1
- New upstream release

* Wed Apr 20 2011 Johannes Weißl <jargon@molb.org> - 2.3.5-1
- New upstream release

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 2.2.0-4
- rebuild for new F11 features

* Wed Dec 17 2008 Conrad Meyer <konrad@tylerc.org> - 2.2.0-3
- Make more verbosely (V=2).

* Tue Dec 16 2008 Conrad Meyer <konrad@tylerc.org> - 2.2.0-2
- Build ffmpeg support with gentoo patch.
- Remove libmikmod.

* Sun Nov 16 2008 Conrad Meyer <konrad@tylerc.org> - 2.2.0-1
- Initial package.
