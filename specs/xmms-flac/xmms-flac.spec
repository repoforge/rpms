# $Id$
# Authority: dag

### EL4 ships with xmms-flac-1.1.0-7.el4_5.2
%{?el4:# Tag: rfx}

%{!?dtag:%define _without_gettextdevel 1}
%{?fc2:  %define _without_gettextdevel 1}
%{?fc1:  %define _without_gettextdevel 1}
%{?el3:  %define _without_gettextdevel 1}
%{?rh9:  %define _without_gettextdevel 1}
%{?rh7:  %define _without_gettextdevel 1}
%{?el2:  %define _without_gettextdevel 1}

%define xmms_inputdir %(xmms-config --input-plugin-dir 2>/dev/null || echo %{_libdir}/xmms/General)

Summary: XMMS plugin needed to play FLAC (Free Lossless Audio Codec) files
Name: xmms-flac
Version: 1.2.1
Release: 2%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://flac.sourceforge.net/

Source: http://dl.sf.net/flac/flac-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: xmms-devel, libogg-devel, gettext
### Doesn't actually require it, but at least we won't build it for older FLAC releases
BuildRequires: flac-devel >= 1.1
%{!?_without_gettextdevel:BuildRequires: gettext-devel}

%description
FLAC is a Free Lossless Audio Codec. The FLAC format supports streaming,
seeking, and archival, and gives 25-75% compression on typical CD audio.
This is the input plugin for XMMS to be able to read FLAC files.

%prep
%setup -n flac-%{version}

%build
%configure --with-pic
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 src/plugin_xmms/.libs/libxmms-flac.so %{buildroot}%{xmms_inputdir}/libxmms-flac.so

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING.GPL
%{xmms_inputdir}/libxmms-flac.so

%changelog
* Sun Sep 30 2007 Dag Wieers <dag@wieers.com> - 1.2.1-1
- Updated to release 1.2.1.

* Thu Feb 15 2007 Matthias Saou <http://freshrpms.net/> 1.1.4-1
- Update to 1.1.4.
- Remove now included "xmms" patch.
- Remove no longer relevant "libtool" patch.
- No longer autoreconf, since we don't patch configure.in anymore.

* Mon Aug 28 2006 Matthias Saou <http://freshrpms.net/> 1.1.2-27
- FC6 rebuild.

* Mon Feb 13 2006 Matthias Saou <http://freshrpms.net/> 1.1.2-26
- Rebuild for new glibc/gcc.

* Tue Nov 22 2005 Matthias Saou <http://freshrpms.net/> 1.1.2-25
- Update patch with one provided from FLAC CVS by Øyvind Stegard to further
  fix configuration dialog crashes (#173723).

* Sat May 28 2005 Matthias Saou <http://freshrpms.net/> 1.1.2-24
- Bump release to 24 since main Core flac obsoletes xmms-flac < 1.1.2-24.
- Add patches from FC flac to fix libtool issues on x86_64.

* Thu May 19 2005 Matthias Saou <http://freshrpms.net/> 1.1.2-2
- Add patch to fix memory double freeing issue (bz #157796).

* Thu May 19 2005 Matthias Saou <http://freshrpms.net/> 1.1.2-1
- Initial RPM release since the plugin was disabled from the main flac in
  Core, because xmms was moved to Extras, thus no longer available at build
  time for Core packages.
- Laziness has made me include the whole 1.4MB of FLAC sources, but if
  someone wants to provide a simple script to extract only the relevant sources
  in order to create a custom source package of the plugin only, that would
  be great!
