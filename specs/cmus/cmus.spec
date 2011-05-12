# $Id$
# ExcludeDist: el3 el4

%{?el5:%define _without_pulseaudio 1}

Name:           cmus
Version:        2.4.0
Release:        1%{?dist}
Summary:        Ncurses-Based Music Player
Group:          Applications/Multimedia
License:        GPLv2+
URL:            http://cmus.sourceforge.net/
Source0:        http://downloads.sourceforge.net/cmus/cmus-v%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  alsa-lib-devel >= 1.0.11
BuildRequires:  faad2-devel
BuildRequires:  ffmpeg-devel
BuildRequires:  flac-devel
BuildRequires:  libao-devel
BuildRequires:  libmad-devel
BuildRequires:  libmodplug-devel
BuildRequires:  libmp4v2-devel
BuildRequires:  libmpcdec-devel
BuildRequires:  libvorbis-devel
BuildRequires:  wavpack-devel
%{!?_without_pulseaudio:BuildRequires: pulseaudio-libs-devel}

BuildRequires:  ncurses-devel


%description
cmus is a small and fast text mode music player for Linux and many
other UNIX-like operating systems.



%prep
%setup -q -n %{name}-v%{version}


%build
./configure prefix=%{_prefix} bindir=%{_bindir} datadir=%{_datadir} \
  libdir=%{_libdir} mandir=%{_mandir} \
  exampledir=%{_datadir}/%{name}/examples \
  CONFIG_ROAR=n CONFIG_ARTS=n CONFIG_SUN=n \
  %{?_without_pulseaudio:CONFIG_PULSE=n} \
  CFLAGS="%{optflags}"
make %{?_smp_mflags} V=2


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_datadir}/%{name}/examples .
chmod -x examples/*


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc COPYING AUTHORS examples
%{_bindir}/%{name}
%{_bindir}/cmus-remote
%{_libdir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/cmus-remote.1*
%{_mandir}/man1/cmus.1*
%{_mandir}/man7/cmus-tutorial.7*


%changelog
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
